#!/usr/bin/env bash
# julia-dev-squad 统一质量门禁：本地/发布前同一份脚本。
# CI 接入需先解决兄弟仓路径依赖，留待 bootstrap-lint 提案；此处不声称已接 CI。
# 事实与规则仍归 ledger；本脚本只把既有判据串起来，不复制检查逻辑。
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
LEDGER="${JULIA_LEDGER_ROOT:-$ROOT/../ledger-driven-dev}"
FAILURES=0
BOARD_NAME="$(python3 governance/board_path.py --target . --filename)"

note(){ printf '\n== %s ==\n' "$1"; }
pass(){ printf '[PASS] %s\n' "$1"; }
fail(){ printf '[FAIL] %s\n' "$1"; FAILURES=$((FAILURES+1)); }
run(){ name="$1"; shift; if "$@"; then pass "$name"; else fail "$name"; fi; }

stage_spec(){
  note '规范自查（ledger spec-check/1：术语/版本/派生漂移/必备文件/链接/本体/标签/兼容/可执行主张）'
  if [ ! -f "$LEDGER/scripts/spec_check.py" ]; then
    echo "  找不到 ledger spec_check.py：$LEDGER（可用 JULIA_LEDGER_ROOT 覆盖）"
    return 1
  fi
  python3 "$LEDGER/scripts/spec_check.py" --target . --json >/dev/null || return 1
  echo '  九项判据全适用且零命中'
}

stage_knox(){
  note '规矩冗余（Knox：重复条款 / 失效本仓引用，例外须登记）'
  python3 scripts/knox_scan.py --root . --json >/dev/null || return 1
  echo '  重复条款与失效引用均为零命中'
}

stage_tests(){
  note '单元测试（文档契约 + spec 合规 + Knox 行为）'
  python3 -m unittest discover -s tests -v >/dev/null || return 1
  echo '  unittest discover 全绿'
}

stage_ledger(){
  note '账本不变量（verify_ledger --strict）'
  python3 governance/verify_ledger.py --root . \
    --ledger governance/DECISION_LEDGER.json \
    --registry governance/registry.json \
    --board "governance/$BOARD_NAME" --strict || return 1
}

stage_model(){
  note '能力模型可复算（账本 = f(registry, 仓库, 报告)）'
  python3 governance/build_capability_model.py --root . \
    --test-report governance/test_report.json --check || return 1
}

if [ "${1:-all}" = "--help" ]; then
  echo "用法: bash scripts/check.sh [all]"
  echo "  JULIA_LEDGER_ROOT 可覆盖 ledger-driven-dev 的路径（默认兄弟目录）"
  exit 0
fi

run '规范自查' stage_spec
run '规矩冗余' stage_knox
run '单元测试' stage_tests
run '账本不变量' stage_ledger
run '模型可复算' stage_model

printf '\n'
if [ "$FAILURES" -gt 0 ]; then
  printf '质量门禁失败：%d 个阶段未通过\n' "$FAILURES"
  exit 1
fi
printf '质量门禁全绿：规范自查 / 规矩冗余 / 单元测试 / 账本不变量 / 模型可复算\n'
