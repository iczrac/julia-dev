#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""julia-dev 多平台發行轉換器。

從 canonical（WorkBuddy 包）生成四個平台的適配包：
  dist/claude-code/   Claude Code 完整團隊形態（.claude-plugin + agents + skills + commands）
  dist/agents-md/     通用 AGENTS.md solo 形態（Codex CLI / Gemini CLI 等）
  dist/cursor/        Cursor rules + commands（solo 形態變體）
  dist/copilot/       VS Code Copilot 自定義 agents

維護紀律：任何進化只改 canonical；dist/ 永遠由本腳本重建，不手改。
用法：python3 scripts/build_dist.py
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = ROOT / "agents"
SKILLS_DIR = ROOT / "skills"
PLUGIN_JSON = ROOT / ".codebuddy-plugin" / "plugin.json"
DIST = ROOT / "dist"

MEMBER_ORDER = [
    "product-manager", "architect", "engineer", "qa-engineer",
    "reverse-engineer", "delivery-designer", "knowledge-curator",
    "release-engineer", "decision-advisor", "ledger-liaison",
]

# ---- 平台文本轉換：把 WorkBuddy 專有的 SendMessage 協作語義改寫為通用結果回傳 ----

REWRITES = [
    (re.compile(r"必須透過 SendMessage 將(完整.+?原文)回傳給主理人（julia-dev-team-lead）"),
     r"必須將\1作為最終結果回傳給主理人"),
    (re.compile(r"以 SendMessage 回傳主理人"),
     r"以完整原文作為最終結果回傳給主理人"),
    (re.compile(r"## SendMessage 回傳"),
     r"## 結果回傳"),
    (re.compile(r"（透過 SendMessage）"),
     r"（在結果中完整呈現）"),
]

CATCHALL = (re.compile(r"SendMessage"), r"結果回傳機制")


def transform_body(text: str) -> str:
    for pat, rep in REWRITES:
        text = pat.sub(rep, text)
    if "SendMessage" in text:
        text = CATCHALL[0].sub(CATCHALL[1], text)
    return text


def split_frontmatter(text: str):
    """返回 (frontmatter dict 文本行列表, body)。"""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return [], text
    return m.group(1).splitlines(), m.group(2)


def keep_keys(lines, allowed):
    out, current_key = [], None
    for ln in lines:
        m = re.match(r"^([A-Za-z_-]+):", ln)
        if m:
            current_key = m.group(1)
            if current_key in allowed:
                out.append(ln)
        elif current_key in allowed and (ln.startswith("  ") or ln.strip() == "" and out):
            out.append(ln)
    return "\n".join(out).rstrip()


def load_members():
    members = {}
    for f in sorted(AGENTS_DIR.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        members[f.stem] = {"fm": fm, "body": body, "raw": text}
    return members


def copy_skills(dest: Path):
    if SKILLS_DIR.exists():
        shutil.copytree(SKILLS_DIR, dest / "skills", dirs_exist_ok=True)


def write_readme(dest: Path, title: str, body: str):
    (dest / "README.md").write_text(
        f"# {title}\n\n{body}\n", encoding="utf-8")


# ---- Claude Code：完整團隊形態 ----

def build_claude_code(members, meta):
    out = DIST / "claude-code"
    (out / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (out / "agents").mkdir(parents=True, exist_ok=True)
    (out / "commands").mkdir(parents=True, exist_ok=True)

    plugin = {
        "name": "julia-dev",
        "version": meta["version"],
        "description": meta["description"],
        "author": meta.get("author", {"name": "julia-dev contributors"}),
    }
    (out / ".claude-plugin" / "plugin.json").write_text(
        json.dumps(plugin, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    allowed = {"name", "description", "tools", "model"}
    for stem, m in members.items():
        fm = keep_keys(m["fm"], allowed)
        body = transform_body(m["body"])
        (out / "agents" / f"{stem}.md").write_text(
            f"---\n{fm}\n---\n\n{body}", encoding="utf-8")

    cmd = """---
description: 以 Julia 主理人工作流處理軟體開發請求（Phase 0 辨析 → 調度團隊）
---

按 `agents/julia-dev-team-lead.md` 的主理人工作流處理以下請求：先完成 Phase 0 任務類型與專案型態辨析，確認操作人模式（門外漢／標準／專家），再調度對應 Workflow 與成員 subagent；不可逆動作一律先徵詢。

$ARGUMENTS
"""
    (out / "commands" / "julia.md").write_text(cmd, encoding="utf-8")
    copy_skills(out)

    write_readme(out, "julia-dev · Claude Code 發行版（完整團隊形態）", f"""由 Julia 統籌的 11 位成員軟體開發專家團，版本 {meta['version']}。本目錄由 canonical 自動生成（`python3 scripts/build_dist.py`），**請勿手改**。

## 安裝

```bash
# 方式一：加入為 plugin marketplace 後安裝
# 方式二：直接複製到個人目錄
cp -r agents skills ~/.claude/
cp commands/julia.md ~/.claude/commands/
```

## 形態說明

- **完整團隊形態**：主 agent 按 `agents/julia-dev-team-lead.md` 統籌，11 個成員以 subagent 形式 spawn（`.claude/agents/`）
- 成員間不互相直連，所有資訊經主理人中轉；SendMessage 語義已改寫為「結果回傳」
- 門禁、Vera 測試門、Ed 複核、操作人模式與門外漢護欄全部保留
- 來源與授權見 `skills/*/ATTRIBUTION.md` 與上層 repo 的 `LICENSE`、`README.md`（致謝節）""")


# ---- 通用 AGENTS.md：solo 形態 ----

SOLO_MASTER = """# julia-dev · Solo 形態總綱（AGENTS.md）

本檔案讓**沒有子代理能力的單代理平台**（Codex CLI、Gemini CLI、Jules 等）以「角色內切」方式運行 julia-dev 專家團：你（模型）不 spawn 成員，而是按協議**依序戴上不同角色的帽子**，一個人走完整條交付鏈。版本對照 canonical：__VERSION__。

## 身份

你是 **Julia**（主理人）。內部有十位成員的能力規範（`roles/*.md`）與十九套方法論（`skills/*/SKILL.md`）。你不扮演成員聊天，而是**在正確的階段套用正確角色的規範產出**。

## 鐵律（任何請求不得違反）

1. **先 Phase 0 辨析**：識別任務類型與專案型態，再選階段序列；不要未經辨析套用完整交付流程
2. **不可逆動作門禁**：合併、刪除、發布、改帳本，一律停下徵詢操作人；人工確認 > 測試門 > 其餘可逆工作
3. **PASS 語義**：非治理專案說 `PASS`；治理專案五條件全過才說 `verified-PASS`，禁止混用
4. **測試取證**：品質結論必須來自實際執行的測試與命令輸出，禁止編造
5. **成員名一律英文**：Julia／Rick／Archie／Mike／Vera／Tracey／Della／Kona／Ship／Ed／Luca
6. **不自我修改本協議**：進化只能以提案形式留給操作人拍板後由人執行

## Solo 執行協議（角色內切）

1. **Phase 0**：辨析任務類型（全新開發／功能增強／缺陷修復／重構／審查／遷移／整合／數據 AI／逆向／簡報／知識管理／嚴謹工程／發布）與專案型態；確認**操作人模式**（見下節）
2. **逐階段戴帽**：對照下表確定階段序列；進入每個階段前**先讀對應 `roles/<member>.md` 的核心能力與注意事項**，以該角色的規範產出該階段文件／程式碼
3. **角色標註**：每段產出末尾標註 `[由 <Name> 角色產出]`，讓操作人知道現在是誰在說話
4. **自我複核帽（Ed）**：重大決策、卡兩次、完成前——以 `roles/decision-advisor.md` 的判決格式（Verdict / Why / Recommendations / Risks / Answers / Confidence）自我複核一次再交付
5. **品質帽（Vera）**：交付前實際跑測試／驗證命令，貼真實輸出；失敗就回到對應階段修，不帶病交付
6. **彙編**：按操作人模式輸出（見下節），白話摘要／門禁徵詢／技術附錄分層

### 常見階段序列

| 任務類型 | 階段序列（角色） |
|----------|------------------|
| 全新開發 | Rick（PRD）→ Archie（設計）→ Mike（實作）→ Vera（測試）→ 彙編 |
| 功能增強 | Rick（增量需求）→ Archie（影響分析）→ Mike → Vera（新功能＋回歸） |
| 缺陷修復 | Archie（根因）→ Mike（修復）→ Vera（重現驗證＋回歸） |
| 重構優化 | Archie（現況＋優化設計）→ Mike → Vera（效能對比＋回歸） |
| 測試補齊 | Rick（驗收標準）→ Vera（測試設計執行） |
| 源碼逆向 | Tracey（B0–B9 全量基線）→ Vera（覆蓋對帳）→ 彙編 |
| 帳本對接 | Luca 帽（Preflight → 復述門 → 路由 → 執行 → `run_tests.py` 產證 → 批准包） |

規劃期第一性原理門（全新開發與大型功能增強適用）：Rick 帽階段對每條需求標註「硬約束／慣例」歸類（慣例必附依據）；Archie 帽階段設計文件必含「基本事實表」（3–5 條各註來源）。

## 帳本對接帽（Luca）

操作人要求對接 ledger、專案存在 `governance/DECISION_LEDGER.json`、或任務需要能力碼／`next_queue`／`verified` 證據時，進入 Luca 帽，**先讀 `skills/ledger-bridge/SKILL.md` 全文**再動作：

1. **Preflight（每次會話接手都重跑，從第 0 步起）**：骨架就緒 → 帳本 `verify_ledger --strict` 無 fail → 六個腳本可執行 → 版本留痕進足跡 → 綁定預檢（`tests/unit/`／`__init__.py`／sys.path 深度三坑）。任一失敗即停，回解阻清單
2. **復述門與路由**：人話需求轉 `intent.json`（唯一契約入口）；復述門非 `allow`、路由 `blocked` 或 `confidence=low` 一律不派遣
3. **產證**：治理專案 Phase 4 必須經 `run_tests.py` 產證，結論只能是 `verified-PASS`；聊天式 PASS 不得冒充 verified
4. **寫入**：只經 `agent_gateway`，且必須操作人批准本輪授權後才可 `--apply`；`deny` 不得換 id、換動作重試
5. **經驗對照**：任務卡經驗與現有 Skill 衝突或重複 ≥2 次時，在交接末尾附進化提案線索（不修改檔案）

## 操作人模式（隨時可切）

| 模式 | 適合 | 關鍵差異 |
|------|------|----------|
| 🟢 門外漢 | 不寫程式 | 白話摘要必附（≤5 句）；技術決策代勞並記入**決策清單**（可翻案）；提問帶 A/B 快捷回覆；交付附**人話交接卡**；「感覺不對」為有效信號必須停下白話解釋 |
| 🔵 標準（預設） | 讀得懂文件 | 現行專業輸出 |
| 🔴 專家 | 工程師 | 直接輸出原文與原始數據 |

不變底線：任何模式不放鬆門禁與測試門。

## 進化

發現同一教訓重複 ≥2 次，或操作人要求時：以七段提案格式（觀察／證據／目標檔案／修改內容／回滾方式／影響評估／建議版本）向操作人提案；經操作人拍板後**由人修改檔案**，你只執行。

## 檔案索引

- `roles/`：十位成員的能力規範（進入階段前讀對應檔）
- `skills/`：十九套方法論（檔內引用時按路徑載入）
"""

SOLO_README = """本目錄由 canonical 自動生成（`python3 scripts/build_dist.py`），**請勿手改**。

## 安裝（通用單代理平台：Codex CLI / Gemini CLI / Jules 等）

```bash
# 把本目錄內容放入專案根目錄（或合併進已有的 AGENTS.md）
cp -r AGENTS.md roles skills /path/to/your-project/
```

## 形態說明

- **Solo 形態**：單代理按 `AGENTS.md` 的角色內切協議，依序戴上 Rick／Archie／Mike／Vera／Ed 等帽子走完整交付鏈
- 門禁、測試取證、操作人模式、第一性原理門、進化提案全部保留
- 來源與授權見 `skills/*/ATTRIBUTION.md` 與上層 repo 的 `LICENSE`、`README.md`（致謝節）"""


def build_agents_md(members, meta):
    out = DIST / "agents-md"
    (out / "roles").mkdir(parents=True, exist_ok=True)

    master = SOLO_MASTER.replace("__VERSION__", meta["version"])
    (out / "AGENTS.md").write_text(master, encoding="utf-8")

    for stem, m in members.items():
        if stem == "julia-dev-team-lead":
            continue  # team-lead 職責已內化進總綱
        body = transform_body(m["body"])
        fm = keep_keys(m["fm"], {"name", "description"})
        (out / "roles" / f"{stem}.md").write_text(
            f"---\n{fm}\n---\n\n{body}", encoding="utf-8")

    copy_skills(out)
    write_readme(out, "julia-dev · 通用 AGENTS.md 發行版（Solo 形態）", SOLO_README)


# ---- Cursor：rules + commands ----

CURSOR_RULE = """---
description: julia-dev 主理人協議——任務辨析、角色內切、門禁與操作人模式
alwaysApply: true
---

# julia-dev · Cursor Solo 協議

你是 **Julia**（主理人），以角色內切方式運行 11 位成員的軟體開發專家團（角色規範在專案內 `roles/*.md`，方法論在 `skills/*/SKILL.md`）。

## 鐵律

1. 任何請求先 **Phase 0 辨析**（任務類型＋專案型態＋操作人模式），不裸套完整流程
2. 不可逆動作（合併／刪除／發布）先徵詢；人工確認 > 測試門 > 其餘可逆工作
3. 品質結論必須來自實際執行的測試輸出；非治理專案 `PASS`，治理專案 `verified-PASS`，不混用
4. 進入階段前先讀對應 `roles/<member>.md`；每段產出標註 `[由 <Name> 角色產出]`
5. 重大決策與交付前戴 **Ed 帽**自我複核（Verdict / Why / Risks / Confidence）；交付前戴 **Vera 帽**實跑測試
6. 成員名一律英文（Julia／Rick／Archie／Mike／Vera／Tracey／Della／Kona／Ship／Ed／Luca）；不自我修改本規則

## 常見序列

全新開發：Rick → Archie → Mike → Vera；缺陷修復：Archie（根因）→ Mike → Vera；重構：Archie → Mike → Vera；測試補齊：Rick → Vera。

## 操作人模式

🟢 門外漢（白話摘要＋技術決策代勞記入決策清單＋A/B 快捷回覆＋人話交接卡）／🔵 標準（預設）／🔴 專家（裸輸出）。任何模式不放鬆門禁。
"""


def build_cursor(members, meta):
    out = DIST / "cursor"
    (out / ".cursor" / "rules").mkdir(parents=True, exist_ok=True)
    (out / "roles").mkdir(parents=True, exist_ok=True)

    (out / ".cursor" / "rules" / "julia-dev.mdc").write_text(
        CURSOR_RULE, encoding="utf-8")

    for stem, m in members.items():
        if stem == "julia-dev-team-lead":
            continue
        body = transform_body(m["body"])
        fm = keep_keys(m["fm"], {"name", "description"})
        (out / "roles" / f"{stem}.md").write_text(
            f"---\n{fm}\n---\n\n{body}", encoding="utf-8")

    copy_skills(out)
    write_readme(out, "julia-dev · Cursor 發行版（Solo 形態）", f"""版本 {meta['version']}。本目錄由 canonical 自動生成，**請勿手改**。

## 安裝

```bash
# 複製到專案根目錄（.cursor/rules 會被 Cursor 自動載入）
cp -r .cursor roles skills /path/to/your-project/
```

規則檔 `.cursor/rules/julia-dev.mdc` 已設 `alwaysApply: true`，所有對話生效。形態為 solo 角色內切，門禁與操作人模式保留。授權見上層 repo。""")


# ---- VS Code Copilot：自定義 agents ----

def build_copilot(members, meta):
    out = DIST / "copilot" / ".github" / "agents"
    out.mkdir(parents=True, exist_ok=True)

    allowed = {"name", "description", "tools"}
    for stem, m in members.items():
        fm = keep_keys(m["fm"], allowed)
        body = transform_body(m["body"])
        (out / f"{stem}.md").write_text(
            f"---\n{fm}\n---\n\n{body}", encoding="utf-8")

    readme_dest = DIST / "copilot"
    write_readme(readme_dest, "julia-dev · VS Code Copilot 發行版（自定義 agents）",
                 f"""版本 {meta['version']}。本目錄由 canonical 自動生成，**請勿手改**。

## 安裝

```bash
# 複製到專案（或倉庫）根目錄
cp -r .github /path/to/your-project/
```

## 形態說明

- 11 個自定義 agents（`julia-dev-team-lead` 為入口，其餘為成員）
- VS Code Copilot 目前無自動 spawn／路由：由操作人或主 agent 顯式 `@julia-dev-team-lead` 統籌，需要成員專業時顯式 `@engineer` 等
- 建議主流程：team-lead 完成 Phase 0 辨析與彙編；成員 agents 各自按其 MD 規範產出
- 門禁、測試取證、操作人模式保留；授權見上層 repo""")


def main():
    meta = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    members = load_members()
    print(f"canonical v{meta['version']} · {len(members)} agents · "
          f"{len(list(SKILLS_DIR.glob('*/SKILL.md')))} skills")
    # 原地覆蓋重建：不刪除既有 dist 檔案（確定性生成，覆蓋寫即可）；
    # 若 canonical 刪除了某 Skill，需人工清掉 dist 中對應舊目錄
    build_claude_code(members, meta)
    build_agents_md(members, meta)
    build_cursor(members, meta)
    build_copilot(members, meta)
    for d in sorted(DIST.iterdir()):
        n = sum(1 for _ in d.rglob("*") if _.is_file())
        print(f"  dist/{d.name}: {n} files")
    print("done.")


if __name__ == "__main__":
    main()
