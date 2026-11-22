# 執行入口：001-handoff-03 流程演練

人已改為在目前對話先走通流程，暫不做手機操作；本輪是非嚴格樣本，不是極簡入口對照。以下保留單句入口供查詢或接續本 run；它不會自動開啟新實驗。新對話只有此句時，授權仍只到 Draft PR；目前對話另有人的明確提交及合併授權。

```text
請用繁體中文接手 GitHub 的 fallrising/gatling，依 prompts/NEXT.md 執行，授權到 Draft PR，不要合併或發布。
```

## 本輪任務與來源

請用繁體中文工作。這輪只做 `plans/001-handoff.md` 的 run `001-handoff-03`。本次沿用既有對話，必須記錄已存在的背景與額外協助，不宣稱無歷史或只依 repo 工作；實作仍以本 repo 的固定小題為準。

先從最新 main 讀 `AGENTS.md`、`README.md`、`plans/001-handoff.md`、`runs/README.md` 與本檔 `prompts/NEXT.md`，並核對完整來源 commit SHA。本次由人授權在同一工作分支更新方向與認領；接續時再讀本 run 分支最新紀錄，不改寫原始來源 SHA。

固定小題 `pending_ids` 與四組輸入輸出以計畫為準；本次加入 Claude Code 技術審查並沿用對話，不作單一變因比較，不為了比較而開啟 run 02 產物。記錄實際流程缺口，但不在本輪修訂共用框架。

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

所有變更交人審；只有單句入口時授權到 Draft PR，不要合併或發布。目前對話已有人的明確合併授權，可在驗證與審查完成後合併本次 PR；此授權不得推廣為未來對話的自動合併規則。交付後，該 run 的 `run.json.next_prompt` 是接續提示入口。合併後依 `runs/README.md` 在下一個 PR 回填本 run 的 acceptance，不動其他 run。
