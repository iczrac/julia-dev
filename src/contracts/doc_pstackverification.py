"""生成物（由 scripts/gen_doc_contracts.py 派生，勿手改）。

可执行契约：真实读取对应能力文档并断言结构完整性。
绑定路径：tests/test_doc_contracts.py import 本模块 → 符号命中 → impl 集合 → verified。
"""

from pathlib import Path

DOC = Path('skills/pstack-verification/SKILL.md')
REQUIRED_ANCHORS = ['# pstack 可驗證性方法（濃縮版）', '## 何時用', '## 一、證明它可行（Prove It Works）']
MIN_CHARS = 992


def contract_check(root: Path) -> None:
    p = root / DOC
    assert p.is_file(), f"契约失败：{DOC} 缺失"
    text = p.read_text(encoding="utf-8")
    assert len(text) >= MIN_CHARS, f"契约失败：{DOC} 内容过短（{len(text)} < {MIN_CHARS}）"
    for anchor in REQUIRED_ANCHORS:
        assert anchor in text, f"契约失败：{DOC} 缺锚点 {anchor!r}"
