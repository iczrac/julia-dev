---
name: ontology-modeling
description: "Ontology-driven modeling for medium-to-large business systems. Decompose a domain into orthogonal model files with hard semantic boundaries and requirement-to-code traceability. Use when architecting enterprise business systems, CRUD-heavy domains, or systems needing auditable tracing. Skip for small tools, pure frontend work, or throwaway scripts."
---

# 本體驅動建模

> 方法論來源：`sharptoolbox/ontology_modeling_framework`（作者 @人月聊IT，Apache License 2.0）。本檔為該方法論的濃縮重述，非原文複製。原始規範：https://github.com/sharptoolbox/ontology_modeling_framework 。完整署名見同目錄 `ATTRIBUTION.md`。
>
> **與 `ontology-driven-dev` Skill 的分工**：本 Skill 管建模方法論細節；若要「需求探索 → 建模 → 可運行系統」的完整交付管線，見 `ontology-driven-dev` Skill。

## 一句話

用「本體」當核心隱喻，把業務世界切成**互不重疊、可獨立演進、可用 YAML 承載**的建模關切，建立「需求 → 設計 → 程式碼」的可追蹤鏈。

## 何時用／何時不用

| 用 | 不用 |
|----|------|
| 有明確領域邊界的中大型業務系統 | 小工具、一次性腳本、Prototype |
| CRUD 密集、規則多、流程與審批複雜 | 純前端展示、行銷頁 |
| 需要稽核「這段程式碼對應哪條需求」 | 探索性 AI 應用、資料管線 |
| 多角色協作、需要穩定交接契約 | 需求尚未成形的早期腦暴 |

## 五條核心原則

1. **語義驅動**：模型元素帶業務語義，不是技術描述
2. **正交分解**：一個關切只由一個模型承擔，互不重疊
3. **解耦優先**：跨物件聯動要顯式宣告，禁止源物件直接寫入另一聚合
4. **職責硬邊界**：行為只回答「做什麼、改什麼狀態」；規則只回答「條件是否成立」；流程才管順序
5. **可追溯**：每個實作單元都要能溯源到具體模型定義，且有門禁檢查孤兒元素

## 正交建模關切（v6 全量 11 模型）

| 關切 | 模型 | 回答的問題 |
|------|------|-----------|
| 存在 | M1 物件 | 有哪些業務物件、邊界與不變性為何 |
| 行為 | M2 行為 | 每個物件能做什麼、改變什麼狀態 |
| 規則 | M3 規則 | 什麼條件成立、能否執行（只判斷、不改狀態） |
| 事件 | ME 事件 | 已發生的事實是什麼、誰訂閱 |
| 協同 | M4 場景 | 一件事如何引發跨物件協同 |
| 誰 | M5 主體 | 誰能做什麼（角色與權限） |
| 流程 | M6 流程 | 業務怎麼從頭走到尾、誰審批 |
| 讀取 | M7 查詢報表 | 跨物件查詢、統計與報表 |
| 入口 | MU UI | 使用者在哪裡操作、點了什麼 |
| 落地 | MM 映射 | 物件落在哪張表哪個欄位 |
| 邊界 | MI 介面 | 系統兩側如何通訊 |

> ⚠️ M6 / M7 在不同版本語義不同：v1/v2 的 M6 是異常補償、M7 是品質約束；v4 起改為流程與查詢報表。引用舊文件時先確認版本。

## 版本選型

| 情境 | 版本 | 理由 |
|------|------|------|
| 中小型單體、同步流程、要讓 AI 穩定出碼 | **v9（7 模型）** | 移除事件與外部整合複雜度，語義邊界硬、生成歧義低 |
| 微服務、事件驅動、完整介面與持久化映射 | **v6（11 模型）** | 唯一含 ME / M4 / MM / MI 的完整版本 |

**實務建議**：用 v6 理解全貌，用 v9 落地執行。

### v9 的 7 個模型

M1 物件 · M2 行為（含 `syncTriggers` 同步聯動） · M3 規則 · M5 主體 · M6 流程 · M7 查詢報表 · MU UI

### v9 的關鍵裁剪

- 無事件模型，跨物件聯動改用 `syncTriggers`（源行為成功後同步呼叫下游行為）
- 規則一律被同步呼叫，回歸「只判斷、不驅動」
- 物件到資料表的映射交給 ORM／DDL，不在本體層建模

## 建模順序（不可隨意顛倒）

**v9 八階段（主用）**：

1. M1 物件 → 2. M5 角色 → 3. M3 規則 → 4. M2 行為（含聯動） → 5. M7 查詢報表 → 6. M5 權限 → 7. M6 流程 → 8. MU UI（反向校驗可追溯性）

**v6 十二階段（全量）**：

M1 → M5(角色) → M3 → M2 → M7 → ME → M5(權限) → M4 → M6 → MU → MM → MI

> M5 分兩次：先定角色與職責，待行為穩定後再綁權限。

## 語義邊界鐵律

1. **規則下沉判定**（逐級問，第一個「是」就停）：

   內建欄位能表達？ → 是：用欄位約束
   → 否：只依賴當前屬性？ → 是：用 `refRules`
   → 否：只依賴同一聚合？ → 是：用 `invariants`
   → 否：才進 M3 規則模型

2. **跨物件聯動**：
   - v9：`syncTriggers` 顯式宣告，下游必須作用於**另一個獨立聚合**
   - v6：事件必須是**已完成的事實**（「合同新增一筆收款」，不是「合同滿足關閉條件」）
   - 禁止源物件行為直接跨聚合寫入目標物件
   - 聯動失敗語義必須寫進後置條件或流程，禁止隱含吞掉例外

3. **流程 vs 規則 vs 行為**：順序與審批歸 M6；條件判斷歸 M3；狀態改變歸 M2。不要混在一起寫。

## 追溯門禁（交付前必查）

- `triggerType=USER_ACTION` 的行為，**必須**被至少一個 MU 操作功能點引用，否則是孤兒行為
- MU 的 `callChain` 是唯一按序描述「一次操作 → 系統處理」的載體，標準順序：
  `VALIDATE`(M3) → `BEHAVIOR_CALL`(M2) → 聯動／事件 → 協同 → `QUERY_REPORT` → `NAVIGATE`
- `VALIDATE` 必須在 `BEHAVIOR_CALL` 之前
- 每個 M2 查詢行為要有對應的 M7 定義（一對一）
- 任何跨模型破壞性變更要記 `CHANGELOG.md`

## 交付物與目錄約定

- v9：`yaml/` 下 7 個固定檔名（`m1-object-model.yaml`、`m2-behavior-model.yaml`、`m3-rule-model.yaml`、`m5-actor-model.yaml`、`m6-flow-model.yaml`、`m7-report-model.yaml`、`mu-ui-model.yaml`）
- v6：`onto-cs/model/{projectId}/yaml/` 下 11 個
- 每個元文件自帶 `version` 欄位；`manifest.json` 可選，且不得存絕對路徑
- 框架只描述「系統做什麼、為何這樣運轉、使用者如何驅動」；**不覆蓋** NFR、部署拓撲、BI 指標、遷移腳本、驗收測試用例——這些由團隊其他角色與配套規格補齊

## 與本團隊 Workflow 的接合

- 在 Workflow A／D／I 的 Phase 2，阿奇可選用本 Skill 產出模型元文件，取代單純的 Mermaid 設計圖
- 瑞克在 Phase 1 提供的驗收標準，需標出對應的 MU 操作功能點
- 麥克在 Phase 3 依模型映射實作：M1→資料模型、M2→服務方法、M3→規則／校驗、M6→流程編排、MU→UI 元件
- 維拉在 Phase 4 執行追溯門禁檢查，判定是否有孤兒行為與中斷的 callChain

## 來源與授權

- 原始框架：https://github.com/sharptoolbox/ontology_modeling_framework
- 作者：@人月聊IT · Copyright 2026 sharptoolbox
- 授權：Apache License 2.0
- 本檔為濃縮重述與方法論擷取，非原文複製；完整署名與 NOTICE 見 `ATTRIBUTION.md`
