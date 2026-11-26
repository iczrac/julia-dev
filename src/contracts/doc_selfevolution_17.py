"""生成物（由 scripts/gen_doc_contracts.py 派生，勿手改）。

可执行契约：真实读取对应能力文档并断言结构完整性。
绑定路径：tests/test_doc_contracts.py import 本模块 → 符号命中 → impl 集合 → verified。
"""

from pathlib import Path

DOC = Path('skills/self-evolution/SKILL.md')
REQUIRED_ANCHORS = ['# 受控自我進化', '## 觸發條件（提案資格門）', '## 提案格式（固定七段）']
MIN_CHARS = 946


def contract_check(root: Path) -> None:
    p = root / DOC
    assert p.is_file(), f"契约失败：{DOC} 缺失"
    text = p.read_text(encoding="utf-8")
    assert len(text) >= MIN_CHARS, f"契约失败：{DOC} 内容过短（{len(text)} < {MIN_CHARS}）"
    for anchor in REQUIRED_ANCHORS:
        assert anchor in text, f"契约失败：{DOC} 缺锚点 {anchor!r}"
