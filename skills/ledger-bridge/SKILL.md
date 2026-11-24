# 帳本橋接：julia-dev 對接 ledger-driven-dev（濃縮版）

> 來源：[ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev)（MIT，Copyright 2026 Ledger-Driven Dev contributors）。本檔為方法論濃縮重述，非原文複製；只保留互通所需的命令名、欄位名與 fail-closed 紀律。原專案的腳本、模板與帳本不內嵌，授權見 `ATTRIBUTION.md`。

## 何時用

由盧卡（帳本對接官）在茱莉亞派工時使用：

- 使用者明確要求與 ledger 協作，或目標專案已有 `governance/DECISION_LEDGER.json`
- 需要把人話需求轉成 `intent.json`，或把 `next_queue` 任務卡轉成 Julia 的工作任務
- 需要把維拉的證據換算成 ledger 的 `declared / verified`，或準備 `approval_bundle`

**不適用**：小修小補、尚未辨析需求、帳本未通過 `verify_ledger`、意圖混淆且沒有人可確認。

## 三條硬邊界

| 邊界 | 內容 |
|------|------|
| 事實邊界 | ledger 是專案事實源；OKF 是外部知識可信層；footprint 只是工作現場草稿。三者不互相複製 |
| 路由邊界 | ledger 決定「誰有資格寫」，Julia 決定「誰來執行」。衝突時寫入資格以 ledger 為準 |
| 寫入邊界 | 橋接角色不直接寫帳本；寫入只經 `agent_gateway`，且必須有人批准本輪授權 |

## Preflight（對接前檢查，未通過不得呼叫任何橋接命令）

1. **帳本可信**：`governance/DECISION_LEDGER.json` 存在，且 `verify_ledger.py --strict` 無 fail
2. **腳本可用**：`intent_restate`／`route_expert`／`expert_run`／`run_tests`／`verify_ledger`／`agent_gateway` 都能執行（`--help` 不報缺模組）；腳本不在包內，依賴目標專案安裝的 ledger 版本
3. **版本留痕**：把 ledger 腳本版本／`method_assets` 摘要寫入足跡，後續每次對接先比對；漂移即重新路由，不沿用舊裁決
4. **失敗降級**：任一項失敗即停，向使用者說明「ledger 不可用」，詢問是否降級為非治理任務（維拉 `PASS` 交付）

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
- `target_level` → `definition_of_done`

不要一次把多張卡塞進同一個 worker。

### 3. `test_report` 與 `verify_ledger` JSON

維拉的 PASS 必須同時滿足：

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

### 4. `approval_bundle` 與 `audit`

```bash
python3 scripts/agent_gateway.py --target <P> status --json
# 以下預設 dry-run；只有人與席普可在授權後 --apply
python3 scripts/agent_gateway.py --target <P> request --agent <id> --action <action> \
  --code <CAP.CODE> --expect-fingerprint <FP> --json
```

`approval_bundle` 只列命令，不執行。被 `deny` 時不得換 id、換動作重試；回到 `route_expert` 或請人裁決。

## 角色映射

| ledger 側 | julia-dev 側 | 纪律 |
|-----------|--------------|------|
| `expert-router` | 盧卡＋茱莉亞 | 唯讀路由，不寫 |
| `intent-restate` | 茱莉亞 Phase 0＋瑞克任務契約 | 接受標準要碼化 |
| `project-archaeologist` | 翠西 | 源碼盤點可作為草稿素材，不覆蓋既有治理檔 |
| `greenfield-architect` | 阿奇 | 治理骨架不等於系統架構 |
| `loop-executor` | 麥克／翠西／阿奇 | 一卡一 scope，寫入走網關 |
| `evidence-auditor` | 維拉 | 只讀驗證，不自己修帳本 |
| `ledger-steward` | 人工裁決；艾德只給建議 | 橋接角色不代寫決策或經驗 |
| `release-steward` | 席普 | 解凍／歸檔／退役必須人批准 |
| `goal-orchestrator` | 茱莉亞 Workflow S | 方向鎖、預算與停滯檢查照 ledger |
| OKF／簡報 | 寇娜／黛拉 | 不併入 ledger 核心 |

## 與 julia-dev Workflow 的接合點

| Julia 階段 | 橋接動作 |
|-----------|----------|
| Phase 0 | 人話 → `intent.json`；缺欄位就請瑞克補 |
| Phase 0.5 | 復述門／路由／編排；`blocked` 就停 |
| Workflow S | `next_queue` → 任務圖；保留 `dependsOn` 與 `measurements[]` |
| Phase 4 | 維拉證據 → `evidence_tier`／`binding_status`／`verify_ledger` |
| Phase 7 | `approval_bundle` → 人工批准 → 席普執行 |
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

## 解阻（Andon）

停不是終點。每次 fail-closed 停下，必須向主理人回傳**解阻清單**：阻塞原因、誰能解（人／瑞克補 `open_questions`／盧卡重路由）、所需動作、已嘗試步驟。按情況處理：

| 情況 | 解阻動作 |
|------|---------|
| 復述門非 `allow` | 請瑞克補齊 `open_questions` 後重跑**一次**；仍非 `allow` → Andon 給使用者 |
| `route.blocked` 或 `confidence=low` | 補 `intent.json` 或請人裁決；不得猜測派遣 |
| `verify_ledger` fail | 交維拉修測試或請人裁決；不得軟化結論 |
| `evidence_binding.inputs=0` | 補齊新鮮證據後重算；在此之前只能稱 `declared` |
| `agent_gateway` deny | 停，回到 `route_expert` 或請人裁決；**禁止換 id、換動作重試** |
| 同一阻塞卡兩次 | 主理人向使用者 Andon：事實／選項／建議／需要的決定，四段固定格式 |

## 硬規則

1. 盧卡只讀、只翻譯、只準備；不寫帳本、不開 PR、不合併、不批准。
2. 只交換四類物件：`intent.json`、`route/handoff/next_queue`、`test_report + verify JSON`、`approval_bundle/audit`。
3. 不把完整帳本複製進 julia-dev，只傳當前任務卡、相關決策、相關經驗與證據路徑。
4. 維拉的聊天式 PASS 不等於 ledger 的 `verified`；必須有報告、綁定與不變量通過。
5. 人工確認門禁 > ledger 寫入門禁 > 不可逆動作確認 > 維拉 `PASS` > 其餘可逆工作。
6. 任何 `--apply`、`register`、`unfreeze`、`archive` 都屬批准包，不是橋接角色可自行執行的命令。
7. 所有交接經茱莉亞中轉，團員不互相直連。
8. `intent.json` 是唯一契約入口；茱莉亞的任務契約是它的執行投影。intent 變更後必須重跑復述門與路由，禁止兩邊各自修改。
9. 對接前必須先跑 Preflight；未通過不得呼叫任何橋接命令。
10. 治理專案內維拉的結論必須是 `verified-PASS`（五條件全過）；`PASS` 與 `verified-PASS` 不得混用。
