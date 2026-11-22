# 接續提示：人決定之後（run 001-handoff-02）

**來源**　這份提示由記錄人決定的 session（`claude-code-remote:session_01KrZsT2WMaqyJrXyGsVuXYv`）寫成，存在分支 `claude/run-001-handoff-02-decision-2168ri`，和決定紀錄一起送審。讀取的基準是 main `96002e52eb4f37895562cfc919b073a21ad27ca3`，也就是複查 01 的 PR #6 的合併 commit。run 02 的來源 SHA 是 `1de672a13bf798380ef2eb414a1aebc9f096c433`。決定內容來自人在這個 session 的訊息，原文照錄於下。

**狀態**　run 02 為 `accepted`（PR #5、PR #6 都已合併）。`run.json` 的 `human_decision` 已改為 `null`，兩項待決事項都已決定：

1. **run 02 是否算嚴格手機無歷史樣本：接受。**人的理由：由手機新對話執行、入口提示逐位元組相同；開工時 `ls -R` 只列出 `runs/001-handoff-01/` 的檔名、未讀內容，題意與驗收全在計畫內，不影響解題；`review-01.md` 的 F1 是交付後人在同一對話追加的提示修改，不影響實作。已寫入 `run.json` 的 `outcome.strict_mobile_no_history_sample`。
2. **實驗 001 下一次對照的交接方式：極簡入口提示。**固定小題 `pending_ids`、角色、工具與驗收條件，只把手機貼入的入口提示縮成一句（見下方區塊）。run id、盲做規則與交付清單全部改由 repo 文件提供。run id 為 `001-handoff-03`。

**下一人能先做的既有工作**　沒有。決定 (2) 需要先改計畫與入口提示，這屬於人決定的實驗規格，agent 不自行修改 `plans/001-handoff.md` 或 `prompts/NEXT.md`，也不自行開 run 03。

**執行條件**　請人更新 `plans/001-handoff.md` 與 `prompts/NEXT.md` 後再貼入口提示。更新時至少要讓 repo 文件本身交代以下事項，因為入口提示不再提供：

- 本輪 run id 為 `001-handoff-03`，以及本輪唯一變因是入口提示縮成一句（計畫目前寫「入口提示指定本輪 run id」，與新方式不符）
- 盲做規則與 run 03 的禁讀範圍（`runs/001-handoff-01/`、`runs/001-handoff-02/` 與其分支、PR 內容）
- 交付清單：完整 commit SHA、PR 網址、Python 版本與測試結果、是否由手機開啟及依據、下一份單一任務提示、待人決定的方向
- 授權範圍：到 Draft PR，不合併、不發布
- 本 PR 與更新計畫的 PR 都要先合併到 main，run 03 從 main 讀取

更新並合併後，用手機開一個新對話。平台允許時只掛載 `fallrising/gatling`。整段貼上下面這一句，不要補充說明：

```text
請用繁體中文接手 GitHub 的 fallrising/gatling，依 prompts/NEXT.md 執行，授權到 Draft PR，不要合併或發布。
```

**仍待人決定的事**

1. 何時、如何把決定 (2) 寫進 `plans/001-handoff.md` 與 `prompts/NEXT.md`（措辭、run 03 的嚴格樣本條件是否沿用 run 02）。
2. 本 PR 合併後，是否要在 run 02 的 `outcome.acceptance.pull_requests` 回填本 PR。run 03 依盲做規則不應開啟 `runs/001-handoff-02/`，所以這次回填若需要，要另由一個非 run 03 的對話處理，或由人決定不回填。

**驗收**　計畫與 `prompts/NEXT.md` 由人更新並合併；入口提示與上方區塊逐位元組相同；run 03 的紀錄在 `runs/001-handoff-03/run.json`，`check_runs.py` 全部 `ok`。
