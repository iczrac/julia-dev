# codebase-reverse — 存量源碼逆向

> 方法論來源：`sharptoolbox/codebase-reverse`（MIT）。本檔為濃縮重述，非原文複製。原始規範：https://github.com/sharptoolbox/codebase-reverse 。完整署名見同目錄 `ATTRIBUTION.md`。

## 何時使用

需要理解**既有系統**卻缺乏可信文件或原始設計者时：接手舊專案、遷移前置盤點、重构前現況基線、影響分析、尋找隱藏入口（定時任務／事件監聽／API-only／批次）、補寫需求規格。

不適用：全新開發（走 Workflow A）、只要跑測試（走 Workflow C）。

## 核心方法

### 兩條鐵律
1. **全量基線，深度分層**：覆蓋完整度與細節深度是兩個維度。基線必須列盡範圍內全部源碼資產；只有細節可分層。
2. **從源碼反查遺漏**：不是「讀了什麼就寫什麼」，而是先建立源碼資產台帳，再反查每項是否已被文件覆蓋。有未歸屬的入口／介面／任務／DAO／表即不得標記完成。

### B0–B9 全量基線順序
| 階段 | 產出 |
|------|------|
| B0 範圍界定 | 語言選擇（zh/en）、包含與排除目錄及理由 |
| B1 源碼資產台帳 | 全部檔案、入口、元件歸屬 |
| B2 技術架構 | 框架、分層、技術元件與實際能力介面 |
| B3 業務功能與需求面板 | 每個 `FUNC-*` 的獨立業務結果、狀態變化、權限 |
| B4 介面與對象 | 逐端點／逐事件／逐任務、對象全量分類 |
| B5 資料庫設計 | 逐物理表、視圖、欄位；DDL 缺失時標 `unknown`，不得偽造 |
| B6 功能穿透鏈 | 入口 → 需求語義 → Controller/Job/Listener → Service → DAO → 子呼叫 → 公共能力 → 物理表 R/C/U/D |
| B7 公共能力 | 認證、權限、流程、通知、消息、檔案、字典、審計、排程及其消費者 |
| B8 覆蓋對帳 | source-coverage-report：台帳 vs 文件逐項核對 |
| B9 獨立校驗 | consistency-report：語義與關係一致性，`PASS` + `ERROR=0` |

### 單功能深挖（可選）
- `F-FULL`：業務＋技術實作全集。每個頁面、子頁、Tab、嚮導步驟、彈窗、抽屜都要 ASCII 版面圖；每個控制項／事件要有独立縱向穿透卡片，不得按技術層拆散。
- `F-REQ`：技術實作無關的需求規格。只輸出業務介面、功能、規則、狀態、驗收與資料庫物件模型；**不得混入**類別／方法／框架／分層。

### 關鍵判準
- 沒有菜單不等於沒有功能：JOB／EVENT／API／ENTRY 都要當鏈路起點，並說明誰發現失敗、誰能干預。
- `CAP-*` 只是能力分組，不能代替具體 `FUNC-*`；兩者一一對應需求面板與穿透鏈。
- 每條關鍵關係記錄源碼路徑、符號與證據等級（事實／推斷／假設）。

## 交付清單

`source-asset-inventory.md`、`business-function-requirements.md`、`function-chain-index.md`、`database-inventory.md`、`database-schema.md`、`database-relations.md`、`database-access-matrix.md`、`source-coverage-report.md`、`consistency-report.md`、`function-drilldowns/FUNC-xxx.md` 或 `function-requirements/FUNC-xxx.md`。

## 與團隊協作

由**逆向工程師**（reverse-engineer）主導；Vera（qa-engineer）負責 B8/B9 的獨立覆蓋對帳與一致性校驗，Archie（architect）基於逆向基線做影響分析。主理人不得代寫逆向結論。
