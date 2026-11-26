#!/usr/bin/env python3
"""Knox 冗余扫描：把「規矩冗餘」从角色文字变成可执行判据。

只扫本仓权威文档（agents/*.md、skills/*/SKILL.md），检查两类确定性问题：
  1. duplicate_clause：同一条实质条款（>=40 字）在多份文档中重复出现；
  2. stale_ref：正文内联代码指向本仓不存在的 agents/skills/onto/scripts/tests 路径。

合法重复与指向外部仓的路径必须写进 knox_allowlist.json 并附理由与批准人；
allowlist 是例外登记处，不是第二事实源。扫描只读，不修改任何文档。

用法：
    python3 scripts/knox_scan.py --root . --json
退出码：0 零命中；1 有命中；2 配置/输入错误。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SCHEMA = "knox-scan/1"
ALLOW_SCHEMA = "knox-allowlist/1"
MIN_CLAUSE_CHARS = 40
LEADING_RE = re.compile(r"^\s*(?:[-*+>]\s*|\d+[.)]\s*|#+\s*)*")
REF_RE = re.compile(r"`((?:agents|skills|onto|scripts|tests)/[A-Za-z0-9_./*-]+)`")


def normalize(line: str) -> str:
    """去掉列表/标题/强调符号后压成单行，用于比对实质条款。"""
    stripped = LEADING_RE.sub("", line.strip()).replace("`", "")
    return re.sub(r"\s+", " ", stripped).strip()


def iter_docs(root: Path) -> list[Path]:
    return sorted(root.glob("agents/*.md")) + sorted(root.glob("skills/*/SKILL.md"))


def load_allowlist(root: Path) -> dict:
    path = root / "knox_allowlist.json"
    if not path.is_file():
        return {"schema": ALLOW_SCHEMA, "duplicate_clauses": [], "stale_refs": []}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValueError(f"allowlist 不可读：{exc}") from exc
    if data.get("schema") != ALLOW_SCHEMA:
        raise ValueError(f"allowlist schema 必须为 {ALLOW_SCHEMA}")
    return data


def scan_duplicates(root: Path, allow: dict) -> list[dict]:
    approved = {e.get("sha256") for e in allow.get("duplicate_clauses", [])}
    clauses: dict[str, dict] = {}
    for path in iter_docs(root):
        rel = path.relative_to(root).as_posix()
        for line in path.read_text(encoding="utf-8").splitlines():
            text = normalize(line)
            if len(text) < MIN_CLAUSE_CHARS or text.startswith(("#", "|")):
                continue
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            item = clauses.setdefault(digest, {"text": text, "files": set()})
            item["files"].add(rel)
    hits = []
    for digest, item in sorted(clauses.items()):
        if len(item["files"]) < 2 or digest in approved:
            continue
        hits.append({"hash": digest, "files": sorted(item["files"]),
                     "text": item["text"][:160]})
    return hits


def scan_stale_refs(root: Path, allow: dict) -> list[dict]:
    approved = {(e.get("file"), e.get("ref"))
                for e in allow.get("stale_refs", [])}
    hits = []
    for path in iter_docs(root):
        rel = path.relative_to(root).as_posix()
        for line in path.read_text(encoding="utf-8").splitlines():
            for ref in REF_RE.findall(line):
                if "*" in ref:
                    continue  # 模式说明，不是单文件引用
                if (root / ref.rstrip("/")).exists():
                    continue
                if (rel, ref) in approved:
                    continue
                hits.append({"file": rel, "ref": ref, "line": line.strip()[:160]})
    return hits


def run(root: Path) -> dict:
    allow = load_allowlist(root)
    dup = scan_duplicates(root, allow)
    stale = scan_stale_refs(root, allow)
    return {"schema": SCHEMA, "root": root.name,
            "docs_scanned": len(iter_docs(root)),
            "duplicate_clauses": dup, "stale_refs": stale,
            "hits": len(dup) + len(stale), "ok": not (dup or stale)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Knox 冗余扫描（零依赖、只读）")
    ap.add_argument("--root", default=".", help="仓库根目录")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"输入错误：目录不存在 {root}", file=sys.stderr)
        return 2
    try:
        report = run(root)
    except (OSError, ValueError, UnicodeDecodeError) as exc:
        print(f"输入错误：{exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Knox · 扫描 {report['docs_scanned']} 份文档 · 命中 {report['hits']}")
        for item in report["duplicate_clauses"]:
            print(f"  重复条款 {item['hash'][:12]} — {', '.join(item['files'])}")
        for item in report["stale_refs"]:
            print(f"  失效引用 {item['file']} -> {item['ref']}")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
