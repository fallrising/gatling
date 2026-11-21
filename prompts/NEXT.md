# 第一輪手機提示

基線通過人審後，複製下面整段到新的對話。已完成一輪時，工作分支上 `runs/<run-id>/run.json` 的 `next_prompt` 會指向接續提示。

```text
請用繁體中文接手 GitHub 的 fallrising/gatling，這輪只做 plans/001-handoff.md 的乾淨環境交接實驗。只依這段提示與 repo 文件工作。優先從 main 讀計畫；若計畫仍只在 setup/gatling-baseline 的 Draft PR，回報該 PR 等我審查。若我明確指定從該 PR 開始，才使用它的最新 head 另建實驗分支。讀 AGENTS.md 與計畫，查 lab/001-handoff-01、相關 PR 與 runs/001-handoff-01/run.json；依實際狀態認領或接續，保留來源 SHA。自行完成計畫內實作、測試、證據回讀與 Draft PR。若已送審，直接交付既有結果。最後給我完整 commit SHA、PR 網址、測試結果，以及能直接貼入下個手機對話的單一任務提示，交代它的來源、執行條件及有沒有方向需要我決定。所有變更交我審，授權到 Draft PR。
```
