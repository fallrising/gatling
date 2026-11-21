# 001-handoff-01　獨立複查 01

依本 run 的 [`next.md`](next.md) 執行的獨立複查。只複查，未改動 `solution.py`、`test_solution.py`、`test-output.txt` 或計畫。

## 啟動與條件

| 項目 | 內容 |
| --- | --- |
| 複查時間 | 2026-11-21T08:12:30+00:00 |
| 對話來源 | 雲端 session 的 `origin` 為 `ios`，建立於 2026-11-21T08:10:52Z，是人從手機開的新對話，沒有舊對話 |
| 人給的提示 | 自由文字：接手 gatling、讀 main 的 AGENTS.md、找交接文件、照提示完成第一輪乾淨環境交接實驗、交付 Draft PR、留下下個手機對話可用的 prompt。不是 `prompts/NEXT.md` 或 `next.md` 的原文 |
| 模型與工具 | Claude Code 雲端 session，session 設定與實際服務模型相同；Git、GitHub MCP、Python 3.13.18 |
| 平台注入的背景 | session 同時掛了 fallrising 的其他 9 個 repo，平台自動載入它們的 AGENTS.md／CLAUDE.md 與使用者帳號資訊。這些不含本題內容，但不是只有 gatling |
| 額外題意 | 無。題目、驗收、下一步全部從 repo 取得 |
| 交付分支 | `claude/quirky-ptolemy-neabog`：雲端 session 只允許推這個分支。`lab/001-handoff-01` 已合併，未再寫入 |

## 啟動條件判定

`next.md` 要求「run.json 已標為 `in_review` 且有對應 PR」。實際：`lab/001-handoff-01` head `a5557f05e3ed80bbde9e63a79ad9ea2504710d5f` 的 run.json 是 `in_review`，對應 [PR #2](https://github.com/fallrising/gatling/pull/2)，PR 已在 2026-11-21T08:09:26Z 合併到 main，合併結果 `43396de680b95ba4a9ea0303a88758b6b9784cb0`。判定條件成立：有對應 PR，只是已合併。

`next.md` 寫「不要改檔、開新 PR」，人在本次對話明確要求交付到 Draft PR。依人的較新指示，本複查以新增檔案的方式記錄，不改動原產物。

## 逐項檢查

| # | 檢查 | 結果 | 證據 |
| --- | --- | --- | --- |
| 1 | PR #2 head 與 lab 分支一致 | 通過 | PR head `a5557f05e3ed80bbde9e63a79ad9ea2504710d5f` = `origin/lab/001-handoff-01` |
| 2 | 來源 SHA 是 head 的祖先 | 通過 | `git merge-base --is-ancestor 5a0b06d6… a5557f05…` 退出 0 |
| 3 | 首次認領是從計畫基準原子提交 | 通過 | `fcfc98cb…` 的唯一 parent 是 `5a0b06d6…`，只新增 run.json，狀態 `running`、owner `codex-handoff-agent` |
| 4 | 合併後 main 與送審 head 內容相同 | 通過 | `git diff --quiet a5557f05 43396de6` 退出 0 |
| 5 | 測試只對應計畫的四組輸入輸出 | 通過 | `test_solution.py` 四個測試逐字對應計畫表格四列 |
| 6 | 在乾淨 checkout 重跑（PR head） | 通過 4/4，退出 0 | 新 clone，checkout `a5557f05…`，從 repo 根目錄執行 `python3 -m unittest discover -s runs/001-handoff-01 -p 'test_*.py' -v`；輸出存於 [`review-01-test-output.txt`](review-01-test-output.txt) |
| 7 | 在合併後 main 重跑 | 通過 4/4，退出 0 | 同一命令於 `43396de6…` |
| 8 | 受版控的 `test-output.txt` 與重跑一致 | 通過 | 除耗時外逐行相同 |
| 9 | run.json 語法與相對路徑 | 通過 | `python3 -m json.tool` 通過；`plan`、`next_prompt` 與 evidence 的 5 個路徑都存在 |

原紀錄用 Python 3.12.14，本次用 3.13.18，兩個版本結果相同。

## 判定

**程式驗收：有證據支持。** 來源可追溯，四組測試在兩個版本、兩個 commit 的乾淨 checkout 都通過。

**手機無歷史交接（第一輪實作）：證據不支持，維持 `not_tested`。** run.json 自述執行者是主代理指派的 Codex 子代理、環境是雲端全新 clone，不是人從手機開的新對話。這與 run.json 的 `strict_mobile_clean_context: not_tested` 一致，不能把第一輪當成手機樣本。

**本次複查作為交接觀察：部分支持，不是嚴格樣本。** 本次是人從手機開的新對話，提示只指向 repo，沒有舊對話。agent 只靠 repo 就判斷出第一輪已合併、下一步是 `next.md` 的複查，並完成複查。但有三項限制：

1. 交接的任務是複查，不是計畫的實作小題。
2. 提示是人手寫，不是 repo 內的入口提示原文。
3. 平台同時注入了其他 9 個 repo 的規則與帳號資訊。

而且本次已讀過第一輪的 `solution.py`，不能再當作盲做實作的樣本。

## 發現的問題

1. **合併後沒有狀態可記。** `runs/README.md` 的狀態只有 `running`、`handoff_ready`、`blocked`、`in_review`。PR #2 已合併，main 上的 run.json 仍是 `in_review`，讀者無法只從機讀紀錄知道它已被接受。
2. **計畫只容得下一個 run。** `plans/001-handoff.md` 把工作分支固定為 `lab/001-handoff-01`，並規定「已送審就交付既有 PR」。若要做嚴格手機樣本，照現行計畫新 agent 只會回報第一輪，無法開第二個 run。
3. **人的提示與交接文件衝突。** 人說「完成第一輪」「交付到 Draft PR」，但第一輪已合併，`next.md` 也禁止開 PR。agent 能從 repo 解開這個衝突，但這代表入口提示沒有涵蓋「上一輪已合併」的情況。
4. **重跑會留下未追蹤的 `__pycache__/`。** repo 沒有 `.gitignore`，跑測試後 `runs/001-handoff-01/__pycache__/` 會出現在工作樹，有被誤提交的風險。

## 待人決定

- 是否做嚴格手機無歷史的實作樣本。若要做，需要人先修訂計畫：run id 與分支（例如 `001-handoff-02`）、該 run 不得讀 `runs/001-handoff-01/` 的產物、入口提示用 repo 原文。
- 是否在 `runs/README.md` 增加合併後的狀態（例如 `accepted`），並回填 001-handoff-01。
- 是否加 `.gitignore` 排除 `__pycache__/`。

以上都改動實驗方向或格式，本次不做。
