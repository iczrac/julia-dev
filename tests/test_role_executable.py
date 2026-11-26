"""Workflow V 角色可执行性：机械角色必须有真工具，人类裁决角色必须显式声明。

这是「把教训编进结构」的测试版：Workflow V 曾把 Knox 写成纸面角色，长期没有
可执行脚本；此后任何机械角色若只剩文字、或引用不存在的工具，测试必须失败。
人类判断角色（Vera/Ed/Julia）不强求脚本，但必须在本文件显式登记理由。
"""
from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEAM = REPO / "agents" / "julia-dev-team-lead.md"
LEDGER = Path(os.environ.get("JULIA_LEDGER_ROOT",
                             str(REPO.parent / "ledger-driven-dev")))

EXPECTED_ROLES = {"機械自查", "Vera", "Knox", "Ed", "Julia"}
HUMAN_ONLY = {
    "Vera": "抽验需判断证据新鲜度与 dist 一致性，非纯脚本动作",
    "Ed": "不可逆前的第二意见只能由顾问裁决",
    "Julia": "汇编与人拍板由主理人执行",
}

SECTION_RE = re.compile(r"^### Workflow V：.*?$(.*?)(?=^---$)", re.M | re.S)
ROLE_RE = re.compile(r"^\s*\d+\.\s+\*\*([^*]+)\*\*", re.M)
TOKEN_RE = re.compile(r"`([^`]+)`")
SCRIPT_RE = re.compile(r"(?:^|[/\s])([A-Za-z0-9_.-]+\.(?:py|sh))\b")


def workflow_v(text: str) -> str:
    m = SECTION_RE.search(text)
    return m.group(1) if m else ""


def steps(section: str) -> list[tuple[str, str]]:
    parts = ROLE_RE.split(section)
    return [(parts[i].split("（")[0].strip(), parts[i + 1])
            for i in range(1, len(parts) - 1, 2)]


def resolves(token: str, repo_root: Path) -> bool:
    """Token 是工具主张时才判存在；布局路径/产物名不算工具。"""
    t = token.strip()
    if t.startswith(("scripts/", "governance/", "tests/")):
        return (repo_root / t).exists() or (LEDGER / t).exists()
    m = SCRIPT_RE.search(t)
    if not m:
        return False
    name = m.group(1)
    return any((root / "scripts" / name).exists() for root in (repo_root, LEDGER))


def audit(text: str, repo_root: Path = REPO) -> list[dict]:
    found = steps(workflow_v(text))
    roles = {role for role, _ in found}
    problems: list[dict] = []
    if roles != EXPECTED_ROLES:
        problems.append({"role": "<workflow>", "reason": "role_set_mismatch",
                         "found": sorted(roles)})
    for role, body in found:
        if role in HUMAN_ONLY:
            continue
        tools = [t for t in TOKEN_RE.findall(body) if resolves(t, repo_root)]
        if not tools:
            problems.append({"role": role, "reason": "no_executable_tool"})
    return problems


SYNTHETIC = """### Workflow V：內部體檢（測試夾具）
1. **機械自查**：跑 `spec_check.py`
2. **Vera**：抽驗
3. **Knox**：跑 `scripts/knox_scan.py`
4. **Ed**：裁決
5. **Julia**：汇編
---
"""


class RoleExecutableTest(unittest.TestCase):

    def test_real_workflow_passes(self):
        self.assertEqual(audit(TEAM.read_text(encoding="utf-8")), [])

    def test_ghost_tool_hits(self):
        text = SYNTHETIC.replace("scripts/knox_scan.py", "scripts/ghost_tool.py")
        problems = audit(text)
        self.assertIn({"role": "Knox", "reason": "no_executable_tool"}, problems)

    def test_missing_role_hits(self):
        text = SYNTHETIC.replace("5. **Julia**：汇編\n", "")
        problems = audit(text)
        self.assertTrue(any(p["reason"] == "role_set_mismatch" for p in problems))

    def test_undeclared_human_role_hits(self):
        text = SYNTHETIC.replace("---\n", "6. **Ship**：跑 `scripts/ghost_tool.py`\n---\n")
        problems = audit(text)
        self.assertIn({"role": "Ship", "reason": "no_executable_tool"}, problems)

    def test_human_exceptions_have_reasons(self):
        self.assertTrue(HUMAN_ONLY)
        for role in HUMAN_ONLY:
            self.assertIn(role, EXPECTED_ROLES)
            self.assertTrue(HUMAN_ONLY[role].strip())


if __name__ == "__main__":
    unittest.main()
