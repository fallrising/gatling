# 001　新對話能否只靠 repo 接手？

**問題**　在沒有前一段聊天紀錄的環境，新 agent 能否找到目前任務、依規格完成小題，並交回足以複查的結果？這一輪只測一次文件交接。日後做對照時，固定小題、角色、工具和驗收條件，只換交接方式。

**起點**　人手動開一個新的手機對話，貼上 [prompts/NEXT.md](../prompts/NEXT.md) 中指定的入口提示原文。不附舊對話、不口頭補題目；平台允許時只掛載本 repo。agent 登記啟動時的來源 SHA、實際模型或工具，以及額外提示。平台可能提供的既有記憶、同時掛載的其他 repo 與自動載入的規則也列入限制；無法辨識就記為未知。

**各次嘗試**　每次嘗試是一個 run，ID 為 `001-handoff-NN`（兩位數，依序遞增），紀錄目錄 `runs/001-handoff-NN/`，工作分支 `lab/001-handoff-NN`。本輪 run id 由 `prompts/NEXT.md` 指定。各 run 的狀態以各自的 `run.json` 為準。`01` 由雲端子代理執行，不算手機無歷史樣本；`02` 重做同一條件，交接方式不變，所以不算新增變因。

**03 的對照**　本輪為 `001-handoff-03`，唯一變因是手機貼入的入口提示縮成一句；run id、盲做規則與交付清單改由 `prompts/NEXT.md` 提供。其餘條件和 `02` 相同，固定小題 `pending_ids`、角色、工具與驗收條件均不變。

**03 的嚴格樣本條件（人已確認）**　沿用 run 02：人從手機開新對話、只貼指定入口提示原文、不附舊對話或補充說明，平台允許時只掛載本 repo，遵守盲做規則；平台注入的背景與無法辨識的條件照實記錄，由人判定是否接受為嚴格手機無歷史樣本。人已確認沿用上述條件；這不代表 run 03 的實際結果已獲驗收。計畫與入口提示須先經人審核並合併到 main，之後才從 main 開始。

## 固定小題

用 Python 3 標準函式庫實作 `pending_ids(planned, done)`，輸入為兩個字串清單，輸出仍待辦的 ID 清單。依 `planned` 中首次出現的順序輸出，每個 ID 最多一次。出現在 `done` 裡的項目略過，額外的已完成 ID 不影響輸出。ID 依原字串精確比對。

| planned | done | 預期輸出 |
| --- | --- | --- |
| `["C","A","C","B"]` | `["A","Z"]` | `["C","B"]` |
| `[]` | `["Z"]` | `[]` |
| `["K","k"]` | `["K","K"]` | `["k"]` |
| `["X"]` | `["X"]` | `[]` |

## 執行與驗收

以下 `<run-id>` 指 `prompts/NEXT.md` 指定的 run。

0. **盲做規則。** 交付前不得開啟其他 run 的紀錄目錄、工作分支或 PR 內容（列出 PR 標題與狀態不算）；可讀 `AGENTS.md`、`README.md`、`plans/`、`runs/README.md`、`cases/` 與 `tools/`。已讀到時照實記入 `conditions.context_limitations`，該 run 不算嚴格樣本。
1. 工作分支為 `lab/<run-id>`，紀錄目錄為 `runs/<run-id>/`。核對遠端預設分支、本 run 的分支與相關 PR。首次認領以預設分支最新 SHA 為起點。平台只允許推送指定分支時，改用該分支並把實際分支記入 `run.json` 的 `branch`，不另開第二個分支。依[執行紀錄格式](../runs/README.md)在工作分支提交 `run.json`，回讀確認認領後開始。
2. 若本 run 的工作分支或 `run.json` 已存在，從最新 head 讀取 `run.json` 與現有產物。狀態為 `accepted` 時只回報並停止；已送審就交付既有 PR；可交接或使用者已明確移交就以同一分支更新認領，從未完成項接續，保留原始來源 SHA。其他執行者仍在工作時，回報現有認領位置。
3. 在紀錄目錄內建立或接續 `solution.py` 與 `test_solution.py`。用 `unittest` 逐一驗證以上四組輸入輸出，從 repo 根目錄執行 `python3 -m unittest discover -s runs/<run-id> -p 'test_*.py' -v`。
4. 在 `run.json` 填入實際測試結果、額外協助與限制。寫一份可直接貼到下一個手機對話的 `next.md`，用 `next_prompt` 指向它。接續任務為獨立複查四組測試與本輪交接證據，寫明證據來源、執行條件與待人決定的方向。執行 `python3 tools/check_runs.py` 檢查 JSON 與相對路徑，再開設或更新同一個 Draft PR，將送審狀態記為 `in_review` 並回讀最終遠端 head。

**通過條件**　有可追溯的來源 SHA，四組測試通過，新對話僅憑 repo 與入口提示完成，下一位能從機讀紀錄取得證據與單一任務。若需人補充題意，即使程式測試通過，也應記錄「需補交接資訊」。嚴格手機無歷史樣本另需：人從手機開新對話、貼入口提示原文、遵守盲做規則；平台注入的其他背景照實記錄，由人判定是否接受。

## 執行環境與成本

首輪手動啟動。日後如採用 GitHub Actions，公開 repo 使用標準 GitHub-hosted runner 的運算免費；larger runner 會計費，外部模型 API 的用量另計。排程只在預設分支執行，最短間隔五分鐘；高負載時可能延遲或遺漏，公開 repo 連續 60 天無活動時會停用排程。[GitHub Actions 計費](https://docs.github.com/en/billing/concepts/product-billing/github-actions) · [GitHub 排程事件](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)

這次觀察只回答這一題能否交接。並行認領、故障恢復與跨模型相容性另立實驗。
