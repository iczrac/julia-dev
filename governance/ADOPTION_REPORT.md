# 存量项目接入报告

> 本报告由只读扫描生成，未修改任何既有文件。草稿需经人工确认才可成为正式清单。

- 模式：filesystem-only/spec-repo / schema registry-draft/1
- 文件计数：源码 1、测试 0、文档 53、配置 0
- 候选：模块 3、能力点 31
- 置信度：medium

## 候选模块

| 模块码 | 扫描入口 | 能力点数 |
|---|---|---:|
| TEAM | agents/ | 11 |
| SKILLS | skills/ | 19 |
| INFRA | scripts/ | 1 |

## 警告

- 规范型仓库模式：能力点候选来自 SKILL.md/agents 文档结构，编码与分域需人工确认（draft 仅供采纳起点）。
- 未发现测试文件；这些能力预期停在 L0-L2，不要误判为完成。

## 下一步

1. 编辑 `governance/registry.draft.json`：删除非能力文件、合并重复域、校准 hints。
2. 用 `init_project.py --mode adopt --from-draft ...` 生成治理骨架。
3. 在项目根运行 `governance/build_capability_model.py --root . --dry-run` 对照真实等级。
4. 确认后再正式生成并跑 `governance/verify_ledger.py --root . --strict`。
