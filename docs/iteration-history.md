# julia-dev 開發迭代史

本檔記錄專家包的**開發過程與迭代來源**：每一輪進化從哪裡來、由誰拍板、解決什麼問題。逐條變更的精確記錄（版本／日期／證據指針／裁決）見 [`evolution-log.md`](evolution-log.md)；本檔是其敘事版。

## 迭代來源的四個渠道

julia-dev 的所有進化都來自以下四個渠道之一，且一律走「提案 → Ed 複核 → 人拍板 → 主理人執行 → commit」的受控回路：

1. **使用者拍板**——方向性需求（自我進化機制、操作人模式、多平台適配、命名規則）
2. **缺口評估走查**——定期以特定視角（協作接縫、門外漢旅程、ledger 結合）全文走查，找斷點與接縫
3. **實測回灌**——真實專案（如 Workflow U smoke test）踩到的坑，制度化寫回 Skill
4. **外部開源吸收**——13 個開源專案的方法論濃縮重述（清單見 README「致謝」節）

## 版本時間線

### 包建立期（v1.0 – v1.8.x）

- 專家團骨架成型：Julia 主理人＋十位成員，21 條 Workflow，19 套 Skill
- 外部方法論分批吸收：sharptoolbox 系（ontology-modeling／ontology-driven-dev／codebase-reverse／visual-model／consulting-html-ppt／llm-knowledge-base）、OKF（Google）、pstack（Lauren Tan）、cursor/plugins 系（orchestrate／ralph-loop／cursor-team-kit／thermos／dyl-stack／advisor／cli-for-agent）
- v1.8.0：新增第十一位成員 Luca（帳本對接官）與 `ledger-bridge` Skill，接通 [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev) 的治理能力；對接方案經評估後確定為「只讀薄橋」，ledger 倉庫零改動

### v1.9.0 接縫修補

協作落地後的缺口再評估發現，問題已從「能力不足」轉為「接縫與可運行性」。補上五項機制：足跡規範、契約唯一入口、PASS 分級、解阻（Andon）、Preflight。

### v1.9.1 實測回灌

Workflow U smoke test 在 `/tmp/julia-smoke` 實跑，踩到四個坑並制度化回灌：先跑生成器再 verify、測試放 `tests/unit/` 且補 `__init__.py`、網關動作固定枚舉、deny 附 fix 指引。**能力碼 SMOKE.API.QUERY.01 成功升到 tier=verified／binding=bound。**

### v1.10.0 – v1.10.2 制度化期

- **v1.10.0**：P1 缺口三項——AI 評估雙基線、系統級安全清單六項、環境腳本有主
- **v1.10.1**：成員名統一英文化（390 處）
- **v1.10.2**：建立**受控自我進化機制**——成員提案（重複 ≥2 次才夠格）→ Ed 唯讀複核 → 人拍板（唯一生效門）→ 主理人執行 → commit → 進化日誌登記；一次生效 = 一個 commit，天然回滾點

### v1.10.3 – v1.10.5 可用性期

- **v1.10.3**：規劃期第一性原理分解——Remy 需求標註「硬約束／慣例」歸類、Archie 設計文件必含「基本事實表」、Julia 增設第一性原理門
- **v1.10.4**：**操作人模式三檔**（門外漢／標準／專家）——Phase 0 聲明、隨時切換；模式改變介面不改變治理
- **v1.10.5**：門外漢五護欄——模式探測、代勞決策清單、人話交接卡、快捷回覆提問、「感覺不對」有效信號通道

### v1.10.6 – v1.10.8 發行與治理期

- **v1.10.6**：補根目錄 MIT LICENSE＋README 集中致謝節（13 項來源總表）
- **v1.10.7**：**多平台發行層**——`scripts/build_dist.py` 從 canonical 生成四平台發行包（Claude Code 完整團隊／通用 AGENTS.md solo／Cursor／VS Code Copilot）；dist 永遠腳本重建，不手改
- **v1.10.8**：ledger 結合再評估六修補——solo 總綱補帳本對接帽、Preflight 加綁定預檢（三坑）、Phase 4 必經 `run_tests.py` 產證、接手必重跑 Preflight、門外漢人話批准卡、進化提案加 ledger 契約影響檢查、Luca 經驗對照進化觸發器

### v1.10.9 – v1.10.10 命名與文檔期

- **v1.10.9**：三位成員改名對齊巧思單詞前兩字母（Remy／Mark／Knox，舊名映射見進化日誌 v1.10.9——該日誌是舊名的唯一合法記錄地）；全詞替換 101 處（53 處 ASCII 邊界＋48 處 CJK 相鄰，第二輪修復了 Python `\b` 把漢字視作詞符導致的漏換）
- **v1.10.10**：文檔補全——本檔（迭代史）、README 多語言（English／简体中文）、語言切換入口

### 2026-11-26 收斂（工作樹改動，未升版）

- **多語言介紹移除**：項目尚未定型，移除 README 多語言介紹（English／简体中文）與語言切換入口，只保留單一 README；變動記入進化日誌。

## 工程紀律（貫穿全程）

- **canonical 單一事實源**：WorkBuddy 包是唯一改動入口；`dist/` 由腳本原地重建
- **一次生效 = 一個 commit**：所有進化有 git 回滾點
- **門禁不隨模式與平台放鬆**：不可逆門禁、測試門、Ed 複核在任何形態下保留
- **改寫只做語義等價**：跨平台轉換、外部方法論濃縮重述，均不改變治理語義；外部專案保留完整署名

## 歷史經驗教訓（已制度化）

| 教訓 | 制度化去向 |
|------|-----------|
| 全新骨架需先跑生成器再 verify | ledger-bridge Preflight 第 0 步 |
| 測試放 `tests/unit/`＋`src/` 補 `__init__.py`＋sys.path 深度 | Preflight 綁定預檢（v1.10.8） |
| `agent_gateway --action` 是固定枚舉 | ledger-bridge 網關實測紀律 |
| Python `\b` 對 CJK 相鄰文本不產生詞邊界 | 改名工具須用 ASCII 環視（本檔記錄，供未來批量文本操作參考） |
| `settings.json` 註冊腳本副作用 | 註冊後必查 `ls settings.json` |
