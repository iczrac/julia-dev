"""规范型仓库合规包装套件：把 ledger spec_check 机械判据包装为本仓单元测试。

哲学（2026-11-25 拍板）：代码仓库的 verified 靠单测绑定源码；规范型仓库的
verified 靠机械判据绑定文档。本套件使 julia 的文档资产（agents/*.md、
skills/*/SKILL.md、onto/*.json）获得与代码同等的证据待遇——判据全绿即
「一致与在位」的机械证明（内容质量仍归 Workflow V 人工流程线）。

工具唯一来源：ledger-driven-dev 的 spec_check.py（本仓不自建检查器，
ledger-bridge 纪律）。路径经 JULIA_LEDGER_ROOT 环境变量可覆盖，默认
CapabilityForge 兄弟目录。
"""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER_ROOT = Path(
    os.environ.get("JULIA_LEDGER_ROOT",
                   REPO.parent / "ledger-driven-dev"))
SPEC_CHECK = LEDGER_ROOT / "scripts" / "spec_check.py"


def run_spec_check(no_rebuild: bool = False):
    cmd = [sys.executable, str(SPEC_CHECK), "--target", str(REPO), "--json"]
    if no_rebuild:
        cmd.append("--no-rebuild")
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if proc.returncode not in (0, 1):
        raise RuntimeError(f"spec_check 异常退出 {proc.returncode}: {proc.stderr[-500:]}")
    return proc.returncode, json.loads(proc.stdout)


def metric(report: dict, name: str) -> dict:
    return next(m for m in report["metrics"] if m["metric"] == name)


class SpecComplianceTest(unittest.TestCase):
    """九判据全绿：术语/版本/派生/必备/链接/可执行主张/本体/发版标签/组合锚。"""

    def setUp(self):
        self.code, self.report = run_spec_check()

    def test_toolchain_available(self):
        self.assertTrue(SPEC_CHECK.exists(),
                        f"spec_check 不存在：{SPEC_CHECK}（检查 JULIA_LEDGER_ROOT）")

    def test_exit_code_zero(self):
        self.assertEqual(self.code, 0,
                         "spec_check 退出码 1：存在命中，明细见各判据用例")

    def test_forbidden_terms_zero(self):
        m = metric(self.report, "forbidden_terms")
        self.assertTrue(m.get("applicable", True), "术语判据意外 n/a")
        self.assertEqual(m["hits"], 0, f"术语残留：{m.get('detail')}")

    def test_version_consistent(self):
        m = metric(self.report, "version")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"版本失步：{m.get('detail')}")

    def test_generated_no_drift(self):
        m = metric(self.report, "generated_drift")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"派生漂移：{m.get('detail')}")

    def test_required_files_present(self):
        m = metric(self.report, "required_files")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"必备文件缺失：{m.get('detail')}")

    def test_links_resolve(self):
        m = metric(self.report, "broken_links")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"断链：{m.get('detail')}")

    def test_ontology_integrity(self):
        m = metric(self.report, "ontology_integrity")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"本体缺陷：{m.get('detail')}")

    def test_release_tag_exists(self):
        m = metric(self.report, "release_tag")
        self.assertTrue(m.get("applicable", True))
        self.assertEqual(m["hits"], 0, f"版本缺 tag：{m.get('detail')}")

    def test_all_criteria_applicable(self):
        na = [m["metric"] for m in self.report["metrics"] if not m.get("applicable", True)]
        self.assertEqual(na, [], f"九判据应全部适用（compat 由组合锚启用）：{na}")


class OntologyContractTest(unittest.TestCase):
    """本体契约抽验：唯一声明点与平台映射的关键不变量。"""

    def setUp(self):
        self.onto = json.loads((REPO / "onto" / "actors.json").read_text(encoding="utf-8"))

    def test_eleven_actors_declared(self):
        self.assertEqual(len(self.onto["actors"]), 11)

    def test_platform_paths_resolve(self):
        missing = []
        for a in self.onto["actors"]:
            for plat, p in a.get("platforms", {}).items():
                if p is not None and not (REPO / p).exists():
                    missing.append(f"{a['id']}:{plat}:{p}")
        self.assertEqual(missing, [], f"平台映射断链：{missing}")

    def test_hermes_is_null_candidate(self):
        julia = next(a for a in self.onto["actors"] if a["id"] == "actor.julia")
        self.assertIsNone(julia["platforms"].get("hermes"),
                          "hermes 落地时须同步更新此处与 dist")


class CompatAnchorTest(unittest.TestCase):
    """组合锚：声明的 ledger 版本约束必须满足（compat 判据的直读复核）。"""

    def test_ledger_min_version(self):
        cfg = json.loads((REPO / "spec_check.json").read_text(encoding="utf-8"))
        anchors = cfg.get("compat", {}).get("anchors", [])
        self.assertTrue(anchors, "spec_check.json 未声明组合锚")
        code, report = run_spec_check(no_rebuild=True)
        self.assertEqual(code, 0, "compat 判据命中：兄弟仓版本不满足锚")


if __name__ == "__main__":
    unittest.main()
