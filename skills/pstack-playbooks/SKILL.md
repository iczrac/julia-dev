# pstack 嚴謹工程 Playbook（濃縮版）

> 來源：`cursor/plugins` 的 `pstack`（作者 Lauren Tan，MIT）。本檔為方法論的濃縮重述，非原文複製。原始專案：https://github.com/cursor/plugins/tree/main/pstack 。完整授權見同目錄 `ATTRIBUTION.md`。

## 何時用

主理人在 Phase 0 完成任務辨析後，若任務需要「嚴謹工程處理」（特別是除錯、效能、重構、上線長時間任務），載入本 Skill 選擇一個 playbook，並**把其步驟逐條抄進任務清單**再開始。不要一邊做一邊 improvisation。

## 自治與門禁優先序（本團隊改寫）

pstack 原版傾向「可逆工作直接做、不要問人」。本團隊的優先序如下，衝突時從上到下：

1. Workflow L 的八階段人工確認門禁（瑞克逐階段硬暫停）
2. 維拉的 `PASS`／`FAIL` 結論（不得代寫或軟化）
3. 不可逆動作（force push、部署、資料刪除、對外訊息）必須暫停取得確認
4. 其餘可逆工作：直接推進、完成後報告；能用實驗決定的分歧就做原型，不要回頭問人

## 22 個 Playbook 路由表

| Playbook | 適用情境 |
|----------|----------|
| investigation | 只讀問題：X 怎麼運作、為什麼這樣做、我們確定嗎 |
| bug fix | 重現缺陷、找根因、以執行期證據修復 |
| perf | 追蹤量測到的變慢，對照基線改善 |
| hillclimb | 針對單一指標科學式持續改善，每個被接受的改善 一個 commit |
| runtime forensics | 從 instrumentation 診斷活體症狀（洩漏、空轉、抖動） |
| trace forensics | 診斷已擷取的 profiling 產物（cpuprofile、trace、heap snapshot） |
| feature | 從命名的資料形狀出發建置新行為 |
| refactoring | 不改變行為的結構調整 |
| prototype | 用一次性草圖便宜地決定設計或行為分歧 |
| visual parity | 兩個實作的像素級 UI 等價 |
| authoring a skill | 撰寫或修改 SKILL.md |
| eval | 盲測 Skill／提示變更對 agent 行為的影響 |
| babysit | 把 PR 或 stack 推到可合併：衝突、review 執行緒、CI |
| shipping | 獨立驗證 green stack，再由底層往上落地 |
| autonomous run | 不停下來完成長任務 |
| autopilot-full | 獨立 PR 各自跑到合併，每個 PR 一位 owner |
| autopilot-stack | 同上但不合併，堆疊 PR 供操作者審核 |
| session pickup | 接手先前 agent 未完成的工作 |
| pause safely | 乾淨暫停在途工作，供之後恢復 |
| multi-phase plan | 跨階段或堆疊 PR 的工作 |
| worktree cleanup | 清理已合併／廢棄 worktree，安全門禁 |
| opening a pr | 從小且有順序的 commit 開 PR（其他 playbook 結束時呼叫） |

## 五個關鍵流程（濃縮）

### Bug fix — 每行程式都要追溯到執行期證據

1. **自己重現**：在對應介面重現；只有當控制介面確實到不了目標、且已盡力驅動後，才帶具體理由問使用者。重現不了就合成觸發條件、收緊條件或加 instrumentation 直到它發生。
2. **二分法找因**：列出候選假設，取能切掉最多剩餘空間的那一刀，用執行期證據淘汰；狀態不明就加 log 並讀實際輸出。不要猜。「可能有用」的防護是假設，不是修復；證據反駁就回退。
3. **規劃修復**：跨函式邊界先走 architect（阿奇）；委派實作時給明確範圍。
4. **同一介面驗證**：原始重現必須通過；「inconclusive」或驗證在錯誤介面不算通過。
5. **提交排序**：讓失敗的重現先進 git history，修復在其上（有便宜本地測試路徑時先寫失敗測試）。
6. 開 PR；回報原文貼上「失敗→通過」的輸出。

### Perf — 先有基線才談改善

量測慢在哪裡 → 命名限制因子 → 對照基線改善 → 用同一方法重測 → 依 `pstack-verification` 的基準檢驗清單核對數字。數字未通過檢驗前不得宣稱加速。

### Feature — 先命名資料形狀

追蹤受影響子系統 → 阿奇定形狀 → 寫下吞吐量檢查點（阻塞前置步骤／可平行工作流／共享可變狀態／最小安全切分，不適用要寫 `n/a: 原因` 不可刪項）→ 委派實作時指定檔案路徑、資料形狀與其組織結構、成功條件 → 同一介面驗證 → 拆成小的有序 commit → 設計有爭議時先 interrogate → 開 PR。

### Session pickup — 讀足跡，不要重做

1. 定位先前足跡（工作區內的 transcript、分支、紀錄），先讀摘要與最後訊息，再回頭找決策點；長紀錄交 subagent 濃縮，主執行緒只留時間軸。
2. 重建操作狀態：分支、worktree、已落地什麼、未完成 todo、已做決策。先前足跡是權威輸入，不要重新推導。
3. 比對「已完成 vs 待辦」，指名恢復點；不要重跑已經做過的重現。
4. 把剩餘工作路由到對應 playbook，本 playbook 到此結束。
5. 對真實產物驗證繼承而來的宣稱——先前 agent 的自我回報不是證據。

### Shipping — 你負責「什麼被落地」

1. **獨立驗證每個 PR**：一位沒有寫該程式碼的驗證者，以使用者方式跑過變更，在 PR 上給 `PASS`／`PASS+NOTES`／`FAIL`。綠燈 CI 與機器人核准都不是裁決。
2. **只落地從底部起連續通過的區段**：從最低未合併 PR 往上走，遇到第一個沒有 PASS 的就停；上方通過的 PR 要等。
3. **重查裁決是否仍描述現在的程式**：rebase 換 SHA 後用 `git patch-id` 比對；只有測試／文件／lint 設定差異可視為雜訊，且要列出檔案。
4. **由底層往上一次合一個**，合併後再讀回狀態確認真的合了（merge 指令成功不代表已合併，也可能是進了 queue 或 auto-merge）。
5. **落地期間別亂動分支**，停在上限；要延伸區段就重新做一輪驗證。

## 與本團隊 Workflow 的對應

- bug fix → Workflow E；perf／refactoring → Workflow F；investigation → Workflow C
- shipping／babysit／session pickup → Workflow R（由席普主導）
- arena／interrogate 的並行操作見 `pstack-parallel-review`
- 驗證細節見 `pstack-verification`；取捨標準見 `pstack-principles`
