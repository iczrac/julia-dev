# julia-dev · Claude Code 發行版（完整團隊形態）

由 Julia 統籌的 11 位成員軟體開發專家團，版本 1.10.10。本目錄由 canonical 自動生成（`python3 scripts/build_dist.py`），**請勿手改**。

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
- 來源與授權見 `skills/*/ATTRIBUTION.md` 與上層 repo 的 `LICENSE`、`README.md`（致謝節）
