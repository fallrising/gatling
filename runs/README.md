# 執行紀錄

每次嘗試的機讀入口是工作分支上的 `runs/<run-id>/run.json`。認領時建立；後續接手、驗收與送審皆更新同一個檔案。尚未觀察到的結果填 `null` 或空陣列。根目錄 README 只提供導覽。

| JSON 欄位 | 內容 |
| --- | --- |
| `run_id`, `case_id`, `plan` | 此次嘗試 ID、案例 ID、計畫的 repo 相對路徑 |
| `source_sha`, `branch` | 起點的完整 commit SHA 與本次工作分支；接手後保留起始 SHA |
| `owner`, `status`, `updated_at` | 此次認領的執行者代號、目前狀態、含時區的更新時間。狀態用 `running`、`handoff_ready`、`blocked`、`in_review` 或 `accepted` |
| `conditions` | 本輪變因、固定條件、實際模型或工具、環境、額外題意、舊對話與平台注入背景的影響、是否讀過其他 run 的產物；可用 `unknown` 表示無法辨識的項目 |
| `evidence`, `outcome` | 產物的 repo 相對路徑、測試命令、退出碼、實際摘要與可回讀的證據；驗收結果及依據。狀態為 `accepted` 時，`outcome.acceptance.pull_requests` 列出已合併 PR 的網址、head 與合併 commit |
| `human_decision`, `next_prompt` | 尚待人決定的方向，沒有就填 `null`；下一份可直接貼入新對話的單一任務提示之 repo 相對路徑 |

交接提示存成同一 run 目錄下的 `next.md`。寫明 repo、工作分支、來源 SHA、要讀的證據、啟動條件、唯一任務與驗收。若方向未決，指定下一人能先做的既有工作，例如查驗本輪證據；新方向待人選定後才執行。把可貼文字一併放入交付訊息。

`accepted` 表示人已合併送審 PR，送審內容被接受；它不代表每一項判定都通過，各項結果仍以 `outcome` 為準。PR 合併後，在下一個 PR（例如接續的複查或下一個 run）回填。

從 repo 根目錄執行 `python3 tools/check_runs.py`，檢查所有 `run.json` 的語法、必填欄位、狀態、SHA 格式與相對路徑，再回讀遠端版本。只改到檢查器時另跑 `python3 -m unittest discover -s tools -v`。交付訊息以最終遠端 head SHA 標識送審版本。
