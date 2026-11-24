# 結構化編排與有界循環（濃縮版）

> 來源：`cursor/plugins` 的 `orchestrate`、`ralph-loop`、`cursor-team-kit/loop-on-ci`（皆為 MIT，Copyright 2026 Cursor）。本檔為方法論濃縮重述，非原文複製；Cursor SDK、Bun 腳本與 Slack 整合不內嵌。原始專案見同目錄 `ATTRIBUTION.md`。

## 何時用

由Julia（主理人）在**大型／可拆分／需要平行或反覆推進**的任務使用；Ship在 CI 照護時使用其中的 CI 迴圈。這是對既有 SOP 的**協作層升級**：`pstack` 管「每行程式碼的證據」，本 Skill 管「任務圖、交接格式、循環何時停」。

**不適用**：單檔小修改、純問答、需求尚未辨析（先走 Phase 0）、需要人類判斷的模糊目標。

## 一、三種節點與責任邊界

| 節點 | 誰擔任 | 擁有什麼 | 不做什麼 |
|------|--------|----------|----------|
| Planner | Julia（或子規劃者） | 整體目標、任務圖、讀交接、決定下一步 | 不寫程式、不合併、不亲自修衝突；想改程式就發一個新任務 |
| Worker | Mark／Tracey／Archie等專業成員 | 單一限定範圍、一份交接 | 不與其他 worker 通信、不改別人路徑、不自己結案整體目標 |
| Verifier | Vera／Ship | 單一目標的驗收標準、判決交接 | 不改目標原始碼、不開 PR、不合併；只跑證據、給裁決 |

**共同介質是 git／檔案系統**，不是聊天紀錄或通知工具。通知工具只是「可見性」，不是任務狀態。所有跨成員資訊仍由主理人中轉，符合團隊鐵律。

## 二、任務圖與狀態

規劃時先寫下等效於 `plan.json` 的任務表：

- `goal`：使用者原話，逐字保留
- `summary`：給人看的一句話
- `tasks[]`：每項含 `name`、`type`（worker／verifier）、`scopedGoal`、`pathsAllowed`、`acceptance`、`verify`、`dependsOn`、`measurements[]`
- 狀態表記載：status、分支、agent/run id、verification、attention 事件
- 交接檔逐字保存成員回傳，**不要美化或改寫**；規劃者需要原始措辭

規劃規則：

- 合併也是任務：在 `scopedGoal` 寫明合併哪些分支、衝突時的取捨、合併後跑什麼驗證
- 偏好較少但較大的 worker；只有當切片真正獨立或有衝突風險才拆分
- 預設每個 worker 配一個 verifier；`dependsOn` 不只是排序，也代表 upstream 交接必須轉交給 downstream
- 量化主張放 `measurements[]`；worker 回傳後重跑指令，偏差 >10% 或單位不一致要標記
- fan-in 太大時先發一個「彙總 worker」，不要把一堆交接塞進同一個提示詞

## 三、Worker 交接格式

成員完成後，回傳固定結構（中英對照皆可，但欄位不可省）：

```text
## Status
success | partial | blocked

## Branch
<actual branch name> 或 (no branch)

## What I did
- 逐檔或逐切片摘要

## Measurements
- <metric>: <before> <op> <after>
- 沒有量化驗收就寫 (none)

## Verification
live-ui-verified | unit-test-verified | type-check-only | not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- 假設、驚訝、取捨、破壞的 invariant、需求不清之處

## Suggested follow-ups
- 給規劃者的候選任務
```

`Notes` 是最有價值的欄位：worker 對任務範圍的抱怨，往往代表任務提示詞有問題。

## 四、Verifier 證據分級

Verifier 的交接到固定包含：

```text
## Verification
<live-ui-verified | unit-test-verified | type-check-only | verifier-blocked | verifier-failed>

## Target
<task> on branch <branch>

## Execution
- <command> → <outcome>
- <test suite> → <pass/fail counts>
- <manual repro step> → <observed behavior>

## Findings
- [x] <criterion>: <evidence> (met | not met | n/a)
- (high|med|low) <finding>: <evidence>

## Notes & suggestions
- flaky tests、鄰近問題、後續任務
```

分級紀律：

- **讀 diff 不等於驗證**。要跑程式、打 API、點 UI、執行指令並貼出輸出
- `verifier-blocked`：環境故障（Docker、port、憑證、harness）導致跑不了。修法可能是對的，但未證明，**不得算通過**
- `type-check-only`：只有型別／建置通過；除非變更只涉及型別，否則要補更強的驗證
- `verifier-failed`：跑了但fix無效 → 發修復任務，不是自動重跑同一個 verifier
- worker 的自評可被 verifier 覆寫；覆寫時以 verifier 為準

## 五、有界 Ralph 循環

適用於「驗收標準可機械判定」的任務：讓測試全綠、完成遷移、依規格補齐功能。

1. 把任務寫成**不會變的提示詞**，並明確列出完成條件（例如「CRUD 端點可用、輸入驗證完成、測試通過且覆蓋率 >80%，完成時輸出 COMPLETE」）
2. 設定 `completion_promise`（完成短語）與 `max_iterations`（上限）
3. 每一輪都看到自己上一輪留下的工作樹與 git 紀錄，再迭代；**提示詞不變，程式碼變**
4. 只有當承諾真的完全成立才能輸出承諾；禁止為了逃離迴圈說謊
5. 到了上限就停，明確回報「未完成＋已完成什麼＋卡在哪」，不得標記完成

大任務先拆階段，並在提示詞內建「測試 → 修正」迴圈；模糊目標與需要人為品味判斷的任務不要用。

## 六、失敗處理與 Andon

失敗交接要寫：`failureMode`、`branch`、`agentId/runId`、`terminatedAt`、`last activity`、`last tool call`、SDK error。

| Failure mode | 處理 |
|--------------|------|
| cap-hit / oom | 縮小範圍重試：更窄的路徑、更短的 scopedGoal |
| network-drop | 原樣重試，視為暫時性 |
| tool-error | 換模型或換工具重試 |
| unknown | 原樣重試一次；再失敗就放棄並 replan |

同一任務重試兩次後，優先「從任務圖移除，繞道重規畫」，而不是第三次硬試。上游失敗時下游維持 pending，不要讓它帶著猜测繼續。

**Andon（全樹暫停）**：只有當繼續產生交接只會製造垃圾時才觸發——上游輸出錯誤、驗收條件壞掉、auth／infra 不可恢復。單一任務卡住寫在它的交接裡即可，不必拉下全樹。

## 七、CI 迴圈

- 以 `gh pr checks` 為準（它包含所有 PR 附加檢查；`gh run list` 只看 GitHub Actions）
- 先看現有失敗；pending 用 `gh pr checks --watch --fail-fast`
- 每次 push 後重查完整檢查集合，檢查集合會變
- 一次修正只處理一個失敗原因；Flaky 重試一次並留下證據
- 禁止用 `--no-verify` 強行推進；失敗明顯與本 PR 無關且 main 已修好時，合併最新 main，不要在 PR 裡塞無關修正

## 硬規則

1. Planner 不寫程式；Worker 不與兄弟通信；Verifier 不改目標原始碼
2. 所有交接逐字保存，不美化；下游需要上游資訊就明確宣告依賴
3. 沒有Execution證據的 verification 一律降級或 blocked
4. 循環一定要有完成承諾與上限；到上限如實回報未完成
5. Andon 是稀有動作，不是單一失敗的替代品
6. 本 Skill 不取代Vera的 `PASS` 門禁、人工確認門禁或Ship的 patch-id 核對
