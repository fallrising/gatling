# 接續提示：獨立複查 001-handoff-02

**來源**　由 run `001-handoff-02` 的執行者寫成，存在分支 `claude/gatling-001-handoff-02-ittju6`。本 run 的 Draft PR 送審時，此檔與 `runs/001-handoff-02/run.json` 一起提交；PR 網址、送審 head 寫在 `run.json` 的 `outcome.pull_request`。來源 SHA `1de672a13bf798380ef2eb414a1aebc9f096c433`（main，認領起點）。

**執行條件**　由人用手機開一個新對話，平台允許時只掛載 `fallrising/gatling`，貼上下面整段原文，不補充說明。可以在 PR 合併前或合併後執行，提示內已寫好兩種情況的讀取位置。

**待人決定的方向**　有。(1) 平台注入的背景與 run 02 開工時列出的其他 run 檔名，是否仍接受本 run 為嚴格手機無歷史樣本，見 `run.json` 的 `human_decision`。(2) 實驗 001 下一步要換哪種交接方式做對照，計畫尚未指定。這兩項都由人決定；複查者只查驗既有證據，不開新 run、不改計畫。

```text
請用繁體中文接手 GitHub 的 fallrising/gatling，這輪只做一件事：獨立複查 plans/001-handoff.md 的 run 001-handoff-02。只依這段提示與 repo 文件工作，不使用其他 repo 或舊對話的資訊。先從 main 讀 AGENTS.md、plans/001-handoff.md 與 runs/README.md。若 main 已有 runs/001-handoff-02/run.json 就從 main 讀；否則從分支 claude/gatling-001-handoff-02-ittju6 的最新 head 讀。除 runs/001-handoff-02/ 外，不要開啟其他 run 的紀錄目錄、分支或 PR 內容；列出 PR 標題與狀態可以。複查內容：記下讀取的完整 head SHA，核對 run.json 的 source_sha 是否存在於 main 歷史、branch 與 PR 是否相符；在 repo 根目錄重跑 python3 -m unittest discover -s runs/001-handoff-02 -p 'test_*.py' -v，並另寫腳本對照計畫的四組輸入輸出，記錄 Python 版本、退出碼與完整輸出；比對 test-output.txt、run.json 的 evidence 與 outcome 是否與實際一致；檢查 conditions 中的平台背景與限制記錄是否足以讓人判斷是否為嚴格樣本，不替人下判定。只新增 runs/001-handoff-02/review-01.md 與 runs/001-handoff-02/review-01-test-output.txt，不改 solution.py、test_solution.py、run.json 或計畫。執行 python3 tools/check_runs.py。在平台指定的工作分支提交並推送（非 force），以 main 為 base 開一個 Draft PR，回讀遠端 head。最後給我完整 commit SHA、PR 網址、Python 版本與測試結果、是否由手機開啟（能辨識就寫依據，不能就寫未知）、複查發現，以及 run.json 中 human_decision 列出待我決定的方向。所有變更交我審，授權到 Draft PR，不要合併或發布。
```

**驗收**　`review-01.md` 列出讀取的完整 head SHA、重跑命令、Python 版本、退出碼與四組結果；逐項說明 run.json 的證據是否吻合；`tools/check_runs.py` 全部 `ok`；Draft PR 已開且遠端 head 回讀一致。
