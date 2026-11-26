---
name: self-evolution
description: "Controlled self-evolution loop: members propose capability-doc amendments with evidence and repeat-failure gate, Ed reviews read-only, the human approves as the only effect gate, the lead executes edits with one green `bash scripts/check.sh` → `git commit` → patch version bump (no validate/register commands)."
---

# 受控自我進化

團隊能力文件（Agent MD／Skill）的進化回路。核心立場：**成員是每次會話臨時 spawn 的執行者，沒有跨會話記憶；能進化的載體只有專家包文件本身**。因此進化 = 文件演化，用「提案 → 複核 → 人拍板 → 執行 → 版本」五道閘替代自由自我修改，讓改進可追溯、可回滾、不漂移。

## 觸發條件（提案資格門）

滿足其一才允許提案，不滿足就繼續執行現行規則：

1. **重複門**：同一教訓在同一成員身上重複出現 ≥2 次（對齊「卡兩次」紀律）
2. **外部輸入**：使用者要求吸收新方法論或修正流程
3. **主動邀請**：使用者明確要求成員反思並提案
4. **體檢裁決**：Workflow V 內部體檢中 Ed 裁定為「必修」的發現（裁決替代重複門；「緩議」項不具備資格，累計重複後走重複門）

## 提案格式（固定七段）

成員在回傳產出末尾附加，**不得自行修改任何檔案**：

```
## EVOLUTION PROPOSAL
- 觀察：一句話描述重複出現的問題或機會
- 證據指針：footprint 路徑／測試報告／對話紀錄（可驗證，不接受「我覺得」）
- 目標：擬修改的檔案與段落（精確到小節）
- 修改內容：修改前 → 修改後的文字
- 回滾方式：對應的還原操作（git revert 範圍）
- 影響評估：影響哪些 Workflow／Skill／成員，是否觸碰禁區；**是否觸碰 ledger 契約**（改動 PASS 語義／證據格式／寫入邊界的提案必須註明受影響的能力碼與不變量，Ed複核時加查此項）
- 建議版本：patch 版本號建議
```

## 回路（六步，只有第 3 步能生效）

1. **成員提案**：按七段格式附加在產出末尾；不改文件
2. **Ed 複核**：唯讀判決——建議採納／拒絕／需修改＋理由；判決不等於批准
3. **人拍板**：使用者批准／拒絕／要求修改。**這是唯一生效門，任何其他角色都不能代替**
4. **Julia 執行**：只有主理人修改檔案；修改採「合併替換」不堆疊追加；批准前不動任何文件
5. **驗證生效**：`bash scripts/check.sh` 全綠（含 ledger `spec_check` 與本倉 Knox／角色可執行性測試）→ `git commit`（一次生效 = 一個 commit，即回滾點）→ patch 版本 +1。不存在 `validate_expert` / `register_expert` 命令，不得以裸名冒充可執行步骤
   - **提交原子口徑（沿用 ledger `RELEASE_CHECKLIST.md`）**：commit 邊界 = `bash scripts/check.sh` 全綠的狀態；權威源與派生物（`dist/`、`src/contracts/`、`governance/test_report.json`、`governance/index.html`）必須同一 commit，不按主題拆、按派生一致性拆；中間 commit 各自全綠，否則合為單一一致 commit。「一個 commit 一個決策」不可機器判定，不做硬要求。
   - **發版邏輯原子**：版本錨 + tag；`python3 ../ledger-driven-dev/scripts/spec_check.py --target .` 的 `compat`／`release_tag` 判據已 fail-closed。跨倉物理原子在 Git 不存在，明確放棄；`compat` 讀兄弟倉工作樹 `METHOD_VERSION`（非 tag），tag 提交順序仍是人工紀律，不得宣稱已機器強制。注意：此跨倉命令的路徑前綴（`../` 開頭）**不在 `executable_claims` 掃描前綴**（`scripts/`、`governance/`、`tests/`）內，零命中代表「沒被掃到」而非「已驗證」；其真實存在性由 `bash scripts/check.sh` 的 `stage_spec` 實際執行時保證，不得把 claims 零命中當作這條命令的背書。
6. **日誌登記**：在 `docs/evolution-log.md` 記錄提案摘要、裁決、批准理由一句話

## 禁區（成員不可提案，只能由人主動修改）

- 嚴禁行為清單
- 門禁優先序（門禁優先序：人工確認 > ledger 寫入（僅 ledger 語境，是人工確認的具體化）> 不可逆動作確認 > Vera 證據支持 PASS／FAIL（test_report＋綁定＋不變量通過，非聊天式 PASS）> 其餘可逆工作；Vera PASS 永不取代人工確認，非 ledger 語境略去第二項）
- 成員職責邊界與協作鐵律
- 四類 ledger 交接對象

## 硬紀律

- 成員不得修改自己的 MD 或任何 Skill；進化只能以提案形式存在
- Ed 的複核判決不得代替人的批准
- 提案未過驗證不得註冊生效；驗證通過不等於自動合入
- 規則修改必須合併替換，禁止無限堆疊——SOP 膨脹比 SOP 過時更危險
- 禁區外的提案也必須走完整回路，沒有「小改免審」

## 與其他三層的邊界

| 層 | 載體 | 管什麼 |
|----|------|--------|
| 進化日誌 | `docs/evolution-log.md`（本包） | 專家包能力文件自身的變更史 |
| ledger history／lessons | 目標治理專案 | 項目事實與決策，不回流改 SOP |
| OKF | 知識 bundle | 長期可信知識，AI 改寫已人工審核概念後審核失效 |
| footprint | 目標專案 | 當前工作現場草稿 |

四層互不複製；進化提案引用其他層作為證據，但不把內容搬進專家包。
