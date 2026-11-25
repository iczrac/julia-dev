"""build_dist 基建能力的可执行契约（代码资产也需绑定证据）。

契约断言：四平台发行档存在且保留 11 成员关键锚点——发行产物漂移即失败。
绑定：tests/test_doc_contracts.py import 本模块 → 命中本能力 impl 集合。
"""

from pathlib import Path

DISTS = (
    "dist/claude-code",
    "dist/agents-md",
    "dist/cursor",
    "dist/copilot",
)
ANCHOR = "julia-dev-team-lead"


def contract_check(root: Path) -> None:
    for rel in DISTS:
        d = root / rel
        assert d.is_dir(), f"契约失败：发行档 {rel} 缺失"
        files = list(d.rglob("*"))
        assert files, f"契约失败：发行档 {rel} 为空"
        contents = "\n".join(
            f.read_text(encoding="utf-8", errors="ignore")
            for f in files if f.is_file() and f.suffix in (".md", ".json", ".mdc")
        )
        assert ANCHOR in contents, f"契约失败：发行档 {rel} 缺 {ANCHOR} 锚点"
