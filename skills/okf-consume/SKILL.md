# okf-consume — 從 OKF Bundle 可信問答

> 方法論來源：`open-knowledge-format/open-knowledge-format` 的 `okf-consume` Skill（Apache-2.0，publisher: Google）。本檔為濃縮重述，非原文複製。原始 repo：https://github.com/open-knowledge-format/open-knowledge-format 。完整署名見同目錄 `ATTRIBUTION.md`。

## 何時使用

使用者指向一个 OKF bundle（或有 `index.md` 与 frontmatter `type` 的 Markdown 目錄），询问指标／表／政策／流程的定义、询问由 Attested Computation 定义的数值、或询问哪些概念过期／废弃／未驗證。由知識管理師（knowledge-curator）主導。

**只讀不寫**：建立、修改、修復、遷移、驗證 bundle 改用 `okf-generate`。

## 五條鐵律

1. **只從 bundle 回答**：bundle 未覆盖就明说；任何来自通用知識的陈述要标注「一般知識」。
2. **回報信任**：每个使用的概念都要报告其信任分层、status 与是否 stale。
3. **不自己寫計算或 executor**：Attested Computation 只提供参数值，不编写或改动查詢，严格执行 bundle 给定的 executor。
4. **不拒絕內容**：未知键、未知 type、缺少可选栏位、断链都要照用（规范 §11.2）。
5. **不改動 bundle**。

## 程序

### 1. 找 bundle root
找带 frontmatter 的 `index.md`，它标出 root（即使 bundle 是大 repo 的子目錄）。读 `okf_version`、`title`、`description`（description 说明范围与使用时机，多个 bundle 时据此选择）。无 root index 就用最上层 `.md` 带 `type` frontmatter 的目錄。`okf_version` 非 0.3 时尽力而为读取，并在回答中注明版本差异。

### 2. 找相關概念（不要一次讀完整個 bundle）
两种做法：扫描脚本（原始 Skill 的 `scripts/scan.py`，可列每个概念的 ID／type／信任分层／status／新鲜度，并支援 `--type`／`--tag`／`--grep`／`--current`／`--stale`／`--deprecated`／`--unverified` 过滤；本专家包不内嵌此脚本，可自行实现等价扫描）；或逐层读 `index.md`，只读相关目錄。找到候选后再看同主题的其他概念，检查冲突。

### 3. 讀每個概念
先读 frontmatter（type、title、description、resource、tags 与信任／生命周期栏位），再读 body（定义、`# Schema`、`# Examples`、`# Computation`）。跟随与问题相关的链接（定义、关联、政策、计算）。路径栏位依 `okf-format` 的规则解析，不读越界路径。断链当「知識缺失」处理，不当错误。

### 4. 判斷信任與新鮮度
- **信任分层**：只用 current 事件（`at >= generated.at`，或无 generated）。无 ⇒ unverified；只有非 `human:` ⇒ machine-confirmed；有 `human:` ⇒ human-reviewed。若所有事件都早于最后变更，明说「仅在最后变更前驗證过」。
- **status**：缺 `status` 即 stable。`draft` 要标明草稿；`deprecated` 不当作现行知識，跟随 `superseded_by` 找替代（无则从链接与 body 找，并说明做法）；其他值显示原始值且不当作现行。
- **新鮮度**：`now >= stale_after` 即过期（date 表示当日 UTC 零点）。说明何时开始过期。无法解析视为过期并指出值异常。过期意味「需再检查」，不等于错误。
- **來源**：用可信度信号权衡冲突主张——`author` 看权威性、`usage_count` + `usage_window` 看活跃度（只比数量级）、`last_modified` 看新鲜度。这些是事实不是分数。

### 5. 處理可驗證計算
若数值由 Attested Computation 定义：只读契约与计算，只提供参数值，按 executor 执行；取得回执后由 attester（确定性、无 LLM）校验。**attestation 失败就要显示失败或不出示数值，不得静默丢弃**。`now >= stale_after` 显示警告或不出示值。驗證成功时显示裁决（如 job log 链接），让信任可见。

### 6. 組織回答
先给结论，再附每个使用的概念的信任摘要：`概念 · 信任分层 · status · 新鲜度 · 來源数`。冲突主张并列呈现并说明权衡依据。bundle 未覆盖的部分明确标注范围不足。

## 與團隊協作

知識管理師主導查詢并产出信任摘要；Vera（qa-engineer）复核 attestation 裁决与过期判断。回答中的技术主张若来自 `codebase-reverse` 或 `ontology-modeling` 产物，应同时标注原产物路径。
