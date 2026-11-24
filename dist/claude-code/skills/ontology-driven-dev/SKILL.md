---
name: ontology-driven-dev
description: "End-to-end ontology-driven delivery pipeline: requirement exploration with mandatory human confirmation gates, seven-model YAML modeling, and a 10-step build into a runnable browser-based business system. Use for medium-to-large business systems needing strict requirement-to-code alignment. Supports single-stage entry (model only or build only)."
---

# 本體驅動端到端開發

> 方法論來源：`sharptoolbox/ontology-driven-dev`（MIT License，Copyright 2026 sharptoolbox）。本檔為濃縮重述，非原文複製。原始倉庫：https://github.com/sharptoolbox/ontology-driven-dev 。完整授權見 `ATTRIBUTION.md`。
>
> **與 `ontology-modeling` Skill 的分工**：本 Skill 管**端到端管線與工程落地**（需求門禁 → 模型 → 系統）；`ontology-modeling` 管**建模方法論細節**（正交關切、v6/v9 選型、語義邊界鐵律）。兩者配合使用，不要重複載入相同章節。

## 適用情境

- 使用者給一段業務需求，希望產出**可運行的管理系統**
- 要求「需求探索／本體建模／七模型／AI 原生應用／業務系統開發」
- 資料密集、審批流程多、要求需求到程式碼可稽核的企業系統

不適用：小工具、一次性腳本、純前端展示、探索性 AI 應用。

## 五項核心承諾

1. **需求可追溯**：每個功能都能回溯到需求規格說明書的條目
2. **模型是唯一語義來源**：資料表、介面、選單、權限、流程、規則全部由七模型生成，杜絕「模型一套、程式碼一套」
3. **人工門禁不可跳過**：需求探索八階段，每階段都要暫停等人確認
4. **開箱即用底座**：code-paas（Flask + SQLite + React/TS 單體，含系統管理、流程引擎、工作台、本體註冊表）
5. **強制 AI 對話框**：生成的應用右側自帶 AI 對話，且有唯讀 SQL 安全邊界

## 三階段管線（強順序）

### 階段一：需求探索 → 需求規格說明書

按八階段推進，順序不可顛倒：

| 階段 | 主題 |
|------|------|
| 零 | 總體理解確認 |
| 一 | 業務對象 |
| 二 | 業務功能與規則 |
| 三 | 跨對象聯動識別 |
| 四 | 端到端協同流與審批流 |
| 五 | 查詢統計與固定報表 |
| 六 | 角色權限 |
| 七 | UI 原型（可選，須先確認是否需要） |

**人工確認門禁（強制）**：

- 每階段結束、進入下一階段前，必須用固定格式提問：**問題 N + AI 建議 + 建議理由 + 其他選項 + 快捷回覆**
- **硬性暫停**，等使用者明確確認（「按 AI 建議」／選項字母／修改意見）才可推進
- **A 類**（行業通用）：AI 自動補全，標 `[AI自動補全]`
- **B 類**（企業專屬、猜錯有真實業務風險）：必須帶 AI 建議提問，標 `[待確認]`／`[已確認]`
- 附錄中仍有 `[待確認]` 時，文檔**不得**標記為「完整」

**產出**：`<業務域>-需求規格說明書-V9.md`（置於專案根目錄），需含「七模型建模輸入基線」附錄。

> 這是本 Skill 最關鍵的紀律：寧可多問一次，也不要自行假設企業專屬規則。

### 階段二：本體建模 → 七模型 YAML

- **輸入**：階段一文檔的建模輸入基線（確定性輸入，不再做大範圍業務拆分）
- **產出**：`yaml/` 下 M1 物件／M2 行為／M3 規則／M5 主體／M6 流程／M7 查詢報表／MU UI 共 7 個 YAML + `manifest.json`
- **建模順序**：M1 → M5 角色 → M3 → M2 → M7 → M5 權限 → M6 → MU
- **一致性門禁（強制核對）**：
  - M2 `triggerType=USER_ACTION` 的行為須被至少一個 MU 操作功能點引用
  - M7 `behaviorRef` ↔ M2 `queryReportRef` 嚴格一對一
  - M6 的 `roleRef`／`behaviorRef`／`subFlowRef`／`ruleRef` 引用皆須存在，`SUB_FLOW_CALL` 調用圖無環
  - 聯動描述中，「規則條件」與「結論」不得混寫

> 建模的語義邊界、v6/v9 選型、規則下沉判定等細節，見 `ontology-modeling` Skill。

### 階段三：應用構建 → 可運行 BS 系統

**技術底座**：code-paas，原始碼在原始 repo 的 `techbase/`（Python 版）與 `go-techbase/`（Go 版）。本 Skill 不內嵌底座原始碼，使用前從原始 repo 取得並複製到專案的 `code-app/`；底座是**只讀基線**，所有擴充只在 `code-app/` 內進行。

**標準開發流水線 10 步**：

1. 七模型 YAML 放入 `models/` 並登記 `manifest.json`
2. M1 → 資料庫 DDL（聚合根主表／子實體從表，含 5 個預設欄位與編號規則）
3. 資料字典由註冊表自動註冊
4. M2 行為 + M3 規則 → 服務層（事務內：前置校驗 → 規則校驗 → 狀態變更 → `syncTriggers` 聯動；違反規則給中文提示）
5. M5 → 系統管理種子（角色／權限／資源／使用者，介面加權限裝飾器）
6. M6 → 流程引擎（活動與分支轉 `node_graph`；審批角色須設定且綁定使用者）
7. MU → 選單／頁面／路由（單表 2 列、主從 3 列+從表、查詢 3 列+結果分頁；跳框、下拉、審批頁「暫存／提交」雙按鈕）
8. **強制實作右側 AI 對話框**：本體註冊表注入 system prompt、工具註冊（導航／查詢／行為／唯讀 SQL）、SSE 串流、`text/table/chart/action` 渲染協定、動態 SQL 嚴格唯讀白名單 + 稽核
9. 全鏈路聯調：登入 → 錄入 → 暫存/提交 → 多級審批（通過／駁回／退回／撤回）→ 查詢
10. 驗收：對照檢查清單；規則違反有中文提示；介面符合 UI 規範

**輸出**：`code-app/`（可運行系統）。

## 單階段入口

| 使用者意圖 | 從哪開始 |
|-----------|----------|
| 完整開發 | 階段一 → 二 → 三 |
| 已有需求規格，只要模型 | 階段二（僅建模） |
| 已有七模型 YAML，只要系統 | 階段三（僅構建） |
| 需求文件要修訂 | 回到對應階段補確認 |

## 固定輸出約定

| 產物 | 路徑／命名 |
|------|-----------|
| 需求文檔 | `<業務域>-需求規格說明書-V9.md`（專案根） |
| 本體模型 | `yaml/`（7 YAML + manifest.json） |
| 業務系統 | `code-app/` |
| 技術底座來源 | 原始 repo 的 `techbase/`，使用時複製到 `code-app/` |

使用者明確指定其他路徑時以使用者為準。

## 關鍵紀律（不可違反）

1. **人工確認不可替代**：不能因為「看起來很明顯」就跳過提問
2. **模型是唯一語義來源**：禁止模型一套、程式碼一套
3. **底座不動**：擴充只在 `code-app/`，不就地修改 techbase
4. **嚴格對齊規範**：5 個預設欄位、跳框、雙按鈕、AI 唯讀、邏輯刪除、狀態機
5. **AI 對話強制**：階段三必須實作，且要有唯讀安全邊界
6. **事務與聯動邊界**：一個行為只改一個聚合（聚合內主從同事務）；跨聚合靠 `syncTriggers` 或流程編排

## 外部資源（原始 repo）

```bash
git clone https://github.com/sharptoolbox/ontology-driven-dev.git
```

- `references/`：5 份強制規範（需求編寫規範 V9、v9 七模型規範、模型→實現指導書、AI 原生架構設計、UI-UE 規範）
- `reference-example/`：黃金範例（銷售合同執行管理的需求文檔與七模型 YAML）
- `techbase/`／`go-techbase/`：code-paas 乾淨原始碼
- `code-app-example/`：可運行的完整應用樣例

> 本 Skill 只濃縮方法論，不含上述大型原始碼。需要底座時再從原始 repo 取得。

## 來源與授權

- 原始專案：https://github.com/sharptoolbox/ontology-driven-dev
- Copyright (c) 2026 sharptoolbox · MIT License
- 本檔為方法論擷取與重述，非原文複製；完整授權條款見 `ATTRIBUTION.md`
