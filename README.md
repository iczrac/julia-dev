# 茱莉亞開發團隊 (Julia Dev Team)

由茱莉亞統籌的全方位軟體開發專家團。不論是源碼逆向、從零建置、加功能、修 bug、重構、審查、遷移、串接第三方、數據／AI 應用或交付簡報，都會先辨析任務類型，再調度最合適的團隊流程交付。

## 類型

Team 型（多角色協作團隊）· 版本 1.5.0 · 8 位成員

## 成員與命名巧思

| 成員 ID | 名字 | 職業 | 巧思 |
|---------|------|------|------|
| julia-dev-team-lead | 茱莉亞 Julia | 交付總監 | 諧音「主理呀」——主理人 |
| product-manager | 瑞克 Rick | 產品經理 | req（requirement）需求 |
| architect | 阿奇 Archie | 架構師 | arch（architecture）架構 |
| engineer | 麥克 Mike | 工程師 | make——動手造東西的人 |
| qa-engineer | 維拉 Vera | 品質保證工程師 | verify——驗證的化身 |
| reverse-engineer | 翠西 Tracey | 逆向工程師 | trace——追溯源碼，從入口追到資料庫 |
| delivery-designer | 黛拉 Della | 交付設計師 | deck／deliver——做出可放映的交付簡報 |
| knowledge-curator | 寇娜 Kona | 知識管理師 | know——知識的守護者，管溯源、信任與時效 |

## 任務類型與流程對照

主理人茱莉亞會先做 **Phase 0 任務辨析**，再從 15 條 Workflow 中選一條；不需要的階段直接略過，不浪費流程。

| 你說的話 | 任務類型 | 啟動流程 |
|---------|----------|----------|
| 做一個工具／網站／API | 全新開發 | A 完整交付 |
| 需求很亂，幫我寫 PRD | 需求梳理 | B 需求梳理 |
| 幫我 review 程式碼 | 審查健檢 | C 健檢／G 安全審查 |
| 在現有系統加一個功能 | 功能增強 | D 功能增強 |
| 這裡報錯／結果不對 | 缺陷修復 | E 缺陷修復 |
| 太慢了／幫我重構 | 重構優化 | F 重構優化 |
| 補測試／提高覆蓋率 | 測試補齊 | H 測試補齊 |
| 升級版本／換框架 | 遷移升級 | I 遷移升級 |
| 串接支付／登入／地圖 API | 第三方整合 | J 第三方整合 |
| 爬蟲／RAG／LLM 應用 | 數據 AI | K 數據／AI 應用 |
| 用本體驅動做 XX 管理系統 | 本體驅動 | L 本體驅動端到端 |
| 接手舊專案／盤點程式碼 | 源碼逆向 | M 源碼逆向 |
| 做成簡報／方案彙報 | 交付敘事 | N 交付敘事簡報 |
| 畫架構圖／知識圖譜 | 可視化建模 | O 多視角建模 |
| 建立知識庫／這個數字可信嗎 | OKF 知識管理 | P OKF 知識管理 |
| 用什麼技術比較好 | 技術咨詢 | B 或直接問阿奇 |

## 適用專案型態

Web 前端、後端 API、全端應用、CLI／自動化腳本、桌面應用、行動應用、資料處理、AI／LLM 應用、資料庫設計、DevOps／部署。

每種型態都有對應的設計與驗證重點，會由主理人在派工時明確寫給團員，例如 API 重契約與錯誤碼、AI 應用重幻覺防護與成本、CLI 重冪等性與輸出格式。

## 選配方法論：本體驅動建模

Expert 包內建 `skills/ontology-modeling/`，吸收自開源框架 [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework)（作者 @人月聊IT，Apache-2.0）。它把業務系統切成**正交、可獨立演進、可用 YAML 承載**的模型關切，建立「需求 → 設計 → 程式碼」的可追蹤鏈。

**何時啟用**（由阿奇在 Phase 2 載入）：

- 中大型業務系統（ERP／CRM／審批／合同管理）
- 規則密集、跨物件聯動多、需要稽核溯源
- 需要穩定交接契約的多角色協作

**何時不啟用**：小工具、純前端、一次性腳本、探索性 AI 應用——避免過度工程。

**版本選型**：v9（7 模型，單體同步，最適合 AI 穩定出碼）用於實際落地；v6（11 模型，含事件／介面／持久化映射）用於理解全貌與複雜整合。

方法論已接入五位成員：瑞克標注驗收對應的操作功能點、阿奇產出正交模型、麥克做模型到程式碼映射、維拉做追溯門禁驗證。完整方法論見 `skills/ontology-modeling/SKILL.md`，署名與授權見同目錄 `ATTRIBUTION.md`。

## 選配管線：本體驅動端到端開發

第二個 Skill `skills/ontology-driven-dev/` 吸收自 [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev)（MIT，Copyright 2026 sharptoolbox），補上建模前後兩段：

- **需求探索八階段**：總體理解 → 業務對象 → 功能與規則 → 跨對象聯動 → 協同審批流 → 查詢報表 → 角色權限 → UI 原型
- **人工確認門禁**：每階段用固定格式提問並硬暫停等確認；A 類自動補全、B 類（企業專屬）必須確認，有 `[待確認]` 不得標記完整
- **10 步構建流水線**：從七模型 YAML 到 DDL、服務層、權限、流程引擎、頁面路由、AI 對話框（含唯讀 SQL 安全邊界）、全鏈路聯調與驗收

觸發方式：直接說「幫我開發一個 XX 管理系統」或「做本體驅動開發」，主理人會走 **Workflow L**：瑞克需求探索和人工確認 → 阿奇七模型 → 麥克構建 `code-app/` → 維拉追溯驗收。

兩個 Skill 分工：`ontology-modeling` 管建模細節，`ontology-driven-dev` 管端到端管線與工程落地。技術底座原始碼不內嵌，使用時從原始 repo 取得。

## 新增能力：逆向、可視化、簡報與知識庫

本版從 sharptoolbox 其餘倉庫再吸收四套方法論，全部做成**選配 Skill**，需要時才載入：

| Skill | 來源／授權 | 何時用 | 主責成員 |
|-------|-----------|--------|----------|
| `codebase-reverse` | [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) · MIT | 接手舊系統、遷移前置盤點、補寫需求文件 | 翠西（逆向）＋維拉（覆蓋對帳） |
| `visual-model` | [visual-model](https://github.com/sharptoolbox/visual-model) · CC BY 4.0 | 交付級架構圖、SysML 五視圖、知識圖譜 | 阿奇 |
| `consulting-html-ppt` | [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) · 未宣告授權 | 方案彙報、驗收簡報、可放映交付材料 | 黛拉 |
| `llm-knowledge-base` | [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) · MIT | RAG 知識萃取、來源約束問答 | 麥克＋維拉 |

### 完整融合：Open Knowledge Format（OKF）

逆向文件、架構決策與指標定義最大的風險是**默默過時**——檔案還在，但已不可信。本版完整引入 [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format)（Apache-2.0，publisher: Google，v0.3）的三套 Skill：

| Skill | 職責 |
|-------|------|
| `okf-format` | v0.3 格式規範：bundle 結構、frontmatter、溯源、信任分層、生命週期、可驗證計算 |
| `okf-generate` | 建立／更新／遷移／修復／驗證 bundle 的六條鐵律與程序 |
| `okf-consume` | 只讀問答，逐概念回報信任分層、status、新鮮度與來源 |

新增第八位成員**寇娜 Kona（知識管理師）**主導 OKF 寫入與查詢，維拉獨立覆核信任分層與 attestation。

**三個補上缺口的機制**：

- **信任分層**：unverified／machine-confirmed／human-reviewed。關鍵紀律是「AI 改寫已人工審核的概念後，人工審核立即失效」——這正是多智能體協作最容易自欺的地方。
- **stale_after 時效**：用絕對時間點判定過期，可機械比較；沒有已知複查週期就省略，不臆造日期。
- **可驗證計算**：agent 只能填參數、不能改公式；consumer 用確定性 attester 比對回執。這把幻覺防護從提示詞紀律升級為機械契約，也讓維拉的 `PASS/FAIL` 有可計算的依據。

`llm-knowledge-base` 與 OKF **明確分工**：前者管「如何從文章萃取場景／概念／實體」，後者管「知識如何持久化、交換與取信」。麥克萃取後交給寇娜補齊溯源與信任欄位，不重複做同一件事。原始 repo 的 Python 腳本不內嵌，署名見各 Skill 的 `ATTRIBUTION.md`。

**設計取捨**：

- **逆向是全量、深度可分层**：翠西先建立源碼資產台帳（B0–B9），再逐功能穿透到資料庫；維拉獨立做覆蓋對帳，未歸屬資產不放行。基線不全量就寫功能清單，是逆向最常見的失敗模式。
- **簡報忠於事實**：黛拉的頁面可以有四種形態（真實圖表／架構圖／結構模型／文本分類），但不得虛構數據，且每個技術主張要標註來源。維拉未給 `PASS` 前不開始製作。
- **授權分寸**：前三個有明確授權的專案僅濃縮重述並保留完整署名；`consulting-html-ppt` 原 repo **未宣告開源授權**，因此只吸收方法論要點，不複製其模板庫、圖標或成品，使用平台內建或自製模板替代。各 Skill 的 `ATTRIBUTION.md` 均保留來源與授權說明。

## 功能

- **任務路由**：先辨析類型與專案型態，再選流程；修 bug 不會被逼著寫 PRD
- **結構化交接**：階段間以 PRD／設計文件／變更摘要／測試報告交接，不靠口述
- **增量安全修改**：既有系統改動先做影響分析，保留向後相容
- **多型態驗證**：維拉（QA）依 Web／API／數據／AI 調整測試方式，修改類任務必做回歸
- **明確品質關卡**：維拉給出 `PASS`／`FAIL` 與證據，主理人不得代寫或軟化結論
- **人工確認門禁**：Workflow L 的需求探索逐階段提問並暫停等確認，杜絕 AI 自行假設企業專屬規則
- **源碼逆向**：Workflow M 全量基線＋功能穿透鏈＋覆蓋對帳，把隱藏功能與資料庫映射一併挖出
- **交付敘事**：Workflow N 把驗證通過的成果做成動作式標題的單檔 HTML 簡報
- **可信知識**：Workflow P 的 OKF bundle 讓每個概念都帶來源、信任層級與時效，拒絕靜默過時
- **協作鐵律**：主理人親自建團、所有資訊經主理人中轉、團員不互相直連

## 使用示例

- 我有一個開發需求，請判斷類型並用合適的流程交付。
- 幫我修這個 bug、加功能或重構這段程式碼。
- 審查這份程式碼，給出測試用例與品質報告。
- 幫我把這個舊專案從 Python 2 遷移到 3，並補回歸測試。
- 我想做一個 RAG 問答應用，請從資料規格到可運行程式完整交付。
- 幫我設計一個採購審批系統，要能追溯到每條需求對應的程式碼位置。
- 用本體驅動開發做一個合同管理系統，需求探索每個階段都要我確認。
- 接手這個舊專案，幫我逆向出完整的功能清單、穿透鏈和資料庫表，還要找出沒有菜單的定時任務。
- 把這次的交付成果做成一份 12 頁的諮詢風格 HTML 簡報，技術結論要標註來源。
- 幫我建立一個 OKF 知識庫，並告訴我哪些概念未驗證或已經過期。

## 頭像

頭像已自動生成在 `avatars/` 目錄下。如需替換為自訂頭像，要求：
- 格式：PNG（推薦）或 JPG
- 尺寸：512×512 px
- 大小：單張不超過 500KB

## 安裝

將專家包目錄放到專家目錄下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/julia-dev/
```

然後執行註冊命令使其可見：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## 打包分享

```bash
zip -r julia-dev.zip julia-dev/
```
