# okf-format — Open Knowledge Format v0.3 格式規範

> 規範來源：`open-knowledge-format/open-knowledge-format`（Apache-2.0，publisher: Google）。本檔為濃縮重述，非原文複製。原始規範：https://github.com/open-knowledge-format/open-knowledge-format/blob/main/SPEC.md 。完整署名見同目錄 `ATTRIBUTION.md`。

## 是什麼

OKF 是一種**供應商中立的知識交換格式**：用純 Markdown + YAML frontmatter 表达知識，任何人（人、agent、导出管线）都能产生，任何工具（静态服务器、Obsidian、LLM、搜索索引、图查看器）都能消费。**只規定格式，不規定運行时、存储或查詢基础设施**；不取代 Avro／Protobuf／OpenAPI 等领域標準，而是与之并存。

## Bundle 結構

一个 bundle 是目錄树，根目錄可用带 frontmatter 的 `index.md` 标识：

```
bundle/
  index.md          # 保留名：目錄列表 + bundle metadata
  log.md            # 保留名：变更历史
  tables/orders.md  # 一个概念 = 一个 .md，frontmatter 有非空 type
  metrics/revenue.md
  references/...    # 跨 Cut 引用的背景文档
```

**概念判定**：`.md` 且 frontmatter 有非空 `type` 才是概念。无 frontmatter 或无 `type` 的 `.md`（README.md、AGENTS.md、SKILL.md）不是概念，不影响 conformance。非 `.md` 是 asset。以 `.` 开头的文件不属 bundle。消费者只读 bundle root 内的路径，不跟随越界符号链接。

## Frontmatter

唯一必填键是 `type`（短字符串，如 `BigQuery Table`、`API Endpoint`、`Metric`、`Playbook`、`Reference`、`Attested Computation`）。未知 type 必须接受，当通用概念处理。

可选：`title`、`description`、`resource`（底层资产的规范 URI）、`tags`。扩展键自由，建议命名 `x-<producer>-<name>`；消费者遇到未知键不得拒绝，修改时必须保留。

時間戳仅接受 RFC 3339（带时区的 date-time，或 full-date 表示该日 UTC 零点）。

## 四大 Families（本格式的真正价值）

### 1. 溯源 `sources`
每条 `{ resource (必填), id, title, author, usage_count, last_modified }`。`resource` 可是可跟随的 URL／bundle 内路径，也可是范围描述符（如「X 项目所有查詢」）。可信度靠**客观信号**而非分数：`author`（权威性）、`usage_count` + `usage_window`（活跃度，只看数量级与趋势）、`last_modified`（新鲜度）。消费者自行推断，OKF 不存分数（主观、不可携、会过期）。

逐条主张归属用脚注，标签 = `sources[].id`：`收入不含税.[^rev-policy]`。禁止用数字标签 `[^1]`——agent 常重写列表，位置会错而 id 不会。

### 2. 信任 `generated` / `verified` 与信任分层
- `generated: { by, at }`：当前内容如何产生、最后实质变更時間（格式／空白／链接修复不改 `at`）。
- `verified: [{ by, at }]`：谁在何时对照來源或资源确认过。可多事件（人工签核 + 夜间进程），仅 `human:` actor 赋予 human-reviewed 層級。
- **current 判定**：`at >= generated.at`（或无 generated）。旧事件留在文件作历史，但不计入。
- **三层信任**（只从 current 事件算）：无 current ⇒ `unverified`；只有非 `human:` ⇒ `machine-confirmed`；有 `human:` ⇒ `human-reviewed`。
- 關鍵纪律：**agent 改写一个已人工审核的概念后，人工审核立即失效**——必须重新确认才算 human-reviewed。信任是建议信号，不是访问控制，未驗證概念仍可用。

### 3. 生命周期 `status` / `superseded_by` / `stale_after`
- `status`：`draft`（未审）／`stable`（默认）／`deprecated`（保留供链接与历史）。未知值不当作 stable。
- `superseded_by`：deprecated 时指向替代概念路径。移动／改名时留一个 deprecated 短概念在新路径，旧链接继续可用。
- `stale_after`：绝对時間点，`now >= stale_after` 即过期。过期意味「需再检查」，不等于内容错误。没有已知复查周期就省略，不臆造。消费者不得把无法解析的值当新鲜。

### 4. 可驗證計算 `Attested Computation`
独立概念（自带信任狀態），字段：`runtime`（必填，如 bigquery／postgres／dbt／python）、`parameters`（`{name, type, required}`，agent 只能填值）、`computation`（计算文件路径或 body 中 `# Computation` 的单个代码块）、`executor`（`resource` 执行说明 + `receipt` 回执字段清单）、`attester`（确定性校验代码路径，无 LLM）。

- agent **只能提供参数值，不得编写或修改计算**。消费者绑定参数产生可执行物；attester 独立再绑定一次，比对回执中的展开后 SQL／编译产物。改写查詢、替换计算文件、改依赖都会失败。
- 缺少 `runtime` 或 `attester` 不得显示为「已驗證」。
- **verified vs attestation**：`verified` 确认定义仍符合政策（对文档、慢、記錄在 bundle）；attestation 确认某次運行按核准方式产生值（对每次调用、運行时、不記錄）。两者缺一不可。

## Conformance 要点

消费者必须：解析两种 bundle 内路径形式；不读越界路径；不把 index/log 当概念；不拒绝未知键与未知 type；不因可选字段缺失而拒绝；只用 current 事件算信任；展示失败的 attestation 而非静默丢弃。null／空串／空列表等同缺键；列表字段接受单值当单项（scalar `tags` 是一个标签，不按逗号拆）。

`index.md` 提供渐进式导航（逐层查看，不必一次载入整个 bundle）；`log.md` 記錄按時間排序的变更。

## 與其他 Skill 的分工

- `llm-knowledge-base`：管**如何从文章萃取**场景／概念／实体（生产方法论）。
- `okf-format`：管**知識如何持久化、交換与取信**（格式与信任契约）。
- `okf-generate` / `okf-consume`：分别管写入与读取的操作流程。

四者可串联：llm-knowledge-base 萃取 → okf-generate 写成合规 bundle → okf-consume 带信任报告地回答。
