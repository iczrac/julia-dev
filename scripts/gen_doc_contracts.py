"""文档资产可执行契约生成器：registry.json 是唯一声明点，本脚本生成 31 个契约模块 + 测试。

设计纪律（对齐本体层 v0.1 的「唯一声明点」原则）：
- 契约内容不在 31 个文件里手抄；由本脚本逐点派生，改语义只改这里
- 生成物纳入 spec_check.json generated 判据（rebuild 后逐字节比对），防手改漂移
- 每个能力点有独立契约模块 → 符号绑定粒度精确，杜绝「一个共享模块刷 31 点」
- 每个契约真实读取 impl 文档并断言结构/关键语义，文档损坏即失败（非空壳 import）

契约强度分级（诚实口径）：
- SKILL.md：标题、必备章节锚点（取该文档实际 ## 标题的前 3 个）、长度下限
- agents/*.md：标题存在、长度下限、角色名出现在文档中（来自 hints）
- build_dist.py（代码资产）：已有符号绑定，无需契约模块——保留原生绑定，不重复造
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "governance" / "registry.json"
CONTRACTS = ROOT / "src" / "contracts"
TESTS = ROOT / "tests"

HEADER = '''"""生成物（由 scripts/gen_doc_contracts.py 派生，勿手改）。

可执行契约：真实读取对应能力文档并断言结构完整性。
绑定路径：tests/test_doc_contracts.py import 本模块 → 符号命中 → impl 集合 → verified。
"""

from pathlib import Path

DOC = Path({doc!r})
REQUIRED_ANCHORS = {anchors!r}
MIN_CHARS = {min_chars}


def contract_check(root: Path) -> None:
    p = root / DOC
    assert p.is_file(), f"契约失败：{{DOC}} 缺失"
    text = p.read_text(encoding="utf-8")
    assert len(text) >= MIN_CHARS, f"契约失败：{{DOC}} 内容过短（{{len(text)}} < {{MIN_CHARS}}）"
    for anchor in REQUIRED_ANCHORS:
        assert anchor in text, f"契约失败：{{DOC}} 缺锚点 {{anchor!r}}"
'''


def anchors_for(doc: Path, count: int = 3) -> list[str]:
    text = doc.read_text(encoding="utf-8")
    heads = re.findall(r"^#{1,2} .+$", text, re.M)
    return heads[:count]


def module_name(cap: dict, index: int = 0) -> str:
    base = re.sub(r"[^a-z0-9]+", "_", cap["domain"].lower()).strip("_")
    return f"doc_{base}_{index:02d}"


def build() -> tuple[list[str], list[str]]:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    CONTRACTS.mkdir(parents=True, exist_ok=True)
    generated: list[str] = []
    test_lines: list[str] = []
    for mod in reg["modules"]:
        for i, cap in enumerate(mod["caps"], 1):
            doc_rel = (cap.get("impl") or [""])[0]
            doc = ROOT / doc_rel
            # 代码资产：已存在手写契约模块（如 DIST）则保留，不覆盖
            name = module_name(cap, i)
            if doc.suffix == ".py":
                # 代码资产的契约模块按无序号名保留（如 doc_dist.py），人工维护
                manual = CONTRACTS / f"doc_{re.sub(r'[^a-z0-9]+', '_', cap['domain'].lower()).strip('_')}.py"
                if manual.is_file():
                    generated.append(f"src/contracts/{manual.stem}.py")
                    test_lines.append(
                        f"from src.contracts.{manual.stem} import contract_check as check_{manual.stem}")
                continue
            if not doc.is_file():
                print(f"[WARN] {cap['domain']}: impl 文档不存在，跳过 {doc_rel}")
                continue
            anchors = anchors_for(doc)
            if not anchors:
                print(f"[WARN] {cap['domain']}: 无标题锚点，跳过")
                continue
            (CONTRACTS / f"{name}.py").write_text(
                HEADER.format(doc=doc_rel.replace("\\", "/"),
                              anchors=anchors,
                              min_chars=max(200, len(doc.read_text(encoding="utf-8")) // 3)),
                encoding="utf-8")
            generated.append(f"src/contracts/{name}.py")
            test_lines.append(
                f"from src.contracts.{name} import contract_check as check_{name}")
    # 测试文件：每个能力点一个用例，逐点调用自己的契约（导入即绑定）
    body = ['"""文档资产可执行契约套件（生成物，勿手改）。"""', "", "import unittest",
            "from pathlib import Path", "", *test_lines, "",
            "ROOT = Path(__file__).resolve().parent.parent", "",
            "class DocContractTest(unittest.TestCase):"]
    for cap, name in [
        (c, module_name(c, i)) for m in reg["modules"] for i, c in enumerate(m["caps"], 1)
    ]:
        if f"src/contracts/{name}.py" in generated:
            body += [f"    def test_{name}(self):", f"        check_{name}(ROOT)", ""]
    body += ["", 'if __name__ == "__main__":', "    unittest.main()", ""]
    TESTS.joinpath("test_doc_contracts.py").write_text("\n".join(body), encoding="utf-8")
    generated.append("tests/test_doc_contracts.py")
    return generated, [f"{m['code']}.{c['domain']}" for m in reg["modules"] for c in m["caps"]]


def wire_registry(generated: list[str]) -> None:
    """把契约模块 + 测试路径写回 registry 的 impl / tests 字段。"""
    reg = json.loads(REG.read_text(encoding="utf-8"))
    for mod in reg["modules"]:
        for i, cap in enumerate(mod["caps"], 1):
            name = module_name(cap, i)
            rel = f"src/contracts/{name}.py"
            if rel in generated:
                impl = [x for x in cap.get("impl", []) if x != rel]
                cap["impl"] = impl + [rel]
                cap["tests"] = ["tests/test_doc_contracts.py"]
    REG.write_text(json.dumps(reg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import subprocess
    import sys

    files, caps = build()
    wire_registry(files)
    print(f"generated {len(files) - 1} contract modules + 1 suite for {len(caps)} caps")
    # 两个生成物同属一次重建：契约模块 + 四平台 dist，均纳入 generated 判据
    subprocess.run([sys.executable, "scripts/build_dist.py"], cwd=ROOT, check=True)
