# julia-dev · VS Code Copilot 發行版（自定義 agents）

版本 1.10.11。本目錄由 canonical 自動生成，**請勿手改**。

## 安裝

```bash
# 複製到專案（或倉庫）根目錄
cp -r .github /path/to/your-project/
```

## 形態說明

- 11 個自定義 agents（`julia-dev-team-lead` 為入口，其餘為成員）
- VS Code Copilot 目前無自動 spawn／路由：由操作人或主 agent 顯式 `@julia-dev-team-lead` 統籌，需要成員專業時顯式 `@engineer` 等
- 建議主流程：team-lead 完成 Phase 0 辨析與彙編；成員 agents 各自按其 MD 規範產出
- 門禁、測試取證、操作人模式保留；授權見上層 repo
