"""Knox 冗余扫描的行为测试：真实基线 + 三类负向证明。

判据只认可观察结果：新增重复条款或失效本仓引用必须命中；登记例外后必须放行；
坏 allowlist 必须 fail-closed，不能静默当作空例外表。
"""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import knox_scan as knox  # noqa: E402

CLAUSE = "这是一条专门用于负向证明的足够长的重复条款，它不应该出现在任何正式规范文档里，只是临时测试夹具。"
ALLOW = {"schema": knox.ALLOW_SCHEMA, "duplicate_clauses": [], "stale_refs": []}


def make_root(tmp: Path) -> Path:
    root = tmp / "repo"
    (root / "agents").mkdir(parents=True, exist_ok=True)
    (root / "skills" / "demo").mkdir(parents=True, exist_ok=True)
    return root


class KnoxScanTest(unittest.TestCase):

    def test_real_repo_baseline(self):
        report = knox.run(REPO)
        self.assertTrue(report["ok"], report)
        self.assertGreaterEqual(report["docs_scanned"], 29)
        self.assertEqual(report["hits"], 0)

    def test_duplicate_clause_hits(self):
        with tempfile.TemporaryDirectory() as td:
            root = make_root(Path(td))
            (root / "agents" / "a.md").write_text(CLAUSE, encoding="utf-8")
            (root / "agents" / "b.md").write_text(CLAUSE, encoding="utf-8")
            report = knox.run(root)
            self.assertEqual(len(report["duplicate_clauses"]), 1)
            self.assertEqual(report["hits"], 1)
            self.assertIn("agents/a.md", report["duplicate_clauses"][0]["files"])

    def test_stale_ref_hits(self):
        with tempfile.TemporaryDirectory() as td:
            root = make_root(Path(td))
            (root / "skills" / "demo" / "SKILL.md").write_text(
                "参考 `scripts/ghost.py` 的实现细节。", encoding="utf-8")
            report = knox.run(root)
            self.assertEqual(len(report["stale_refs"]), 1)
            self.assertEqual(report["stale_refs"][0]["ref"], "scripts/ghost.py")

    def test_allowlist_suppresses_both(self):
        with tempfile.TemporaryDirectory() as td:
            root = make_root(Path(td))
            (root / "agents" / "a.md").write_text(CLAUSE, encoding="utf-8")
            (root / "agents" / "b.md").write_text(CLAUSE, encoding="utf-8")
            rel = "skills/demo/SKILL.md"
            (root / rel).write_text("参考 `scripts/ghost.py`。", encoding="utf-8")
            digest = hashlib.sha256(knox.normalize(CLAUSE).encode("utf-8")).hexdigest()
            allow = dict(ALLOW)
            allow["duplicate_clauses"] = [{"sha256": digest, "reason": "fixture",
                                           "approved_by": "test"}]
            allow["stale_refs"] = [{"file": rel, "ref": "scripts/ghost.py",
                                    "reason": "fixture", "approved_by": "test"}]
            (root / "knox_allowlist.json").write_text(
                json.dumps(allow, ensure_ascii=False), encoding="utf-8")
            self.assertTrue(knox.run(root)["ok"])

    def test_bad_allowlist_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = make_root(Path(td))
            (root / "knox_allowlist.json").write_text(
                json.dumps({"schema": "not-knox/9"}), encoding="utf-8")
            with self.assertRaises(ValueError):
                knox.run(root)

    def test_unified_gate_wires_all_checks(self):
        gate = (REPO / "scripts" / "check.sh").read_text(encoding="utf-8")
        for needle in ("spec_check.py", "knox_scan.py", "unittest discover",
                       "verify_ledger.py", "build_capability_model.py"):
            self.assertIn(needle, gate, f"统一门禁缺少：{needle}")
        self.assertIn("--check", gate, "模型漂移门禁必须启用 --check")


if __name__ == "__main__":
    unittest.main()
