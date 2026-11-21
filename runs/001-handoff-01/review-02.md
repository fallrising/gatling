# 001-handoff-01　查驗複查 01

依 [`next-after-review.md`](next-after-review.md) 唯讀查驗 [複查 01](review-01.md) 的每一項結論。查驗本身沒有改檔；本檔、測試輸出與後續修訂，是人在同一對話稍後授權開發後才提交的。

## 啟動與條件

| 項目 | 內容 |
| --- | --- |
| 查驗時間 | 2026-11-21T11:31Z 至 11:35Z |
| 對話來源 | 雲端 session 的 `origin` 為 `ios`，建立於 2026-11-21T11:30:56Z，PR #3 合併後約 35 秒。沒有舊對話 |
| 人給的提示 | 與 `next-after-review.md` 程式碼區塊原文逐字相同（以 `diff` 核對） |
| 模型與工具 | Claude Code 雲端 session；Git、GitHub MCP、Python 3.13.18 |
| 平台注入的背景 | 與複查 01 相同：同時掛載 fallrising 的其他 9 個 repo，自動載入它們的 AGENTS.md／CLAUDE.md 與帳號資訊。查驗未使用其內容 |
| 額外題意 | 無 |
| 啟動條件 | [PR #3](https://github.com/fallrising/gatling/pull/3) 的 head 分支為 `claude/quirky-ptolemy-neabog`，含 `review-01.md`，已於 2026-11-21T11:30:21Z 合併。條件成立 |
| 驗證的 head | `a82d5ebbf4daf1ccd15eed849c858c323e2b0390`；合併後 main `872a7fd9ca6d39d03dea4624fc38ab682915f71b` 的 tree 與它相同 |

## 重跑

在 scratch 目錄新 clone，detached checkout，重跑前工作樹乾淨。從 repo 根目錄執行 `python3 -m unittest discover -s runs/001-handoff-01 -p 'test_*.py' -v`：

| commit | 結果 | 退出碼 |
| --- | --- | --- |
| `a82d5eb…`（PR #3 head，指定對象） | 4/4 ok，輸出存於 [`review-02-test-output.txt`](review-02-test-output.txt) | 0 |
| `a5557f0…`（核對第 6 項） | 4/4 ok | 0 |
| `43396de…`（核對第 7 項） | 4/4 ok | 0 |

## 逐項判定

| # | 判定 | 原因 |
| --- | --- | --- |
| 1 | 同意 | GitHub API 的 PR #2 head 與 `origin/lab/001-handoff-01` 都是 `a5557f05…` |
| 2 | 同意 | `git merge-base --is-ancestor 5a0b06d6… a5557f05…` 退出 0；也是 `a82d5eb` 的祖先 |
| 3 | 同意 | `fcfc98cb…` 唯一 parent 為 `5a0b06d6…`，只新增 `run.json`，`running`／`codex-handoff-agent` |
| 4 | 同意 | `git diff --quiet a5557f0 43396de` 退出 0，兩者 tree 皆為 `9aa6acb8…` |
| 5 | 同意 | 四個測試的輸入與預期值和計畫表格一一相符，只差引號後的空格 |
| 6 | 同意 | 於 `a5557f0` 重跑 4/4，與 `review-01-test-output.txt` 逐行相同 |
| 7 | 同意 | 於 `43396de` 重跑 4/4 |
| 8 | 同意 | 三次重跑都與 `test-output.txt` 逐行相同，連耗時也一樣 |
| 9 | 同意，措辭有歧義 | 兩版 `run.json` 都通過 `json.tool`、路徑都存在。`a5557f0` 是 plan、next_prompt 加 3 個 evidence 共 5 個路徑；`a82d5eb` 光 evidence 就有 5 個 |

## 其他觀察

- 「原紀錄用 Python 3.12.14」只有 `run.json` 自述；`test-output.txt` 沒記版本，無法從產物證實。
- 複查 01 說自己的對話來源是 `ios`，那是另一個 session 的資料，只靠 repo 無法查證。
- 複查 01 的發現 1（合併後沒有狀態）與發現 4（重跑留下 `__pycache__/`）都已重現。
- `next-after-review.md` 寫「已送 Draft PR」，查驗時 PR #3 已合併，描述已過時（歷史紀錄，不改）。
- 作為交接觀察：本次提示是 repo 原文，對話由手機開啟，只靠 repo 就完成查驗。限制仍是平台注入其他 repo 的背景，而且任務是查驗，不是實作小題。

## 後續處理

人在查驗後指示「按你建議、更新、重構以及繼續開發」，以下由此授權執行，並隨同一個 Draft PR 送審：

1. 嚴格手機無歷史實作樣本：修訂 [`plans/001-handoff.md`](../../plans/001-handoff.md)，改為以 run id 區分嘗試，加入盲做規則，入口提示 [`prompts/NEXT.md`](../../prompts/NEXT.md) 改指 `001-handoff-02`。本對話已讀過第一輪產物，不能自己執行 run 02。
2. 合併後狀態：[`runs/README.md`](../README.md) 增加 `accepted`，本 run 回填兩個已合併 PR。
3. `.gitignore` 排除 `__pycache__/` 與 `*.pyc`。
4. 新增 [`tools/check_runs.py`](../../tools/check_runs.py)，把第 9 項的人工核對改成可重跑的檢查。
