# Agent 友善 CLI 設計與review（濃縮版）

> 來源：`cursor/plugins` 的 `cli-for-agent`（MIT，Copyright 2026 Eric Zakariasson）。本檔為方法論濃縮重述，非原文複製。見同目錄 `ATTRIBUTION.md`。

## 何時用

麥克（工程師）在設計或重構 CLI、阿奇在review CLI 契約時載入。也適用於 Workflow C／D／J／K 中需要提供給 agent 呼叫的批次工具。

## 設計清單

1. **非互動優先**：所有必要輸入都有 flag 或環境變數；沒有 hidden prompt。TTY 以外不得等待輸入，不得只靠互動精靈完成流程
2. **分层 `--help`**：頂層 help 列出子指令與一個真實範例；子指令 help 列出必填／選填參數、預設值、輸出格式、退出碼，並附最少一個可貼上執行的例子
3. **stdin 與 pipeline**：接受 stdin 作為輸入來源，能與 pipes、redirection、其他工具串接；不要在 pipe 模式印進度動畫
4. **錯誤快且可行動**：錯誤訊息寫清楚「哪個輸入、為什麼錯、怎麼改、可執行的修正指令」；不要只印 stack trace 或 `Error: failed`
5. **冪等**：同一指令重跑一次不會產生重複副作用；會改狀態的指令要能被安全重試
6. **`--dry-run`**：會寫入、刪除、部署、傳送的指令必須能 preflight，列出將發生的動作而不執行，並說明跳過了什麼
7. **可預測的指令結構**：動詞／名詞一致；相同概念在不同子指令用同一個 flag 名稱與型別
8. **結構化輸出**：提供 `--json`（或等同）穩定 schema，方便 agent 解析；human output 與 machine output 分開，不要在 JSON 裡混進裝飾文字
9. **明確退出碼**：成功、輸入錯誤、驗證失敗、遠端失敗、部分完成各有不同 code，並寫進 help
10. **安全邊界**：secrets 不放 command-line 參數（會進 shell history／process list）；要有 timeout 與重試政策，不靠無限等待

## Review 輸出

review 既有 CLI 時，按 `Blocker / Warning / Nit` 分級，每項給 `file:line` 或指令輸出佐證，最後補一段最小可用範例：

```text
tool --json --dry-run <args>   # preflight
tool --json <args>             # execute
```

## 硬規則

- 不為了向後相容而保留「只能互動」的路徑；若必須保留，明確標為 deprecated 且不能是 agent 的唯一入口
- 不把錯誤改成 silent success；部分完成要如實回報
- 不虛構 flag 或輸出格式；以實際 help 與原始碼為準
