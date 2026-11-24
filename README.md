# 主理呀開發團 (Julia Dev Squad)

團隊名取自主理人茱莉亞的諧音「主理呀」——先辨析任務、再編排流程、最後交付。英文保留 Julia 作為花名，改用 Squad 強調這是一支團隊，也避免被誤讀為 Julia 程式語言開發。

由茱莉亞統籌的全方位軟體開發專家團。不論是源碼逆向、從零建置、加功能、修 bug、重構、審查、遷移、串接第三方、數據／AI 應用或交付簡報，都會先辨析任務類型，再調度最合適的團隊流程交付。

## 類型

Team 型（多角色協作團隊）· 版本 1.7.1 · 10 位成員

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
| release-engineer | 席普 Ship | 發布工程師 | ship——把驗證過的東西安全送上線的人 |
| decision-advisor | 艾德 Ed | 決策顧問 | advisor——在昂貴或不可逆之前被找來的第一個反對者 |

## 任務類型與流程對照

主理人茱莉亞會先做 **Phase 0 任務辨析**，再從 20 條 Workflow 中選一條；不需要的階段直接略過，不浪費流程。

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
| 先重現再修／證明真的可用 | 嚴謹工程 | Q pstack 嚴謹工程 |
| 合併 PR／接手上一輪／我要睡覺 | 發布接續 | R 發布與會話接續 |
| 拆並行任務／跑有界循環／讓 CI 全綠 | 結構化編排 | S 結構化編排與有界循環 |
| 深度 review PR／安全＋可維護性雙軸 | 深度差異審查 | T 深度差異審查與決策複核 |
| 找盲點／卡兩次／交付前再確認 | 決策複核 | T 或直調艾德 |
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

### 嚴謹工程與可驗證交付：pstack

本版吸收 [cursor/plugins 的 pstack](https://github.com/cursor/plugins/tree/main/pstack)（作者 Lauren Tan，MIT，19k stars）——這是 Cursor 官方插件庫中最受歡迎的插件之一，核心主張是「想快就先深入」「寫更少但更好的程式」。四套 Skill 各自職責：

| Skill | 職責 |
|-------|------|
| `pstack-principles` | 24 條工程原則（核心／架構／驗證／委派／後設），回答「怎樣才算做好」 |
| `pstack-playbooks` | 22 個 playbook 路由，展開 bug fix、perf、feature、shipping、session pickup 等關鍵流程 |
| `pstack-verification` | 證明它可行、基準檢驗七問、建立專案本地驗證 Skill、形式化驗證、把錯誤釘進結構 |
| `pstack-parallel-review` | swarm（分割／競速）、arena（競技與移植強項）、interrogate（對抗式審查，只留跑過的發現） |

新增第九位成員**席普 Ship（發布工程師）**：維拉判定對不對，席普負責讓對的東西安全落地——獨立驗證每個 PR、只合併從底部起連續通過的區段、用 `git patch-id` 核對 rebase 前的裁決是否仍有效、落地期間不碰分支、停在上限。

**三個最值得吸收的紀律**：

- **每行程式碼追溯到執行期證據**：bug fix 必須先重現、二分法找根因，「可能有用」的防護是假設不是修復，證據反駁就回退。
- **基準檢驗七問**：說出限制因子、確認對等調校、做數量級算術、計數錯誤、交替跑五次以上、量端到端、確認工作真的發生了。過不了就標 inconclusive，不宣稱加速。
- **對抗式審查只留跑過的發現**：沒有指令輸出證明的問題（含風格、命名、結構）一律丟棄；共享根因合併；「沒有發現」是有效結果。

**與既有能力的分工**：`ontology-modeling` 查需求到程式碼的對應、`pstack-verification` 查實際跑起來的行為、OKF attestation 查計算回執是否被竄改——三者互補。CI 專屬的模型設定與插件依賴沒有內嵌，署名見各 Skill 的 `ATTRIBUTION.md`。

**門禁衝突的處理**：pstack 主張「可逆工作不要問人」，本團隊的優先序是人工確認門禁 > 維拉 `PASS` > 不可逆動作確認 > 其餘可逆工作直接做。

**設計取捨**：

- **逆向是全量、深度可分層**：翠西先建立源碼資產台帳（B0–B9），再逐功能穿透到資料庫；維拉獨立做覆蓋對帳，未歸屬資產不放行。基線不全量就寫功能清單，是逆向最常見的失敗模式。
- **簡報忠於事實**：黛拉的頁面可以有四種形態（真實圖表／架構圖／結構模型／文本分類），但不得虛構數據，且每個技術主張要標註來源。維拉未給 `PASS` 前不開始製作。
- **授權分寸**：前三個有明確授權的專案僅濃縮重述並保留完整署名；`consulting-html-ppt` 原 repo **未宣告開源授權**，因此只吸收方法論要點，不複製其模板庫、圖標或成品，使用平台內建或自製模板替代。各 Skill 的 `ATTRIBUTION.md` 均保留來源與授權說明。

## 再進化：cursor/plugins 其他高價值專案

本版再掃描 [cursor/plugins](https://github.com/cursor/plugins/tree/main) 全庫，挑出四組對多智能體軟體交付真正有增量的做法，全部轉成**選配 Skill**；Cursor 專屬的 SDK、Bun 腳本、hooks 與 Slack 整合一律不內嵌，只保留可移植的方法論。

| 新 Skill | 吸收來源 | 做什麼 | 主責成員 |
|---------|---------|-------|---------|
| `structured-orchestration` | `orchestrate`＋`ralph-loop`＋`cursor-team-kit/loop-on-ci`（MIT） | Planner／Worker／Verifier 職責邊界、逐字交接、五級 verifier 證據、完成承諾＋迭代上限、失敗模式與 Andon、`gh pr checks` CI 迴圈 | 茱莉亞（編排）＋席普（CI） |
| `deep-diff-review` | `thermos`＋`dyl-stack`（MIT） | 正確性／安全與結構／可維護性雙軸平行審查、code judo／1k 行／spaghetti 尺標、去重後最多 7 則可貼 comment 與 🟢／🟡／🔴 | 維拉＋阿奇，艾德複核重大發現 |
| `decision-gates` | `advisor`＋`dyl-stack`（MIT） | 重大決策／卡兩次／完成前四類檢查點、唯讀 `Verdict / Why / Recommendations / Risks / Answers / Confidence`、The Algorithm、根因句、合併與 taste veto 紀律 | 艾德 |
| `agent-friendly-cli` | `cli-for-agent`（MIT） | 非互動 flag、分層 help 與範例、stdin／pipeline、可行動錯誤、冪等、`--dry-run`、JSON 輸出與退出碼 | 麥克＋阿奇 |

新增第十位成員**艾德 Ed（決策顧問）**：他不寫程式、不開 PR、不合併，只在昂貴或不可逆之前給第二意見。他的建議不能覆蓋人工確認門禁、維拉 `PASS` 或不可逆動作確認——這是本團隊刻意設定的優先序。

**四個最值得吸收的紀律**：

- **Planner 不寫程式，Worker 不互聯，Verifier 不改目標原始碼**。`orchestrate` 用逐字 handoff 取代共享狀態，讓平行任務可以收斂而不靠全域協調；下游需要上游資訊就宣告依賴，由主理人轉交。
- **完成要有承諾與上限**。Ralph Loop 的同一提示詞反覆迭代、只能在工作真的完成時輸出承諾；到上限就如實回報未完成，防止 agent 為了結案說謊。Verifier 的 `verifier-blocked` 也禁止把環境故障偽裝成通過。
- **深度審查要雙軸、要只罵 diff、要少而準**。Thermos 把 bug／安全／devex／feature gate 與可維護性分開；dyl-stack 把發現壓縮成最多 7 則可貼 comment 與一個燈號，且永遠不貼到 PR、不 approve、不合併。
- **先問需求、先刪除、再優化**。`The Algorithm` 與 `Root cause: X because Y` 補上 pstack 的根因紀律：null guard、retry、sleep、skip、snapshot 更新在根因句成立前都只是症状修復。

**沒有吸收的部分**：`orchestrate` 的 Cursor SDK／Bun CLI／Slack Andon 腳本、`ralph-loop` 的 hooks、`advisor` 的模型綁定與 state 檔、`thermos` 的 subagent 定義、`dyl-stack` 的 Figma／UI judge 流程——這些都綁定特定平台或工具，移植成本高於收益；`agent-compatibility`、`continual-learning`、`workflow-from-chats` 的洞察已分別被既有驗證、知識管理與偏好沉澱機制覆蓋，不重複造一套。

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
- **嚴謹工程**：Workflow Q 以執行期證據取代自我回報，Workflow R 只落地通過驗證的連續區段
- **結構化編排**：Workflow S 用 worker／verifier 交接與有界循環推進大型任務，CI 以 `gh pr checks` 為準
- **深度差異審查**：Workflow T 雙軸審查 diff，只輸出最多 7 則可貼 comment 與一個燈號，不貼 PR、不 approve
- **決策第二意見**：艾德在重大決策、卡兩次與完成前給唯讀判決，並用 The Algorithm 與根因句擋掉症状修復
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
- 用嚴謹工程流程修這個 bug：先重現、二分法找根因，再給我失敗到通過的輸出。
- 這串 PR 都綠燈了，幫我驗證後由底層往上合併，並告訴我停在哪個上限。
- 把這個大任務拆成 worker／verifier，跑一個有完成承諾與上限的循環，最後給我交接紀錄。
- 深度 review 這個 PR：安全與可維護性分開看，只給我最多 7 則可貼的 comment 和一個燈號。
- 我卡在同一個錯誤兩次了，請艾德讀證據後給第二意見，並先用 The Algorithm 問需求。

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
