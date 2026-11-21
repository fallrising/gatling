# 手機接續提示：獨立複查 001

下段可直接貼入新的手機對話：

```text
請用繁體中文獨立複查 https://github.com/fallrising/gatling 的第一輪交接證據。啟動條件：lab/001-handoff-01 分支的 runs/001-handoff-01/run.json 已標為 in_review 且有對應 PR；否則只回報現況，不另開分支或 PR。來源基準是 main 的 5a0b06d635900001f3d473400cc5b4b9299ab838。先在乾淨 checkout 查 PR 與最新 head，核對來源 SHA 是其祖先，完整讀 AGENTS.md、plans/001-handoff.md、runs/README.md 和該 run.json，再按其 evidence 逐項檢查受版控的產物，從 repo 根目錄重跑 python3 -m unittest discover -s runs/001-handoff-01 -p 'test_*.py' -v。只做複查，交付 PR 網址、驗證的完整 head SHA、四例結果與退出碼，並分別判定「程式驗收」與「手機無歷史交接」是否有證據支持。若證據不能支持後者，不算已通過，由我決定是否另做嚴格手機樣本。不要改檔、換題、開新 PR、合併或發布。
```
