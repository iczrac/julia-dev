"""ledger-bridge 技能的可执行契约：把 SKILL.md 的隐性规范变成机器断言。

绑定语义：测试 import 本模块 → 符号解析命中 → 本模块在能力 impl 集合内 →
verified 成立；且每个断言真实读取 SKILL.md，文档损坏即失败（非空壳刷分）。
契约内容按该技能真实结构订立（markdown 标题式，无 YAML frontmatter）。
"""

from pathlib import Path

SKILL = Path("skills/ledger-bridge/SKILL.md")
# 该技能的必备语义章节：删改任何一节即契约失败
REQUIRED_SECTIONS = (
    "## 何時用",
    "## 三條硬邊界",
    "## 四個交接對象",
    "## Fail-closed 對照",
    "## 規範型倉庫自查（spec_check）",
)


def contract_check(root: Path) -> None:
    p = root / SKILL
    assert p.is_file(), f"契约失败：{SKILL} 缺失"
    text = p.read_text(encoding="utf-8")
    assert text.startswith("# 帳本橋接"), f"契约失败：{SKILL} 标题漂移"
    for sec in REQUIRED_SECTIONS:
        assert sec in text, f"契约失败：{SKILL} 缺章节 {sec}"
    assert "spec_check.py" in text, "契约失败：未声明 spec_check 桥接命令"
    assert "CapabilityForge/ledger-driven-dev" in text, \
        "契约失败：未钉死 ledger 本地执行路径"
