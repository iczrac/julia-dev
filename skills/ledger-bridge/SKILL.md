# 帳本橋接：julia-dev 對接 ledger-driven-dev（濃縮版）

> 來源：[ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev)（MIT，Copyright 2026 Ledger-Driven Dev contributors）。本檔為方法論濃縮重述，非原文複製；只保留互通所需的命令名、欄位名與 fail-closed 紀律。原專案的腳本、模板與帳本不內嵌，授權見 `ATTRIBUTION.md`。

## 何時用

由Luca（帳本對接官）在Julia派工時使用：

- 使用者明確要求與 ledger 協作，或目標專案已有 `governance/DECISION_LEDGER.json`
- 需要把人話需求轉成 `intent.json`，或把 `next_queue` 任務卡轉成 Julia 的工作任務
- 需要把Vera的證據換算成 ledger 的 `declared / verified`，或準備 `approval_bundle`

**不適用**：小修小補、尚未辨析需求、帳本未通過 `verify_ledger`、意圖混淆且沒有人可確認。

## 三條硬邊界

| 邊界 | 內容 |
|------|------|
| 事實邊界 | ledger 是專案事實源；OKF 是外部知識可信層；footprint 只是工作現場草稿。三者不互相複製 |
| 路由邊界 | ledger 決定「誰有資格寫」，Julia 決定「誰來執行」。衝突時寫入資格以 ledger 為準 |
| 寫入邊界 | 橋接角色不直接寫帳本；寫入只經 `agent_gateway`，且必須有人批准本輪授權 |

## Preflight（對接前檢查，未通過不得呼叫任何橋接命令）

0. **骨架就緒**：全新 greenfield 骨架必須先跑生成器再校驗——`init_project` → `build_capability_model --dry-run` → 正式生成 → `verify_ledger --strict`；registry 宣告的 impl 檔必須真實存在（`registry_impls_exist`），缺檔先補實現
1. **帳本可信**：`governance/DECISION_LEDGER.json` 存在，且 `verify_ledger.py --strict` 無 fail
2. **腳本可用**：`intent_restate`／`route_expert`／`expert_run`／`run_tests`／`verify_ledger`／`agent_gateway` 都能執行（`--help` 不報缺模組）；腳本不在包內，依賴目標專案安裝的 ledger 版本
3. **版本與指紋留痕（v2.24.0 起）**：把 `METHOD_VERSION`、`method_assets`／`installed_assets`／`ontology` 摘要一起寫入足跡，後續每次對接先比對；任一漂移即重新路由，不沿用舊裁決。**同時跑 `upgrade.py verify`**：ledger 側每次版本更新都會重綁資產指紋，changelog 明言「目標項目需重新批准升級」——verify 未過（`upgrade_complete=false` 或要求 re-approve）時，記入解阻清單請人批准，批准前不得沿用既有 `verified` 結論
4. **綁定預檢**：在跑測試前對照三個實測坑檢查測試結構——① 測試檔在 `tests/unit/`（不在 `tests/` 根）；② `src/` 各層有 `__init__.py`；③ 測試內 `sys.path` 深度與目錄層級一致。結構不對先修再跑，不要等 binding 失敗後回頭查
5. **文檔門禁基線（v2.24.0 起）**：`check.sh` 第 17 節為文檔生命週期 shadow 門（orphan／suspect／stale_unknown／信任告警／uncovered／obligation_missing／派生漂移）。shadow 期告警不阻斷但**必須記入足跡作為基線**，後續對接比對增量；`--strict` 若被目標項目開啟則視為硬門
6. **失敗降級**：任一項失敗即停，向使用者說明「ledger 不可用」，詢問是否降級為非治理任務（Vera `PASS` 交付）

## 四個交接對象

### 1. `intent.json`

```json
{
  "schema": "intent-restate/0",
  "raw_intent": "<使用者原話>",
  "restatement": "<_agent 自己的話，不得照抄>",
  "intents": ["code"],
  "capabilities": ["PROJ.MODULE.DOMAIN.01"],
  "write_scope": ["src/**", "tests/**"],
  "open_questions": []
}
```

- 每個能力碼必須在 registry 或帳本中真實存在
- 唯讀意圖的 `write_scope` 必須是 `["none"]`
- `meta` 意圖必填 `open_questions`
- 非 `allow` 即停，不猜、不降級

```bash
python3 scripts/intent_restate.py --target <P> --intent-file intent.json --json
```

### 2. `route.handoff` 與 `next_queue`

```bash
python3 scripts/route_expert.py --target <P> --intent "<原話>" --intent-file intent.json --json
python3 scripts/expert_run.py --target <P> --intent-file intent.json --json
python3 scripts/provenance_view.py --target <P> --kind task --json
python3 scripts/work_panel.py --target <P> nodes --json
```

只取一張任務卡，轉換成 Julia 的 Worker 交接：

- `code` → `scopedGoal` 的能力錨點
- `missing_evidence` → `acceptance` 與 `verify`
- `docs` → 必讀資料
- `decisions` / `lessons` → 背景與前人踩過的坑
- **經驗對照（進化觸發器）**：任務卡的經驗與 julia-dev 現有 Skill／成員規範衝突、或同一經驗重複出現 ≥2 次時，Luca 在交接末尾附**進化提案線索**（格式見 `skills/self-evolution/SKILL.md`；只提案線索，不修改任何檔案）
- `target_level` → `definition_of_done`（**唯一來源是 registry 人工聲明的 `committed`／`target_level`**；CAPABILITY_INDEX 只是現狀投影，Julia 不得自行推斷或補寫 target_level，v2.24.0 `compare_graphs` 新增 `no_target` 狀態表示「未聲明目標」，不參與對齊與完成度）

不要一次把多張卡塞進同一個 worker。

### 3. `test_report` 與 `verify_ledger` JSON

Vera的 PASS 必須同時滿足：

1. 有合乎 `ledger-test-report/1` 的報告（或合規適配後的 JUnit／jest／JSON）
2. 報告 `overall=pass`
3. `evidence_binding.inputs` 非空且新鮮
4. 能力碼或測試檔案有真實綁定（`bound`）
5. `verify_ledger --strict` 無 fail

```bash
python3 scripts/run_tests.py --dir tests --out governance/test_report.json
python3 governance/build_capability_model.py --root <P> --test-report <P>/governance/test_report.json --dry-run
python3 governance/verify_ledger.py --root <P> --strict --json
```

若只通過 `--dry-run`，不代表已寫入帳本；這是刻意保留的人工寫入點。

**運行時綁定要求（smoke test 實測，2026-11-24）**——`verified` 是雙條件：報告有 pass 記錄 **且** 符號級綁定證明測的是本能力實現：

- 測試必須放在 `tests/unit/`（L3 目錄約定），放在 `tests/` 根不會被派生為 unit_test 證據
- 測試 import 必須能沿 `__init__.py` 鏈解析到 registry 宣告的 impl 檔——`src/` 各層要有 `__init__.py`，測試內 `sys.path` 深度要與目錄層級一致
- `binding_status`：只有 `bound` 升級 `verified`；`via1`（隔一跳編排層）／`unbound`／`no_tests`／`no_impl` 一律維持 `declared`，不得宣稱已驗證

### 4. `approval_bundle` 與 `audit`

```bash
python3 scripts/agent_gateway.py --target <P> status --json
# 以下預設 dry-run；只有人與Ship可在授權後 --apply
python3 scripts/agent_gateway.py --target <P> request --agent <id> --action <action> \
  --code <CAP.CODE> --expect-fingerprint <FP> --json
```

`approval_bundle` 只列命令，不執行。被 `deny` 時不得換 id、換動作重試；回到 `route_expert` 或請人裁決。

**網關實測紀律（smoke test）**：`--action` 是固定枚舉（`code`／`claim`／`decide`／`verify`／`route` 等，**沒有** `write`）；`request` 預設 dry-run（`applied=false`），未登記的 agent 一律 deny 且逐項給 fix 指引（access 登記、agent 身份、CAS 指紋、registry 摘要）——把 fix 原文放進解阻清單，由人工批准後再帶 `--apply`。

## 角色映射

| ledger 側 | julia-dev 側 | 纪律 |
|-----------|--------------|------|
| `expert-router` | Luca＋Julia | 唯讀路由，不寫 |
| `intent-restate` | Julia Phase 0＋Remy任務契約 | 接受標準要碼化 |
| `project-archaeologist` | Tracey | 源碼盤點可作為草稿素材，不覆蓋既有治理檔 |
| `greenfield-architect` | Archie | 治理骨架不等於系統架構 |
| `loop-executor` | Mark／Tracey／Archie | 一卡一 scope，寫入走網關 |
| `evidence-auditor` | Vera | 只讀驗證，不自己修帳本 |
| `ledger-steward` | 人工裁決；Ed只給建議 | 橋接角色不代寫決策或經驗 |
| `release-steward` | Ship | 解凍／歸檔／退役必須人批准 |
| `goal-orchestrator` | Julia Workflow S | 方向鎖、預算與停滯檢查照 ledger |
| OKF／簡報 | Knox／Della | 不併入 ledger 核心 |

## 與 julia-dev Workflow 的接合點

| Julia 階段 | 橋接動作 |
|-----------|----------|
| Phase 0 | 人話 → `intent.json`；缺欄位就請Remy補 |
| Phase 0.5 | 復述門／路由／編排；`blocked` 就停 |
| Workflow S | `next_queue` → 任務圖；保留 `dependsOn` 與 `measurements[]` |
| Phase 4 | Vera證據 → `evidence_tier`／`binding_status`／`verify_ledger` |
| Phase 7 | `approval_bundle` → 人工批准 → Ship執行 |
| Workflow U | 以上串成一條完整帳本對接鏈 |

## Fail-closed 對照

| 情況 | 動作 |
|------|------|
| `restate_gate` 非 allow | 停，回 `open_questions` |
| `route.blocked=true` 或 `confidence=low` | 停，不派遣 |
| `handoff` 缺 facts／stop_if | 視為路由未完成 |
| `verify_ledger` fail | 不得給 PASS，不得寫入 |
| `evidence_binding.inputs=0` | 降為 `declared`，不得宣稱 verified |
| `source-dir` 與真實 monorepo 佈局不符 | 停，先校正路徑契約 |
| `agent_gateway` deny | 停，不改 id 重試 |
| ledger 版本／摘要漂移 | 重新路由，不沿用舊裁決 |
| `upgrade verify` 未過（需重新批准升級） | 記入解阻清單請人批准 `upgrade apply --approved-by <人>`；批准前不得沿用既有 `verified` |
| 工具指紋漂移後既有證據 | 依硬規則 13 重跑產證，不得拿舊章當新章 |

## 規範型倉庫自查（spec_check）

julia-dev 本身是規範型倉庫（主體為 Markdown 規範、無代碼符號可綁定）。六類可判定自查——術語殘留／版本一致／派生漂移／必備檔案／連結解析／本體完整——**不在本倉庫重複實現**，統一使用 ledger 側 `scripts/spec_check.py`（配置：倉庫根 `spec_check.json`，schema `spec-check/1`）：

- **本地副本（唯一執行處）**：`/Volumes/LQVault/RacAIWorkingRoom/CapabilityForge/ledger-driven-dev`（與遠端 github.com/iczrac/ledger-driven-dev 對齊）；執行 `python3 /Volumes/LQVault/RacAIWorkingRoom/CapabilityForge/ledger-driven-dev/scripts/spec_check.py --target .`
- **進化落地後必跑**：每次版本變更提交前執行上述自查；退出碼 1 的命中必須清零或經使用者拍板豁免
- **歷史記錄豁免唯一**：`docs/evolution-log.md` 是舊名／歷史映射的唯一合法記錄地（scan.exclude），其餘文檔一律不允許出現禁用舊名
- **邊界紀律**：自查判據屬「真相與規則」，隨 ledger 版本升級；本倉庫只維護配置，不得 fork 工具或內嵌第二份檢查器

## 解阻（Andon）

停不是終點。每次 fail-closed 停下，必須向主理人回傳**解阻清單**：阻塞原因、誰能解（人／Remy補 `open_questions`／Luca重路由）、所需動作、已嘗試步驟。按情況處理：

| 情況 | 解阻動作 |
|------|---------|
| 復述門非 `allow` | 請Remy補齊 `open_questions` 後重跑**一次**；仍非 `allow` → Andon 給使用者 |
| `route.blocked` 或 `confidence=low` | 補 `intent.json` 或請人裁決；不得猜測派遣 |
| `verify_ledger` fail | 交Vera修測試或請人裁決；不得軟化結論 |
| `evidence_binding.inputs=0` | 補齊新鮮證據後重算；在此之前只能稱 `declared` |
| `agent_gateway` deny | 停，回到 `route_expert` 或請人裁決；**禁止換 id、換動作重試** |
| 同一阻塞卡兩次 | 主理人向使用者 Andon：事實／選項／建議／需要的決定，四段固定格式 |

## 硬規則

1. Luca只讀、只翻譯、只準備；不寫帳本、不開 PR、不合併、不批准。
2. 只交換四類物件：`intent.json`、`route/handoff/next_queue`、`test_report + verify JSON`、`approval_bundle/audit`。
3. 不把完整帳本複製進 julia-dev，只傳當前任務卡、相關決策、相關經驗與證據路徑。
4. Vera的聊天式 PASS 不等於 ledger 的 `verified`；必須有報告、綁定與不變量通過。
5. 人工確認門禁 > ledger 寫入門禁 > 不可逆動作確認 > Vera `PASS` > 其餘可逆工作。
6. 任何 `--apply`、`register`、`unfreeze`、`archive` 都屬批准包，不是橋接角色可自行執行的命令。
7. 所有交接經Julia中轉，團員不互相直連。
8. `intent.json` 是唯一契約入口；Julia的任務契約是它的執行投影。intent 變更後必須重跑復述門與路由，禁止兩邊各自修改。
9. 對接前必須先跑 Preflight；未通過不得呼叫任何橋接命令。
10. 治理專案內Vera的結論必須是 `verified-PASS`（五條件全過）；`PASS` 與 `verified-PASS` 不得混用。
11. 治理專案 Phase 4 **必須經 `run_tests.py` 產證**（輸出合乎 `ledger-test-report/1` 或合規適配格式）；Vera不得另起爐灶自帶方式跑測試後直接換算 tier——證據格式不符會讓 `evidence_binding` 失真。
12. Preflight 對治理專案的**每次會話接手**都必須重跑（從第 0 步起）：帳本可能已被其他 agent 寫過，舊 Preflight 結論不得沿用。
13. **證據降級條款（v2.24.0 起）**：ledger 工具哈希漂移會使 `evidence_binding` 失效，既有 `verified` **靜默回落 `declared`**——工具或資產指紋與足跡不一致時，該專案全部 `verified` 能力碼視為已降級，必須重跑 `run_tests.py` 產證並重新綁定後才可再稱 `verified-PASS`；不得拿升級前的舊章對外宣稱。
14. **文檔寫入路由（v2.24.0 起）**：治理項目中 `docs/**` 變更必須經 intent 聲明走 ledger 路由（doc+code → `ledger-steward`，doc+verify → `evidence-auditor`，三者並存觸發澄清）；julia-dev 成員**不得直寫** `docs/**`——`docs.registry`／`docs.obligations` 僅 ledger-steward 可寫，正文僅 loop-executor 路由；文檔骨架／過期標記等操作用 ledger 側 `doc-lifecycle` 技能（scaffold／lint／mark-stale／check），派生文檔（`docs/generated/`）只可由生成器重算、手改即漂移。
15. **門禁口徑（v2.25.0 起）**：`0` 與 `n/a` 是兩回事——gate 指標為 `n/a`（判據不適用／未判定）時**不得視為通過**；`stale_unknown`（缺 `stale_after`）單列、不併入 `stale`；缺鍵一律 fail-closed 上報，不許當「未過期」處理。verified-PASS 引用任何 gate 指標時同樣適用此口徑。
