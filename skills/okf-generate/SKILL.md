# okf-generate — 建立與維護 OKF Bundle

> 方法論來源：`open-knowledge-format/open-knowledge-format` 的 `okf-generate` Skill（Apache-2.0，publisher: Google）。本檔為濃縮重述，非原文複製。原始 repo：https://github.com/open-knowledge-format/open-knowledge-format 。完整署名見同目錄 `ATTRIBUTION.md`。

## 何時使用

建立、更新、遷移、修復、驗證 OKF bundle；把資料表、資料集、指標、API、政策、維運手冊寫成 OKF 概念；補齊溯源／信任／生命週期／可驗證計算欄位。由知識管理師（knowledge-curator）主導。

只讀取或問答時改用 `okf-consume`；格式細節見 `okf-format`。

## 六條鐵律

1. **只寫有來源支持的事實**：不編造欄位、分區、URL、負責人、數字、政策或審核日期。無來源就省略或問使用者。
2. **記錄溯源**：每個概念列 `sources`，每個具體主張用腳註（標籤 = `sources[].id`）指向來源。
3. **誠實記錄作者**：`generated.by` 寫自己的 actor `<tool>/<model>`。
4. **不冒充驗證**：本次生成的内容不得加 `verified`；`human:<id>` 只有在本人明確確認並提供 id 时才可寫，不得從登入名或 git 設定推斷。無 id 就不寫並說明原因。
5. **不自己寫可驗證計算的公式**：只能從核准來源（核准 SQL 檔案、dbt model、owner 提供的查詢）逐字複製並註明來源。無核准計算就只描述指標並回報缺口。
6. **保留不屬於自己的內容**：更新時保留未知鍵、`verified` 歷史與人类撰寫文字，不重寫未變更的值。

## 程序

### 1. 界定範圍
找到或選定 bundle root；若已存在先讀 root `index.md` 與 `log.md`，記下 `okf_version`。列出可讀來源（schema metadata、OpenAPI、文件頁、runbook、使用者筆記），並明確告知哪些來源讀不到。範圍不清就提問。

### 2. 規劃目錄
一个概念一个檔案，概念 ID = 不含 `.md` 的路径。依种类分组（`datasets/`、`tables/`、`metrics/`、`computations/`、`policies/`、`playbooks/`、`references/`），沿用既有目錄名。用稳定的小写档名，不得有仅大小写不同的两条路径。不得命名为 `index.md` 或 `log.md`。**超过 10 个檔案先向使用者展示目錄树再动手**。

### 3. 寫每個概念
档首正好一行 `---` 结束 frontmatter。`type` 用简短描述名并沿用既有命名。`description` 一句话。资产类设 `resource` 为规范 URI。`tags` 用 YAML list。時間戳用 RFC 3339 date-time（带 offset）；只有 `stale_after` 等可用 date（表示该日 UTC 零点）。內文先 1–3 段说明概念、粒度、用途与注意事项，再用惯例标题 `# Schema`／`# Examples`／`# Computation`。

### 4. 連結與路徑
本文內的連結用相对路径（如 `../tables/orders.md`，在 GitHub 可直接点击）；路径栏位（`resource`、`sources[].resource`、`computation`、`executor.resource`、`attester.resource`、`superseded_by`）用前导 `/` 从 bundle root 解析。含空格要 percent-encode。只連結确实存在或本次会建立的檔案。

### 5. 溯源、信任與生命週期
每个 `sources` 条目给稳定 `id`、必填 `resource`、`title`；可信度信号（author／usage_count／last_modified）只在有真值时填写，`usage_count` 要配 `usage_window`。具体主张用脚注引用。每次实质变更更新 `generated`（纯格式修复保留原值）。actor 写成 `<producer>/<version>` 或 `<scheme>:<id>`，scheme 有 `human:`／`team:`／`process:`，只有 `human:` 赋予 human-reviewed。正常内容省略 `status`（即 stable）；未完成设为 `draft`；退役保留檔案设 `deprecated` 并加 `superseded_by`；移动／改名保留 generated 与 verified，于旧路径留 deprecated 短概念。`stale_after` 只在來源有明确复查周期时填写。

### 6. 寫可驗證計算
仅在有核准計算時执行。每个计算独立一个 `type: Attested Computation` 概念，填 `runtime`、`parameters`、`computation` 或 body 中单个 `# Computation` 代码块、`executor.resource`／`receipt`、`attester.resource`。引用它的指标概念用普通 Markdown 链接指向计算概念。**绝对不自行编写计算公式**。

### 7. 驗證
完成後检查：frontmatter 全为合法 YAML mapping；无重复键；保留名未被当概念；路径不越界；每个具体主张有对应來源 id；无冒充的 verified；信任分层可从 current 事件重算；过期值可解析。产出符合性报告。

## 與團隊協作

知識管理師主導寫入；維拉（qa-engineer）独立驗證信任分层、时效与 attestation 契约；麦克（engineer）负责把 `llm-knowledge-base` 萃取的三层模型转成 OKF 概念草稿，由知識管理師依本 Skill 补齐溯源与信任栏位。主理人不得代写任何概念或驗證结论。
