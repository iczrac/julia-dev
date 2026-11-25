# 主理呀开发团 (Julia Dev Squad)

> **语言 / Language**：[繁體中文](../README.md) · [English](README.en.md) · 简体中文（本档）

团队名取自主理人Julia的谐音「主理呀」——先辨析任务、再编排流程、最后交付。英文保留 Julia 作为花名，改用 Squad 强调这是一支团队，也避免被误读为 Julia 程式语言开发。

由Julia统筹的全方位软体开发专家团。不论是源码逆向、从零建置、加功能、修 bug、重构、审查、迁移、串接第三方、数据／AI 应用或交付简报，都会先辨析任务类型，再调度最合适的团队流程交付。

## 类型

Team 型（多角色协作团队）· 版本 1.10.12 · 11 位成员

## 成员与命名巧思

| 成员 ID | 名字 | 职业 | 巧思 |
|---------|------|------|------|
| julia-dev-team-lead | Julia | 交付总监 | 谐音「主理呀」——主理人 |
| product-manager | Remy | 产品经理 | req（requirement）需求——取 re 起首 |
| architect | Archie | 架构师 | arch（architecture）架构 |
| engineer | Mark | 工程师 | make——动手造东西的人（取 ma 起首） |
| qa-engineer | Vera | 品质保证工程师 | verify——验证的化身 |
| reverse-engineer | Tracey | 逆向工程师 | trace——追溯源码，从入口追到资料库 |
| delivery-designer | Della | 交付设计师 | deck／deliver——做出可放映的交付简报 |
| knowledge-curator | Knox | 知识管理师 | know——知识的守护者（kn 起首；Fort Knox 金库意象，管溯源、信任与时效） |
| release-engineer | Ship | 发布工程师 | ship——把验证过的东西安全送上线的人 |
| decision-advisor | Ed | 决策顾问 | advisor——在昂贵或不可逆之前被找来的第一个反对者 |
| ledger-liaison | Luca | 帐本对接官 | route＋task card——把 ledger 的路线卡翻成 Julia 的任务 |

## 任务类型与流程对照

主理人Julia会先做 **Phase 0 任务辨析**，再从 21 条 Workflow 中选一条；不需要的阶段直接略过，不浪费流程。

| 你说的话 | 任务类型 | 启动流程 |
|---------|----------|----------|
| 做一个工具／网站／API | 全新开发 | A 完整交付 |
| 需求很乱，帮我写 PRD | 需求梳理 | B 需求梳理 |
| 帮我 review 程式码 | 审查健检 | C 健检／G 安全审查 |
| 在现有系统加一个功能 | 功能增强 | D 功能增强 |
| 这里报错／结果不对 | 缺陷修复 | E 缺陷修复 |
| 太慢了／帮我重构 | 重构优化 | F 重构优化 |
| 补测试／提高覆盖率 | 测试补齐 | H 测试补齐 |
| 升级版本／换框架 | 迁移升级 | I 迁移升级 |
| 串接支付／登入／地图 API | 第三方整合 | J 第三方整合 |
| 爬虫／RAG／LLM 应用 | 数据 AI | K 数据／AI 应用 |
| 用本体驱动做 XX 管理系统 | 本体驱动 | L 本体驱动端到端 |
| 接手旧专案／盘点程式码 | 源码逆向 | M 源码逆向 |
| 做成简报／方案汇报 | 交付叙事 | N 交付叙事简报 |
| 画架构图／知识图谱 | 可视化建模 | O 多视角建模 |
| 建立知识库／这个数字可信吗 | OKF 知识管理 | P OKF 知识管理 |
| 先重现再修／证明真的可用 | 严谨工程 | Q pstack 严谨工程 |
| 合并 PR／接手上一轮／我要睡觉 | 发布接续 | R 发布与会话接续 |
| 拆并行任务／跑有界循环／让 CI 全绿 | 结构化编排 | S 结构化编排与有界循环 |
| 深度 review PR／安全＋可维护性双轴 | 深度差异审查 | T 深度差异审查与决策复核 |
| 找盲点／卡两次／交付前再确认 | 决策复核 | T 或直调Ed |
| 对接 ledger／照帐本路由走／从 next_queue 拿任务 | 帐本对接 | U 帐本对接与受控写入 |
| 用什么技术比较好 | 技术咨询 | B 或直接问Archie |

## 适用专案型态

Web 前端、后端 API、全端应用、CLI／自动化脚本、桌面应用、行动应用、资料处理、AI／LLM 应用、资料库设计、DevOps／部署。

每种型态都有对应的设计与验证重点，会由主理人在派工时明确写给团员，例如 API 重契约与错误码、AI 应用重幻觉防护与成本、CLI 重幂等性与输出格式。

## 选配方法论：本体驱动建模

Expert 包内建 `skills/ontology-modeling/`，吸收自开源框架 [ontology_modeling_framework](https://github.com/sharptoolbox/ontology_modeling_framework)（作者 @人月聊IT，Apache-2.0）。它把业务系统切成**正交、可独立演进、可用 YAML 承载**的模型关切，建立「需求 → 设计 → 程式码」的可追踪链。

**何时启用**（由Archie在 Phase 2 载入）：

- 中大型业务系统（ERP／CRM／审批／合同管理）
- 规则密集、跨物件联动多、需要稽核溯源
- 需要稳定交接契约的多角色协作

**何时不启用**：小工具、纯前端、一次性脚本、探索性 AI 应用——避免过度工程。

**版本选型**：v9（7 模型，单体同步，最适合 AI 稳定出码）用于实际落地；v6（11 模型，含事件／介面／持久化映射）用于理解全貌与复杂整合。

方法论已接入五位成员：Remy标注验收对应的操作功能点、Archie产出正交模型、Mark做模型到程式码映射、Vera做追溯门禁验证。完整方法论见 `skills/ontology-modeling/SKILL.md`，署名与授权见同目录 `ATTRIBUTION.md`。

## 选配管线：本体驱动端到端开发

第二个 Skill `skills/ontology-driven-dev/` 吸收自 [ontology-driven-dev](https://github.com/sharptoolbox/ontology-driven-dev)（MIT，Copyright 2026 sharptoolbox），补上建模前后两段：

- **需求探索八阶段**：总体理解 → 业务对象 → 功能与规则 → 跨对象联动 → 协同审批流 → 查询报表 → 角色权限 → UI 原型
- **人工确认门禁**：每阶段用固定格式提问并硬暂停等确认；A 类自动补全、B 类（企业专属）必须确认，有 `[待确认]` 不得标记完整
- **10 步构建流水线**：从七模型 YAML 到 DDL、服务层、权限、流程引擎、页面路由、AI 对话框（含唯读 SQL 安全边界）、全链路联调与验收

触发方式：直接说「帮我开发一个 XX 管理系统」或「做本体驱动开发」，主理人会走 **Workflow L**：Remy需求探索和人工确认 → Archie七模型 → Mark构建 `code-app/` → Vera追溯验收。

两个 Skill 分工：`ontology-modeling` 管建模细节，`ontology-driven-dev` 管端到端管线与工程落地。技术底座原始码不内嵌，使用时从原始 repo 取得。

## 新增能力：逆向、可视化、简报与知识库

本版从 sharptoolbox 其余仓库再吸收四套方法论，全部做成**选配 Skill**，需要时才载入：

| Skill | 来源／授权 | 何时用 | 主责成员 |
|-------|-----------|--------|----------|
| `codebase-reverse` | [codebase-reverse](https://github.com/sharptoolbox/codebase-reverse) · MIT | 接手旧系统、迁移前置盘点、补写需求文件 | Tracey（逆向）＋Vera（覆盖对帐） |
| `visual-model` | [visual-model](https://github.com/sharptoolbox/visual-model) · CC BY 4.0 | 交付级架构图、SysML 五视图、知识图谱 | Archie |
| `consulting-html-ppt` | [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) · 未宣告授权 | 方案汇报、验收简报、可放映交付材料 | Della |
| `llm-knowledge-base` | [LLM-knowledgeBase](https://github.com/sharptoolbox/LLM-knowledgeBase) · MIT | RAG 知识萃取、来源约束问答 | Mark＋Vera |

### 完整融合：Open Knowledge Format（OKF）

逆向文件、架构决策与指标定义最大的风险是**默默过时**——档案还在，但已不可信。本版完整引入 [open-knowledge-format](https://github.com/open-knowledge-format/open-knowledge-format)（Apache-2.0，publisher: Google，v0.3）的三套 Skill：

| Skill | 职责 |
|-------|------|
| `okf-format` | v0.3 格式规范：bundle 结构、frontmatter、溯源、信任分层、生命周期、可验证计算 |
| `okf-generate` | 建立／更新／迁移／修复／验证 bundle 的六条铁律与程序 |
| `okf-consume` | 只读问答，逐概念回报信任分层、status、新鲜度与来源 |

新增第八位成员**Knox（知识管理师）**主导 OKF 写入与查询，Vera独立覆核信任分层与 attestation。

**三个补上缺口的机制**：

- **信任分层**：unverified／machine-confirmed／human-reviewed。关键纪律是「AI 改写已人工审核的概念后，人工审核立即失效」——这正是多智能体协作最容易自欺的地方。
- **stale_after 时效**：用绝对时间点判定过期，可机械比较；没有已知复查周期就省略，不臆造日期。
- **可验证计算**：agent 只能填参数、不能改公式；consumer 用确定性 attester 比对回执。这把幻觉防护从提示词纪律升级为机械契约，也让Vera的 `PASS/FAIL` 有可计算的依据。

`llm-knowledge-base` 与 OKF **明确分工**：前者管「如何从文章萃取场景／概念／实体」，后者管「知识如何持久化、交换与取信」。Mark萃取后交给Knox补齐溯源与信任栏位，不重复做同一件事。原始 repo 的 Python 脚本不内嵌，署名见各 Skill 的 `ATTRIBUTION.md`。

### 严谨工程与可验证交付：pstack

本版吸收 [cursor/plugins 的 pstack](https://github.com/cursor/plugins/tree/main/pstack)（作者 Lauren Tan，MIT，19k stars）——这是 Cursor 官方插件库中最受欢迎的插件之一，核心主张是「想快就先深入」「写更少但更好的程式」。四套 Skill 各自职责：

| Skill | 职责 |
|-------|------|
| `pstack-principles` | 24 条工程原则（核心／架构／验证／委派／后设），回答「怎样才算做好」 |
| `pstack-playbooks` | 22 个 playbook 路由，展开 bug fix、perf、feature、shipping、session pickup 等关键流程 |
| `pstack-verification` | 证明它可行、基准检验七问、建立专案本地验证 Skill、形式化验证、把错误钉进结构 |
| `pstack-parallel-review` | swarm（分割／竞速）、arena（竞技与移植强项）、interrogate（对抗式审查，只留跑过的发现） |

新增第九位成员**Ship（发布工程师）**：Vera判定对不对，Ship负责让对的东西安全落地——独立验证每个 PR、只合并从底部起连续通过的区段、用 `git patch-id` 核对 rebase 前的裁决是否仍有效、落地期间不碰分支、停在上限。

**三个最值得吸收的纪律**：

- **每行程式码追溯到执行期证据**：bug fix 必须先重现、二分法找根因，「可能有用」的防护是假设不是修复，证据反驳就回退。
- **基准检验七问**：说出限制因子、确认对等调校、做数量级算术、计数错误、交替跑五次以上、量端到端、确认工作真的发生了。过不了就标 inconclusive，不宣称加速。
- **对抗式审查只留跑过的发现**：没有指令输出证明的问题（含风格、命名、结构）一律丢弃；共享根因合并；「没有发现」是有效结果。

**与既有能力的分工**：`ontology-modeling` 查需求到程式码的对应、`pstack-verification` 查实际跑起来的行为、OKF attestation 查计算回执是否被窜改——三者互补。CI 专属的模型设定与插件依赖没有内嵌，署名见各 Skill 的 `ATTRIBUTION.md`。

**门禁冲突的处理**：pstack 主张「可逆工作不要问人」，本团队的优先序是人工确认门禁 > Vera `PASS` > 不可逆动作确认 > 其余可逆工作直接做。

**设计取舍**：

- **逆向是全量、深度可分层**：Tracey先建立源码资产台帐（B0–B9），再逐功能穿透到资料库；Vera独立做覆盖对帐，未归属资产不放行。基线不全量就写功能清单，是逆向最常见的失败模式。
- **简报忠于事实**：Della的页面可以有四种形态（真实图表／架构图／结构模型／文本分类），但不得虚构数据，且每个技术主张要标注来源。Vera未给 `PASS` 前不开始制作。
- **授权分寸**：前三个有明确授权的专案仅浓缩重述并保留完整署名；`consulting-html-ppt` 原 repo **未宣告开源授权**，因此只吸收方法论要点，不复制其模板库、图标或成品，使用平台内建或自制模板替代。各 Skill 的 `ATTRIBUTION.md` 均保留来源与授权说明。

## 再进化：cursor/plugins 其他高价值专案

本版再扫描 [cursor/plugins](https://github.com/cursor/plugins/tree/main) 全库，挑出四组对多智能体软体交付真正有增量的做法，全部转成**选配 Skill**；Cursor 专属的 SDK、Bun 脚本、hooks 与 Slack 整合一律不内嵌，只保留可移植的方法论。

| 新 Skill | 吸收来源 | 做什么 | 主责成员 |
|---------|---------|-------|---------|
| `structured-orchestration` | `orchestrate`＋`ralph-loop`＋`cursor-team-kit/loop-on-ci`（MIT） | Planner／Worker／Verifier 职责边界、逐字交接、五级 verifier 证据、完成承诺＋迭代上限、失败模式与 Andon、`gh pr checks` CI 回圈 | Julia（编排）＋Ship（CI） |
| `deep-diff-review` | `thermos`＋`dyl-stack`（MIT） | 正确性／安全与结构／可维护性双轴平行审查、code judo／1k 行／spaghetti 尺标、去重后最多 7 则可贴 comment 与 🟢／🟡／🔴 | Vera＋Archie，Ed复核重大发现 |
| `decision-gates` | `advisor`＋`dyl-stack`（MIT） | 重大决策／卡两次／完成前四类检查点、唯读 `Verdict / Why / Recommendations / Risks / Answers / Confidence`、The Algorithm、根因句、合并与 taste veto 纪律 | Ed |
| `agent-friendly-cli` | `cli-for-agent`（MIT） | 非互动 flag、分层 help 与范例、stdin／pipeline、可行动错误、幂等、`--dry-run`、JSON 输出与退出码 | Mark＋Archie |

新增第十位成员**Ed（决策顾问）**：他不写程式、不开 PR、不合并，只在昂贵或不可逆之前给第二意见。他的建议不能覆盖人工确认门禁、Vera `PASS` 或不可逆动作确认——这是本团队刻意设定的优先序。

**四个最值得吸收的纪律**：

- **Planner 不写程式，Worker 不互联，Verifier 不改目标原始码**。`orchestrate` 用逐字 handoff 取代共享状态，让平行任务可以收敛而不靠全域协调；下游需要上游资讯就宣告依赖，由主理人转交。
- **完成要有承诺与上限**。Ralph Loop 的同一提示词反复迭代、只能在工作真的完成时输出承诺；到上限就如实回报未完成，防止 agent 为了结案说谎。Verifier 的 `verifier-blocked` 也禁止把环境故障伪装成通过。
- **深度审查要双轴、要只骂 diff、要少而准**。Thermos 把 bug／安全／devex／feature gate 与可维护性分开；dyl-stack 把发现压缩成最多 7 则可贴 comment 与一个灯号，且永远不贴到 PR、不 approve、不合并。
- **先问需求、先删除、再优化**。`The Algorithm` 与 `Root cause: X because Y` 补上 pstack 的根因纪律：null guard、retry、sleep、skip、snapshot 更新在根因句成立前都只是症状修复。

**没有吸收的部分**：`orchestrate` 的 Cursor SDK／Bun CLI／Slack Andon 脚本、`ralph-loop` 的 hooks、`advisor` 的模型绑定与 state 档、`thermos` 的 subagent 定义、`dyl-stack` 的 Figma／UI judge 流程——这些都绑定特定平台或工具，移植成本高于收益；`agent-compatibility`、`continual-learning`、`workflow-from-chats` 的洞察已分别被既有验证、知识管理与偏好沉淀机制覆盖，不重复造一套。

## 选配协定：ledger-driven-dev 帐本桥接

第十一位成员**Luca（帐本对接官）**与第十八套 Skill `ledger-bridge`，把 [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev)（MIT，Copyright 2026 Ledger-Driven Dev contributors）的治理能力接进 Julia 的执行链。这不是把两边合并，而是一层**只读薄桥**：

| 交接物件 | 用途 |
|---------|------|
| `intent.json` | 把人话需求、非目标、能力码与写入范围变成可校验意图 |
| `route.handoff` / `next_queue` | 取得唯一专家、交接链与单张任务卡 |
| `test_report` + `verify_ledger` JSON | 把Vera的证据换算成 `declared / verified` 与不变量结果 |
| `approval_bundle` / `audit` | 只准备待批准命令，由人工签核、Ship执行 |

**ledger-driven-dev 仓库本身零改动**：不改 schema、不改 31 条不变量、不加新专家、不复制 24 个 Skill。需要在目标专案做的是一次性的治理接入：能力码、`verify_ledger`、Agent 注册与测试证据绑定。

门禁优先序：**人工确认 > ledger 写入门禁 > 不可逆动作确认 > Vera `PASS` > 其余可逆工作**。Luca只读、只翻译、只准备；不得带 `--apply` 执行写入，也不得把 ledger JSON 复制成 julia-dev 内的第二份事实源。方法论浓缩见 `skills/ledger-bridge/SKILL.md`，授权见同目录 `ATTRIBUTION.md`。

## v1.9.0：接缝修补

协作落地后的缺口再评估发现，问题已从「能力不足」转为「接缝与可运行性」。本版在不加成员、不加 Workflow 的前提下补上五项机制：

| 机制 | 解决的缺口 | 落点 |
|------|-----------|------|
| **足迹规范（footprint）** | 三处引用足迹却无格式、无落点、无责任人 | 主理人 SOP「足迹规范」＋Vera／Ship／Ed MD |
| **契约唯一入口** | `intent.json` 与Julia任务契约双写，谁为准未定 | Phase 0.5＋Workflow U＋ledger-bridge 硬规则 8 |
| **PASS 分级** | 聊天式 `PASS` 与 ledger `verified` 混用导致含金量通胀 | Phase 4＋ledger-bridge 硬规则 10；治理专案一律 `verified-PASS` |
| **解阻（Andon）** | fail-closed 一路「停」，但停了之后无恢复路径 | ledger-bridge「解阻」节＋严禁行为；卡两次必须向使用者 Andon |
| **Preflight** | 桥接命令依赖目标专案安装的 ledger 脚本，版本漂移无前置检查 | Phase 0.5＋Workflow U 前置＋ledger-bridge「Preflight」节 |

足迹与 ledger、OKF 的分工固定为：**ledger＝专案事实源，OKF＝外部知识可信层，footprint＝当前工作现场草稿**；三者不互相复制，足迹只引用前两者。

## 进化机制：受控自我进化

成员是每次会话临时 spawn 的执行者，没有跨会话记忆——真正能进化的载体只有专家包文件本身。因此进化不采用自由自我修改，而是六步回路：**成员提案（重复 ≥2 次才够格）→ Ed 唯读复核 → 人拍板（唯一生效门）→ 主理人执行修改 → validate＋register＋git commit → 进化日志登记**。

- 提案固定七段格式，必须附可验证证据；规则修改采合并替换不堆叠
- 禁区（严禁行为、门禁优先序、成员边界、四类交接对象）只能由人主动修改，成员不可提案
- 一次生效 = 一个 commit，天然回滚点；变更史见 `docs/evolution-log.md`，回路规则见 `skills/self-evolution/SKILL.md`

## 功能

- **任务路由**：先辨析类型与专案型态，再选流程；修 bug 不会被逼著写 PRD
- **结构化交接**：阶段间以 PRD／设计文件／变更摘要／测试报告交接，不靠口述
- **增量安全修改**：既有系统改动先做影响分析，保留向后相容
- **多型态验证**：Vera（QA）依 Web／API／数据／AI 调整测试方式，修改类任务必做回归
- **明确品质关卡**：Vera给出 `PASS`／`FAIL` 与证据，主理人不得代写或软化结论
- **人工确认门禁**：Workflow L 的需求探索逐阶段提问并暂停等确认，杜绝 AI 自行假设企业专属规则
- **源码逆向**：Workflow M 全量基线＋功能穿透链＋覆盖对帐，把隐藏功能与资料库映射一并挖出
- **交付叙事**：Workflow N 把验证通过的成果做成动作式标题的单档 HTML 简报
- **可信知识**：Workflow P 的 OKF bundle 让每个概念都带来源、信任层级与时效，拒绝静默过时
- **严谨工程**：Workflow Q 以执行期证据取代自我回报，Workflow R 只落地通过验证的连续区段
- **结构化编排**：Workflow S 用 worker／verifier 交接与有界循环推进大型任务，CI 以 `gh pr checks` 为准
- **深度差异审查**：Workflow T 双轴审查 diff，只输出最多 7 则可贴 comment 与一个灯号，不贴 PR、不 approve
- **决策第二意见**：Ed在重大决策、卡两次与完成前给唯读判决，并用 The Algorithm 与根因句挡掉症状修复
- **帐本对接**：Workflow U 用Luca串接 ledger 的复述门、专家路由、任务卡、证据分级与受控写入，避免双重路由与第二事实源
- **AI 评估双基线**：Workflow K 进入实作前固化 golden set、版本号与成本预算，Phase 4 必须「效果＋成本」一起交付，缺一即 FAIL
- **系统级安全清单**：上线前由Vera跑 secrets／依赖许可证／PII／权限／威胁建模／无障碍六项检查，🔴 未释清Ship不得落地；威胁建模摘要是Archie设计文件的必含节
- **环境脚本有主**：launch／doctor／drive／evidence 等环境与取证脚本由 Mark 长期维护，环境故障先修脚本，不作为验证借口
- **受控自我进化**：成员提案、Ed 复核、人拍板、主理人执行；git commit 即回滚点，进化全程可追溯
- **规划期第一性原理分解**：Remy对每条需求标注「硬约束／惯例」归类（惯例必附依据），Archie设计文件必含「基本事实表」（各注来源），类比式设计在规划期即被拦截
- **操作人模式可切换**：门外汉／标准／专家三档，Phase 0 声明、随时切换；门外汉模式附白话摘要与行为验收清单、技术决策代劳 opt-out；不可逆门禁与测试门任何模式都不放松
- **门外汉模式五护栏**：模式探测（偏门外汉语言主动建议切换）、代劳决策清单（人话记录、可逐条翻案）、人话交接卡（成品位置＋使用说明＋回访召唤语）、快捷回复提问（A/B 选项可一句答完）、「感觉不对」有效信号通道
- **协作铁律**：主理人亲自建团、所有资讯经主理人中转、团员不互相直连

## 使用示例

- 我有一个开发需求，请判断类型并用合适的流程交付。
- 帮我修这个 bug、加功能或重构这段程式码。
- 审查这份程式码，给出测试用例与品质报告。
- 帮我把这个旧专案从 Python 2 迁移到 3，并补回归测试。
- 我想做一个 RAG 问答应用，请从资料规格到可运行程式完整交付。
- 帮我设计一个采购审批系统，要能追溯到每条需求对应的程式码位置。
- 用本体驱动开发做一个合同管理系统，需求探索每个阶段都要我确认。
- 接手这个旧专案，帮我逆向出完整的功能清单、穿透链和资料库表，还要找出没有菜单的定时任务。
- 把这次的交付成果做成一份 12 页的咨询风格 HTML 简报，技术结论要标注来源。
- 帮我建立一个 OKF 知识库，并告诉我哪些概念未验证或已经过期。
- 用严谨工程流程修这个 bug：先重现、二分法找根因，再给我失败到通过的输出。
- 这串 PR 都绿灯了，帮我验证后由底层往上合并，并告诉我停在哪个上限。
- 把这个大任务拆成 worker／verifier，跑一个有完成承诺与上限的循环，最后给我交接纪录。
- 深度 review 这个 PR：安全与可维护性分开看，只给我最多 7 则可贴的 comment 和一个灯号。
- 我卡在同一个错误两次了，请Ed读证据后给第二意见，并先用 The Algorithm 问需求。
- 对接这个专案的 ledger，照 route 找负责人，从 next_queue 拿一张卡给我。
- 把Vera的测试证据换算成 ledger 的 verified，准备批准包但先不要写入。

## 头像

头像已自动生成在 `avatars/` 目录下。如需替换为自订头像，要求：
- 格式：PNG（推荐）或 JPG
- 尺寸：512×512 px
- 大小：单张不超过 500KB

## 安装

将专家包目录放到专家目录下：

```
~/.workbuddy/plugins/marketplaces/my-experts/plugins/julia-dev/
```

然后执行注册命令使其可见：

```bash
python3 scripts/register_expert.py <expert-dir>
```

## 开发迭代史

本专家包的进化全部来自四个渠道：使用者拍板、缺口评估走查、实测回灌、外部开源吸收，并一律走「提案 → Ed 复核 → 人拍板 → 主理人执行 → commit」的受控回路。从包建立期（v1.0–v1.8.x）、接缝修补（v1.9.0）、实测回灌（v1.9.1）、制度化期（v1.10.0–1.10.2）、可用性期（v1.10.3–1.10.5）、发行与治理期（v1.10.6–1.10.8）到命名与文档期（v1.10.9–1.10.10）的完整叙事、各版本来源与历史教训清单，见 [`docs/iteration-history.md`](iteration-history.md)；逐条变更记录见 [`docs/evolution-log.md`](evolution-log.md)。

## 致谢

本专家包是对下列开源专案方法论的**浓缩重述**，不是原始文件复制；每个派生 Skill 目录下有独立 `ATTRIBUTION.md` 记录确切来源与授权条款。各来源专案依其自身授权（MIT／Apache 2.0／CC BY 4.0）持续有效，感谢原作者的开源贡献：

| 来源专案 | 作者／持有者 | 授权 | 吸收为 |
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
| [consulting-html-ppt](https://github.com/sharptoolbox/consulting-html-ppt) | sharptoolbox | 未宣告授权 | consulting-html-ppt（仅吸收方法要点，未复制模板或素材） |
| [ledger-driven-dev](https://github.com/iczrac/ledger-driven-dev) | iczrac | MIT | ledger-bridge＋Luca 角色 |

`self-evolution` Skill、操作人模式与门外汉护栏为本专家包原创。本专家包自身以 MIT 授权发布，见根目录 `LICENSE`。

## 多平台适配

本专家包以 WorkBuddy 包为 **canonical 单一事实源**，其他平台包由 `python3 scripts/build_dist.py` 自动生成到 `dist/`，永远以脚本重建、不手改。所有平台共享同一套铁律：门禁、测试取证、操作人模式、第一性原理门与进化提案纪律。

| 发行目录 | 平台 | 形态 | 适配方式 |
|----------|------|------|----------|
| `dist/claude-code/` | Claude Code | **完整团队** | `.claude-plugin/plugin.json`＋11 个 subagents＋19 skills＋`/julia` 指令 |
| `dist/agents-md/` | Codex CLI／Gemini CLI／Jules 等 | **Solo（角色内切）** | `AGENTS.md` 总纲＋`roles/`＋`skills/`；单代理按阶段戴帽执行，Ed／Vera 转为自我复核帽与实跑测试帽 |
| `dist/cursor/` | Cursor | Solo 变体 | `.cursor/rules/julia-dev.mdc`（`alwaysApply`）＋`roles/`＋`skills/` |
| `dist/copilot/` | VS Code Copilot | 自定义 agents | `.github/agents/` 11 个代理；无自动路由，操作人显式 `@julia-dev-team-lead` 统筹 |

改写纪律：跨平台转换只做**语义等价**改写（如 SendMessage 协作语义改为结果回传、清理平台专有 frontmatter 栏位），不改任何门禁、角色分工或方法论内容。

## 打包分享

```bash
zip -r julia-dev.zip julia-dev/
```
