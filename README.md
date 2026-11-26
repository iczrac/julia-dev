# 主理呀開發團 (Julia Dev Squad)

團隊名取自主理人Julia的諧音「主理呀」——先辨析任務、再編排流程、最後交付。英文保留 Julia 作為花名，改用 Squad 強調這是一支團隊，也避免被誤讀為 Julia 程式語言開發。

由Julia統籌的全方位軟體開發專家團。不論是源碼逆向、從零建置、加功能、修 bug、重構、審查、遷移、串接第三方、數據／AI 應用或交付簡報，都會先辨析任務類型，再調度最合適的團隊流程交付。

## 類型

Team 型（多角色協作團隊）· 版本 1.10.17 · 11 位成員

## 成員與命名巧思

| 成員 ID | 名字 | 職業 | 巧思 |
|---------|------|------|------|
| julia-dev-team-lead | Julia | 交付總監 | 諧音「主理呀」——主理人 |
| product-manager | Remy | 產品經理 | req（requirement）需求——取 re 起首 |
| architect | Archie | 架構師 | arch（architecture）架構 |
| engineer | Mark | 工程師 | make——動手造東西的人（取 ma 起首） |
| qa-engineer | Vera | 品質保證工程師 | verify——驗證的化身 |
| reverse-engineer | Tracey | 逆向工程師 | trace——追溯源碼，從入口追到資料庫 |
| delivery-designer | Della | 交付設計師 | deck／deliver——做出可放映的交付簡報 |
| knowledge-curator | Knox | 知識管理師 | know——知識的守護者（kn 起首；Fort Knox 金庫意象，管溯源、信任與時效） |
| release-engineer | Ship | 發布工程師 | ship——把驗證過的東西安全送上線的人 |
| decision-advisor | Ed | 決策顧問 | advisor——在昂貴或不可逆之前被找來的第一個反對者 |
| ledger-liaison | Luca | 帳本對接官 | route＋task card——把 ledger 的路線卡翻成 Julia 的任務 |

## 任務類型與流程對照

主理人Julia會先做 **Phase 0 任務辨析**，再從 21 條 Workflow 中選一條；不需要的階段直接略過，不浪費流程。

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
| 找盲點／卡兩次／交付前再確認 | 決策複核 | T 或直調Ed |
| 對接 ledger／照帳本路由走／從 next_queue 拿任務 | 帳本對接 | U 帳本對接與受控寫入 |
| 用什麼技術比較好 | 技術咨詢 | B 或直接問Archie |

## 適用專案型態

Web 前端、後端 API、全端應用、CLI／自動化腳本、桌面應用、行動應用、資料處理、AI／LLM 應用、資料庫設計、DevOps／部署。

每種型態都有對應的設計與驗證重點，會由主理人在派工時明確寫給團員，例如 API 重契約與錯誤碼、AI 應用重幻覺防護與成本、CLI 重冪等性與輸出格式。

## 選配方法論：本體驅動建模

Expert 包內建 `skills/ontology-modeling/`，吸收自開源框架 [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework)（作者 @人月聊IT，Apache-2.0）。它把業務系統切成**正交、可獨立演進、可用 YAML 承載**的模型關切，建立「需求 → 設計 → 程式碼」的可追蹤鏈。

**何時啟用**（由Archie在 Phase 2 載入）：

- 中大型業務系統（ERP／CRM／審批／合同管理）
- 規則密集、跨物件聯動多、需要稽核溯源
- 需要穩定交接契約的多角色協作

**何時不啟用**：小工具、純前端、一次性腳本、探索性 AI 應用——避免過度工程。

**版本選型**：v9（7 模型，單體同步，最適合 AI 穩定出碼）用於實際落地；v6（11 模型，含事件／介面／持久化映射）用於理解全貌與複雜整合。

方法論已接入五位成員：Remy標注驗收對應的操作功能點、Archie產出正交模型、Mark做模型到程式碼映射、Vera做追溯門禁驗證。完整方法論見 `skills/ontology-modeling/SKILL.md`，署名與授權見同目錄 `ATTRIBUTION.md`。

## 選配管線：本體驅動端到端開發

第二個 Skill `skills/ontology-driven-dev/` 吸收自 [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev)（MIT，Copyright 2026 sharptoolbox），補上建模前後兩段：

- **需求探索八階段**：總體理解 → 業務對象 → 功能與規則 → 跨對象聯動 → 協同審批流 → 查詢報表 → 角色權限 → UI 原型
- **人工確認門禁**：每階段用固定格式提問並硬暫停等確認；A 類自動補全、B 類（企業專屬）必須確認，有 `[待確認]` 不得標記完整
- **10 步構建流水線**：從七模型 YAML 到 DDL、服務層、權限、流程引擎、頁面路由、AI 對話框（含唯讀 SQL 安全邊界）、全鏈路聯調與驗收

觸發方式：直接說「幫我開發一個 XX 管理系統」或「做本體驅動開發」，主理人會走 **Workflow L**：Remy需求探索和人工確認 → Archie七模型 → Mark構建 `code-app/` → Vera追溯驗收。

兩個 Skill 分工：`ontology-modeling` 管建模細節，`ontology-driven-dev` 管端到端管線與工程落地。技術底座原始碼不內嵌，使用時從原始 repo 取得。

## 新增能力：逆向、可視化、簡報與知識庫

本版從 sharptoolbox 其餘倉庫再吸收四套方法論，全部做成**選配 Skill**，需要時才載入：

| Skill | 來源／授權 | 何時用 | 主責成員 |
|-------|-----------|--------|----------|
| `codebase-reverse` | [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) · MIT | 接手舊系統、遷移前置盤點、補寫需求文件 | Tracey（逆向）＋Vera（覆蓋對帳） |
| `visual-model` | [visual-model](https://github.com/sharptoolbox/visual-model) · CC BY 4.0 | 交付級架構圖、SysML 五視圖、知識圖譜 | Archie |
| `consulting-html-ppt` | [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) · 未宣告授權 | 方案彙報、驗收簡報、可放映交付材料 | Della |
| `llm-knowledge-base` | [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) · MIT | RAG 知識萃取、來源約束問答 | Mark＋Vera |

### 完整融合：Open Knowledge Format（OKF）

逆向文件、架構決策與指標定義最大的風險是**默默過時**——檔案還在，但已不可信。本版完整引入 [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format)（Apache-2.0，publisher: Google，v0.3）的三套 Skill：

| Skill | 職責 |
|-------|------|
| `okf-format` | v0.3 格式規範：bundle 結構、frontmatter、溯源、信任分層、生命週期、可驗證計算 |
| `okf-generate` | 建立／更新／遷移／修復／驗證 bundle 的六條鐵律與程序 |
| `okf-consume` | 只讀問答，逐概念回報信任分層、status、新鮮度與來源 |

新增第八位成員**Knox（知識管理師）**主導 OKF 寫入與查詢，Vera獨立覆核信任分層與 attestation。

**三個補上缺口的機制**：

- **信任分層**：unverified／machine-confirmed／human-reviewed。關鍵紀律是「AI 改寫已人工審核的概念後，人工審核立即失效」——這正是多智能體協作最容易自欺的地方。
- **stale_after 時效**：用絕對時間點判定過期，可機械比較；沒有已知複查週期就省略，不臆造日期。
- **可驗證計算**：agent 只能填參數、不能改公式；consumer 用確定性 attester 比對回執。這把幻覺防護從提示詞紀律升級為機械契約，也讓Vera的 `PASS/FAIL` 有可計算的依據。

`llm-knowledge-base` 與 OKF **明確分工**：前者管「如何從文章萃取場景／概念／實體」，後者管「知識如何持久化、交換與取信」。Mark萃取後交給Knox補齊溯源與信任欄位，不重複做同一件事。原始 repo 的 Python 腳本不內嵌，署名見各 Skill 的 `ATTRIBUTION.md`。

### 嚴謹工程與可驗證交付：pstack

本版吸收 [cursor/plugins 的 pstack](https://github.com/cursor/plugins/tree/main/pstack)（作者 Lauren Tan，MIT，19k stars）——這是 Cursor 官方插件庫中最受歡迎的插件之一，核心主張是「想快就先深入」「寫更少但更好的程式」。四套 Skill 各自職責：

| Skill | 職責 |
|-------|------|
| `pstack-principles` | 24 條工程原則（核心／架構／驗證／委派／後設），回答「怎樣才算做好」 |
| `pstack-playbooks` | 22 個 playbook 路由，展開 bug fix、perf、feature、shipping、session pickup 等關鍵流程 |
| `pstack-verification` | 證明它可行、基準檢驗七問、建立專案本地驗證 Skill、形式化驗證、把錯誤釘進結構 |
| `pstack-parallel-review` | swarm（分割／競速）、arena（競技與移植強項）、interrogate（對抗式審查，只留跑過的發現） |

新增第九位成員**Ship（發布工程師）**：Vera判定對不對，Ship負責讓對的東西安全落地——獨立驗證每個 PR、只合併從底部起連續通過的區段、用 `git patch-id` 核對 rebase 前的裁決是否仍有效、落地期間不碰分支、停在上限。

**三個最值得吸收的紀律**：

- **每行程式碼追溯到執行期證據**：bug fix 必須先重現、二分法找根因，「可能有用」的防護是假設不是修復，證據反駁就回退。
- **基準檢驗七問**：說出限制因子、確認對等調校、做數量級算術、計數錯誤、交替跑五次以上、量端到端、確認工作真的發生了。過不了就標 inconclusive，不宣稱加速。
- **對抗式審查只留跑過的發現**：沒有指令輸出證明的問題（含風格、命名、結構）一律丟棄；共享根因合併；「沒有發現」是有效結果。

**與既有能力的分工**：`ontology-modeling` 查需求到程式碼的對應、`pstack-verification` 查實際跑起來的行為、OKF attestation 查計算回執是否被竄改——三者互補。CI 專屬的模型設定與插件依賴沒有內嵌，署名見各 Skill 的 `ATTRIBUTION.md`。

**門禁衝突的處理**：pstack 主張「可逆工作不要問人」，本團隊的優先序是：人工確認 > ledger 寫入（僅 ledger 語境，是人工確認的具體化）> 不可逆動作確認 > Vera 證據支持 PASS／FAIL（test_report＋綁定＋不變量通過，非聊天式 PASS）> 其餘可逆工作；Vera PASS 永不取代人工確認，非 ledger 語境略去第二項。

**設計取捨**：

- **逆向是全量、深度可分層**：Tracey先建立源碼資產台帳（B0–B9），再逐功能穿透到資料庫；Vera獨立做覆蓋對帳，未歸屬資產不放行。基線不全量就寫功能清單，是逆向最常見的失敗模式。
- **簡報忠於事實**：Della的頁面可以有四種形態（真實圖表／架構圖／結構模型／文本分類），但不得虛構數據，且每個技術主張要標註來源。Vera未給 `PASS` 前不開始製作。
- **授權分寸**：前三個有明確授權的專案僅濃縮重述並保留完整署名；`consulting-html-ppt` 原 repo **未宣告開源授權**，因此只吸收方法論要點，不複製其模板庫、圖標或成品，使用平台內建或自製模板替代。各 Skill 的 `ATTRIBUTION.md` 均保留來源與授權說明。

## 再進化：cursor/plugins 其他高價值專案

本版再掃描 [cursor/plugins](https://github.com/cursor/plugins/tree/main) 全庫，挑出四組對多智能體軟體交付真正有增量的做法，全部轉成**選配 Skill**；Cursor 專屬的 SDK、Bun 腳本、hooks 與 Slack 整合一律不內嵌，只保留可移植的方法論。

| 新 Skill | 吸收來源 | 做什麼 | 主責成員 |
|---------|---------|-------|---------|
| `structured-orchestration` | `orchestrate`＋`ralph-loop`＋`cursor-team-kit/loop-on-ci`（MIT） | Planner／Worker／Verifier 職責邊界、逐字交接、五級 verifier 證據、完成承諾＋迭代上限、失敗模式與 Andon、`gh pr checks` CI 迴圈 | Julia（編排）＋Ship（CI） |
| `deep-diff-review` | `thermos`＋`dyl-stack`（MIT） | 正確性／安全與結構／可維護性雙軸平行審查、code judo／1k 行／spaghetti 尺標、去重後最多 7 則可貼 comment 與 🟢／🟡／🔴 | Vera＋Archie，Ed複核重大發現 |
| `decision-gates` | `advisor`＋`dyl-stack`（MIT） | 重大決策／卡兩次／完成前四類檢查點、唯讀 `Verdict / Why / Recommendations / Risks / Answers / Confidence`、The Algorithm、根因句、合併與 taste veto 紀律 | Ed |
| `agent-friendly-cli` | `cli-for-agent`（MIT） | 非互動 flag、分層 help 與範例、stdin／pipeline、可行動錯誤、冪等、`--dry-run`、JSON 輸出與退出碼 | Mark＋Archie |

新增第十位成員**Ed（決策顧問）**：他不寫程式、不開 PR、不合併，只在昂貴或不可逆之前給第二意見。他的建議不能覆蓋人工確認門禁、Vera `PASS` 或不可逆動作確認——這是本團隊刻意設定的優先序。

**四個最值得吸收的紀律**：

- **Planner 不寫程式，Worker 不互聯，Verifier 不改目標原始碼**。`orchestrate` 用逐字 handoff 取代共享狀態，讓平行任務可以收斂而不靠全域協調；下游需要上游資訊就宣告依賴，由主理人轉交。
- **完成要有承諾與上限**。Ralph Loop 的同一提示詞反覆迭代、只能在工作真的完成時輸出承諾；到上限就如實回報未完成，防止 agent 為了結案說謊。Verifier 的 `verifier-blocked` 也禁止把環境故障偽裝成通過。
- **深度審查要雙軸、要只罵 diff、要少而準**。Thermos 把 bug／安全／devex／feature gate 與可維護性分開；dyl-stack 把發現壓縮成最多 7 則可貼 comment 與一個燈號，且永遠不貼到 PR、不 approve、不合併。
- **先問需求、先刪除、再優化**。`The Algorithm` 與 `Root cause: X because Y` 補上 pstack 的根因紀律：null guard、retry、sleep、skip、snapshot 更新在根因句成立前都只是症状修復。

**沒有吸收的部分**：`orchestrate` 的 Cursor SDK／Bun CLI／Slack Andon 腳本、`ralph-loop` 的 hooks、`advisor` 的模型綁定與 state 檔、`thermos` 的 subagent 定義、`dyl-stack` 的 Figma／UI judge 流程——這些都綁定特定平台或工具，移植成本高於收益；`agent-compatibility`、`continual-learning`、`workflow-from-chats` 的洞察已分別被既有驗證、知識管理與偏好沉澱機制覆蓋，不重複造一套。

## 選配協定：ledger-driven-dev 帳本橋接

第十一位成員**Luca（帳本對接官）**與第十八套 Skill `ledger-bridge`，把 [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev)（MIT，Copyright 2026 Ledger-Driven Dev contributors）的治理能力接進 Julia 的執行鏈。這不是把兩邊合併，而是一層**只讀薄橋**：

| 交接物件 | 用途 |
|---------|------|
| `intent.json` | 把人話需求、非目標、能力碼與寫入範圍變成可校驗意圖 |
| `route.handoff` / `next_queue` | 取得唯一專家、交接鏈與單張任務卡 |
| `test_report` + `verify_ledger` JSON | 把Vera的證據換算成 `declared / verified` 與不變量結果 |
| `approval_bundle` / `audit` | 只準備待批准命令，由人工簽核、Ship執行 |

**ledger-driven-dev 倉庫本身零改動**：不改 schema、不改 31 條不變量、不加新專家、不複製 24 個 Skill。需要在目標專案做的是一次性的治理接入：能力碼、`verify_ledger`、Agent 註冊與測試證據綁定。

門禁優先序：**人工確認 > ledger 寫入（僅 ledger 語境，是人工確認的具體化）> 不可逆動作確認 > Vera 證據支持 PASS／FAIL（test_report＋綁定＋不變量通過，非聊天式 PASS）> 其餘可逆工作；Vera PASS 永不取代人工確認，非 ledger 語境略去第二項**。Luca只讀、只翻譯、只準備；不得帶 `--apply` 執行寫入，也不得把 ledger JSON 複製成 julia-dev 內的第二份事實源。ledger v2.24–v2.25 對接後新增四條紀律：**證據降級條款**（工具指紋漂移使既有 `verified` 回落 `declared`，須重跑產證）、**文檔寫入路由**（治理項目 `docs/**` 必經 intent，成員不得直寫）、**門禁口徑 0≠n/a**（`stale_unknown` 單列，缺鍵 fail-closed）、**Preflight 加查 `upgrade verify` 與資產指紋**（ledger 更新後目標項目需重新批准升級）。方法論濃縮見 `skills/ledger-bridge/SKILL.md`，授權見同目錄 `ATTRIBUTION.md`。

## v1.9.0：接縫修補

協作落地後的缺口再評估發現，問題已從「能力不足」轉為「接縫與可運行性」。本版在不加成員、不加 Workflow 的前提下補上五項機制：

| 機制 | 解決的缺口 | 落點 |
|------|-----------|------|
| **足跡規範（footprint）** | 三處引用足跡卻無格式、無落點、無責任人 | 主理人 SOP「足跡規範」＋Vera／Ship／Ed MD |
| **契約唯一入口** | `intent.json` 與Julia任務契約雙寫，誰為準未定 | Phase 0.5＋Workflow U＋ledger-bridge 硬規則 8 |
| **PASS 分級** | 聊天式 `PASS` 與 ledger `verified` 混用導致含金量通脹 | Phase 4＋ledger-bridge 硬規則 10；治理專案一律 `verified-PASS` |
| **解阻（Andon）** | fail-closed 一路「停」，但停了之後無恢復路徑 | ledger-bridge「解阻」節＋嚴禁行為；卡兩次必須向使用者 Andon |
| **Preflight** | 橋接命令依賴目標專案安裝的 ledger 腳本，版本漂移無前置檢查 | Phase 0.5＋Workflow U 前置＋ledger-bridge「Preflight」節 |

足跡與 ledger、OKF 的分工固定為：**ledger＝專案事實源，OKF＝外部知識可信層，footprint＝當前工作現場草稿**；三者不互相複製，足跡只引用前兩者。

## 進化機制：受控自我進化

成員是每次會話臨時 spawn 的執行者，沒有跨會話記憶——真正能進化的載體只有專家包文件本身。因此進化不採用自由自我修改，而是六步回路：**成員提案（重複 ≥2 次才夠格）→ Ed 唯讀複核 → 人拍板（唯一生效門）→ 主理人執行修改 → `bash scripts/check.sh` 全綠 → `git commit`（一次生效 = 一個 commit）→ patch 版本 +1；不存在 `validate_expert` / `register_expert` 命令 → 進化日誌登記**。

- 提案固定七段格式，必須附可驗證證據；規則修改採合併替換不堆疊
- 禁區（嚴禁行為、門禁優先序、成員邊界、四類交接對象）只能由人主動修改，成員不可提案
- 一次生效 = 一個 commit，天然回滾點；變更史見 `docs/evolution-log.md`，回路規則見 `skills/self-evolution/SKILL.md`

## 功能

- **任務路由**：先辨析類型與專案型態，再選流程；修 bug 不會被逼著寫 PRD
- **結構化交接**：階段間以 PRD／設計文件／變更摘要／測試報告交接，不靠口述
- **增量安全修改**：既有系統改動先做影響分析，保留向後相容
- **多型態驗證**：Vera（QA）依 Web／API／數據／AI 調整測試方式，修改類任務必做回歸
- **明確品質關卡**：Vera給出 `PASS`／`FAIL` 與證據，主理人不得代寫或軟化結論
- **人工確認門禁**：Workflow L 的需求探索逐階段提問並暫停等確認，杜絕 AI 自行假設企業專屬規則
- **源碼逆向**：Workflow M 全量基線＋功能穿透鏈＋覆蓋對帳，把隱藏功能與資料庫映射一併挖出
- **交付敘事**：Workflow N 把驗證通過的成果做成動作式標題的單檔 HTML 簡報
- **可信知識**：Workflow P 的 OKF bundle 讓每個概念都帶來源、信任層級與時效，拒絕靜默過時
- **嚴謹工程**：Workflow Q 以執行期證據取代自我回報，Workflow R 只落地通過驗證的連續區段
- **結構化編排**：Workflow S 用 worker／verifier 交接與有界循環推進大型任務，CI 以 `gh pr checks` 為準
- **深度差異審查**：Workflow T 雙軸審查 diff，只輸出最多 7 則可貼 comment 與一個燈號，不貼 PR、不 approve
- **決策第二意見**：Ed在重大決策、卡兩次與完成前給唯讀判決，並用 The Algorithm 與根因句擋掉症状修復
- **帳本對接**：Workflow U 用Luca串接 ledger 的復述門、專家路由、任務卡、證據分級與受控寫入，避免雙重路由與第二事實源
- **AI 評估雙基線**：Workflow K 進入實作前固化 golden set、版本號與成本預算，Phase 4 必須「效果＋成本」一起交付，缺一即 FAIL
- **系統級安全清單**：上線前由Vera跑 secrets／依賴許可證／PII／權限／威脅建模／無障礙六項檢查，🔴 未釋清Ship不得落地；威脅建模摘要是Archie設計文件的必含節
- **環境腳本有主**：launch／doctor／drive／evidence 等環境與取證腳本由 Mark 長期維護，環境故障先修腳本，不作為驗證藉口
- **受控自我進化**：成員提案、Ed 複核、人拍板、主理人執行；git commit 即回滾點，進化全程可追溯
- **內部體檢（Workflow V）**：機械自查（ledger spec_check 九判據）→ Vera 抽驗日誌與 dist → Knox 掃規矩冗餘（`scripts/knox_scan.py`）→ Ed 裁決必修/豁免/緩議 → 走進化提案；觸發＝操作人要求／minor 累計 +5／大版本前，未觸發不空跑
- **規劃期第一性原理分解**：Remy對每條需求標註「硬約束／慣例」歸類（慣例必附依據），Archie設計文件必含「基本事實表」（各註來源），類比式設計在規劃期即被攔截
- **操作人模式可切換**：門外漢／標準／專家三檔，Phase 0 聲明、隨時切換；門外漢模式附白話摘要與行為驗收清單、技術決策代勞 opt-out；不可逆門禁與測試門任何模式都不放鬆
- **門外漢模式五護欄**：模式探測（偏門外漢語言主動建議切換）、代勞決策清單（人話記錄、可逐條翻案）、人話交接卡（成品位置＋使用說明＋回訪召喚語）、快捷回覆提問（A/B 選項可一句答完）、「感覺不對」有效信號通道
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
- 我卡在同一個錯誤兩次了，請Ed讀證據後給第二意見，並先用 The Algorithm 問需求。
- 對接這個專案的 ledger，照 route 找負責人，從 next_queue 拿一張卡給我。
- 把Vera的測試證據換算成 ledger 的 verified，準備批准包但先不要寫入。

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

平台直接從該 marketplace 目錄載入專家包；本倉不提供註冊腳本，無須執行註冊命令。若專家未出現在清單中，請在 WorkBuddy 的專家／外掛管理頁重新載入該 marketplace。

## 開發迭代史

本專家包的進化全部來自四個渠道：使用者拍板、缺口評估走查、實測回灌、外部開源吸收，並一律走「提案 → Ed 複核 → 人拍板 → 主理人執行 → commit」的受控回路。從包建立期（v1.0–v1.8.x）、接縫修補（v1.9.0）、實測回灌（v1.9.1）、制度化期（v1.10.0–1.10.2）、可用性期（v1.10.3–1.10.5）、發行與治理期（v1.10.6–1.10.8）到命名與文檔期（v1.10.9–1.10.10）的完整敘事、各版本來源與歷史教訓清單，見 [`docs/iteration-history.md`](docs/iteration-history.md)；逐條變更記錄見 [`docs/evolution-log.md`](docs/evolution-log.md)。

## 致謝

本專家包是對下列開源專案方法論的**濃縮重述**，不是原始文件複製；每個派生 Skill 目錄下有獨立 `ATTRIBUTION.md` 記錄確切來源與授權條款。各來源專案依其自身授權（MIT／Apache 2.0／CC BY 4.0）持續有效，感謝原作者的開源貢獻：

| 來源專案 | 作者／持有者 | 授權 | 吸收為 |
|----------|-------------|------|--------|
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | Lauren Tan | MIT | pstack-principles／playbooks／verification／parallel-review |
| [orchestrate](https://github.com/cursor/plugins/tree/main/orchestrate)、[ralph-loop](https://github.com/cursor/plugins/tree/main/ralph-loop)、[cursor-team-kit](https://github.com/cursor/plugins/tree/main/cursor-team-kit) | Cursor | MIT | structured-orchestration |
| [thermos](https://github.com/cursor/plugins/tree/main/thermos)、[dyl-stack](https://github.com/cursor/plugins/tree/main/dyl-stack) | Cursor／Dylan Gattey | MIT | deep-diff-review |
| [advisor](https://github.com/cursor/plugins/tree/main/advisor)、dyl-stack | Cursor／Dylan Gattey | MIT | decision-gates |
| [cli-for-agent](https://github.com/cursor/plugins/tree/main/cli-for-agent) | Eric Zakariasson | MIT | agent-friendly-cli |
| [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev) | sharptoolbox | MIT | ontology-driven-dev |
| [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) | sharptoolbox | MIT | codebase-reverse |
| [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) | sharptoolbox | MIT | llm-knowledge-base |
| [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework) | sharptoolbox（@人月聊IT） | Apache 2.0 | ontology-modeling |
| [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format) | open-knowledge-format contributors（Google） | Apache 2.0 | okf-format／generate／consume |
| [visual-model](https://github.com/sharptoolbox/visual-model) | sharptoolbox | CC BY 4.0 | visual-model |
| [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) | sharptoolbox | 未宣告授權 | consulting-html-ppt（僅吸收方法要點，未複製模板或素材） |
| [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev) | iczrac | MIT | ledger-bridge＋Luca 角色 |

`self-evolution` Skill、操作人模式與門外漢護欄為本專家包原創。本專家包自身以 MIT 授權發布，見根目錄 `LICENSE`。

## 多平台適配

本專家包以 WorkBuddy 包為 **canonical 單一事實源**，其他平台包由 `python3 scripts/build_dist.py` 自動生成到 `dist/`，永遠以腳本重建、不手改。所有平台共享同一套鐵律：門禁、測試取證、操作人模式、第一性原理門與進化提案紀律。

| 發行目錄 | 平台 | 形態 | 適配方式 |
|----------|------|------|----------|
| `dist/claude-code/` | Claude Code | **完整團隊** | `.claude-plugin/plugin.json`＋11 個 subagents＋19 skills＋`/julia` 指令 |
| `dist/agents-md/` | Codex CLI／Gemini CLI／Jules 等 | **Solo（角色內切）** | `AGENTS.md` 總綱＋`roles/`＋`skills/`；單代理按階段戴帽執行，Ed／Vera 轉為自我複核帽與實跑測試帽 |
| `dist/cursor/` | Cursor | Solo 變體 | `.cursor/rules/julia-dev.mdc`（`alwaysApply`）＋`roles/`＋`skills/` |
| `dist/copilot/` | VS Code Copilot | 自定義 agents | `.github/agents/` 11 個代理；無自動路由，操作人顯式 `@julia-dev-team-lead` 統籌 |

改寫紀律：跨平台轉換只做**語義等價**改寫（如 SendMessage 協作語義改為結果回傳、清理平台專有 frontmatter 欄位），不改任何門禁、角色分工或方法論內容。

## 與 ledger-driven-dev 的邊界分工

兩個項目聯合使用時的邊界原則（2026-11-25 拍板）：**「真相與規則」歸 ledger，「人與流程」歸 julia**。判定準繩：凡關於證據語義、門禁口徑、帳本契約、文檔生命週期的能力，在 ledger 側實現並隨其版本升級；凡關於角色行為、工作流編排、操作人溝通、翻譯層的紀律，在 julia-dev 側實現。兩邊不得互相複製實現——接口只交換四類結構化物件（契約／路由／證據／批准包），橋接層（Luca）只轉述契約、不複製事實源。

範例：規範型倉庫自查（術語殘留／版本一致／派生漂移／必備檔案／連結解析）屬「可判定規則」，由 ledger 側 `scripts/spec_check.py` 通用實現；本倉庫僅提供配置 `spec_check.json` 並作為首個使用者接入，不自建第二套檢查器。

**概念唯一聲明點（本體層 v0.1，2026-11-25）**：成員身份、改名史與各平台發行路徑映射，唯一聲明於 `onto/actors.json`（改名史記於 aliases 欄，機械判據不掃描該登記檔）；其餘文件只許引用成員現名，不得另行記述改名史或平台路徑。機械判據由 ledger `spec_check` 的 `ontology_integrity` 判據執行（id 唯一／引用可解析無孤兒／別名不與現名衝突／映射路徑落真）。新增發行形態（如 Hermes）先在此登記映射（`null`=候選未落地），再產出發行檔。v0.1 只凍結「身份與映射」，流程細節仍以各 markdown 為準，避免在概念變動期製造第二失步源。

## 打包分享

```bash
zip -r julia-dev.zip julia-dev/
```

**开发仓与部署副本（2026-11-25 起）**：开发仓位于 `/Volumes/LQVault/RacAIWorkingRoom/CapabilityForge/julia-dev-squad`（source of truth，一切编辑只在此进行；目录名与 GitHub slug 一致）；`~/.workbuddy/plugins/marketplaces/my-experts/plugins/julia-dev` 降级为**部署副本**——平台从这里加载专家（平台路径与插件 id 仍为 `julia-dev`，不改）。副本纪律：**只 pull，不手改**（`git pull --ff-only`；意外手改会以 git status 脏档形式暴露，即视为缺陷走查）。平台注册流程对副本的副作用（如删 settings.json、改 plugin.json）由 spec_check required 判据机械兜底。

**版本发布纪律（2026-11-25 起生效，四件套）**：每个 minor/major 版本随版本号四处声明位更新，同步完成四件事——①打 tag（`v<版本>`）并推送；②创建 GitHub Release（变更摘要 + 对照 ledger 协同版本）；③附安装包 zip（排除 `.git`）；④同步部署副本（marketplace 目录 `git pull --ff-only`，平台加载立即生效）。v1.1.0→v1.10.13 期间未执行此纪律（只有 commit 无发布），自 v1.10.14 起补齐并固化。
