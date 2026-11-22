# 入口提示：001-handoff-03

用手機開一個新的對話，平台允許時只掛載本 repo，貼下面那一句原文，不要補充說明。啟動前，先由人確認計畫中 run 03 的嚴格樣本條件，並將確認後的計畫與本入口提示合併到 main。

```text
請用繁體中文接手 GitHub 的 fallrising/gatling，依 prompts/NEXT.md 執行，授權到 Draft PR，不要合併或發布。
```

## 本輪任務與來源

請用繁體中文工作。這輪只做 `plans/001-handoff.md` 的 run `001-handoff-03`。只依入口提示與本 repo 文件工作，不使用其他 repo 或舊對話的資訊。

先從最新 main 讀 `AGENTS.md`、`README.md`、`plans/001-handoff.md`、`runs/README.md` 與本檔 `prompts/NEXT.md`，並核對完整來源 commit SHA。若 main 的計畫仍將 run 03 嚴格樣本條件標為待確認草案，或本次計畫與入口提示尚未合併到 main，只回報未滿足的啟動條件並停止，不自行決定或認領。

本輪唯一變因是入口提示縮成一句。固定小題 `pending_ids`、角色、工具與驗收條件均與 run 02 相同，實作與驗收以計畫為準；不為了確認這些條件而開啟 run 02 產物。

## 盲做規則

交付前不得開啟 `runs/001-handoff-01/`、`runs/001-handoff-02/` 及其分支、PR 內容，也不得開啟其他 run 的紀錄目錄、工作分支或 PR 內容；列出 PR 標題與狀態不算。這包含前次 run 的接續提示與決定紀錄，不要循連結進入。

可讀本輪入口、計畫允許的共用文件（`AGENTS.md`、`README.md`、`plans/`、`runs/README.md`、`cases/` 與 `tools/`），以及本 run 的分支、PR 與產物。若已讀到禁讀內容，照實記入 `conditions.context_limitations`，本 run 不算嚴格樣本。平台提供的記憶、額外 repo、自動載入規則或其他背景也須照實記錄，無法辨識就記為未知。

## 認領或接續

1. 查遠端預設分支、本 run 的 `lab/001-handoff-03`、相關 PR 與 `runs/001-handoff-03/run.json`，依實際狀態處理。平台只允許推送指定分支時，用該分支並在 `run.json.branch` 記錄實際名稱，不另開第二個分支。
2. 首次認領從預設分支最新 SHA 開始，依 `runs/README.md` 在工作分支原子提交 `runs/001-handoff-03/run.json`，記錄完整 `source_sha`、執行者與條件，回讀確認認領後才實作。
3. 已有分支或紀錄時，從既有分支最新 head 讀取本 run 的 `run.json` 與產物，保留原始來源 SHA。若為 `accepted`，只回報現況並停止；若已送審，直接交付既有 PR 與結果。已釋出認領或人已明確移交時，在同一分支更新執行者並從未完成項接續；他人仍在執行時，只回報現有認領位置，不另開平行嘗試。
4. 所有分支更新採非 force 的 fast-forward；遇到衝突先回讀最新 head 與認領狀態。終端認證失敗時，另行確認 GitHub app 的讀寫能力。

## 實作、驗證與送審

自行完成計畫內的實作、測試、證據回讀與 Draft PR。在 `runs/001-handoff-03/` 建立或接續 `solution.py` 與 `test_solution.py`，用 Python 3 標準函式庫與 `unittest` 驗證計畫的四組輸入輸出，不改固定小題或通過條件。

從 repo 根目錄執行，記下實際 Python 版本、輸出與退出碼：

```sh
python3 --version
python3 -m unittest discover -s runs/001-handoff-03 -p 'test_*.py' -v
python3 tools/check_runs.py
```

`check_runs.py` 依既有規則檢查所有 run JSON；只取檢查結果，不另外開啟其他 run 內容。將實際測試、額外協助、環境與限制填入本 run 的 `run.json`，不把未觀察到的結果寫成通過。回讀本 run 的產物與證據，確認結果可複查。

在同一 run 目錄寫 `next.md`，讓 `run.json.next_prompt` 指向它。下一份提示的唯一任務是獨立複查本輪四組測試與交接證據；寫明 repo、工作分支、完整來源 SHA、證據來源、執行條件與驗收，以及有沒有方向待人決定。方向未決時先做既有證據複查，新方向待人決定後才執行。

檢查紀錄後，以 main 為 base 開設或更新本 run 的同一個 Draft PR，將送審狀態記為 `in_review`。記錄與提示完成後再跑 `python3 tools/check_runs.py`，非 force 推送並回讀最終遠端 head、`run.json` 與證據，以遠端完整 commit SHA 標識送審版本。

## 交付清單與授權

- 完整 commit SHA 與 Draft PR 網址；已送審時沿用既有 PR。
- Python 版本、實際測試命令、結果與退出碼，以及可回讀的證據來源。
- 本對話是否由手機開啟：能辨識就寫依據，不能就寫「未知」，不從入口提示推定裝置。
- 可直接貼入下個手機新對話的單一任務提示全文，交代來源、執行條件及有沒有方向需要人決定，並提供 `next_prompt` 路徑。

所有變更交人審，授權只到 Draft PR，不要合併或發布。各 run 交付後，該 run 的 `run.json.next_prompt` 是接續提示入口。
