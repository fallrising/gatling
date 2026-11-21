# 手機接續提示：查驗複查 01

第一輪已合併，[複查 01](review-01.md) 已送 Draft PR。要不要做嚴格手機樣本還沒決定，所以下一輪只查驗複查 01 的證據，不開新方向。下段可直接貼入新的手機對話：

```text
請用繁體中文接手 https://github.com/fallrising/gatling，只依這段提示與 repo 文件工作，不使用其他 repo 或舊對話的資訊。唯一任務：唯讀查驗 runs/001-handoff-01/review-01.md 的每一項結論。啟動條件：有一個 head 分支為 claude/quirky-ptolemy-neabog、內含 runs/001-handoff-01/review-01.md 的 PR（Draft 或已合併皆可）；找不到就只回報現況並停止。來源：第一輪送審 head a5557f05e3ed80bbde9e63a79ad9ea2504710d5f、合併後 main 43396de680b95ba4a9ea0303a88758b6b9784cb0、計畫基準 5a0b06d635900001f3d473400cc5b4b9299ab838。步驟：在新 clone 完整讀 AGENTS.md、plans/001-handoff.md、runs/README.md、runs/001-handoff-01/run.json 與 review-01.md；逐項核對「逐項檢查」表 1–9 的 SHA、祖先關係與檔案；從 repo 根目錄在該 PR 的最新 head 重跑 python3 -m unittest discover -s runs/001-handoff-01 -p 'test_*.py' -v。交付：PR 網址、驗證的完整 head SHA、Python 版本、四例結果與退出碼、每一項檢查「同意／不同意＋原因」，並說明本對話是否由手機開啟（能辨識就寫依據，不能就寫未知）。review-01.md「待人決定」的三項由我決定，不要自行執行。不要改檔、換題、開分支或 PR、合併或發布。
```

## 給人的備註

若你決定做嚴格手機無歷史的實作樣本，請先修訂 `plans/001-handoff.md`：指定新的 run id 與分支，規定該 run 不得讀 `runs/001-handoff-01/` 的產物，並更新 `prompts/NEXT.md`。修訂合併後，貼 `prompts/NEXT.md` 的原文即可，不用這份提示。
