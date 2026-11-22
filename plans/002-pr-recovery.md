# 實驗 002　遺失 PR 網址後，新執行者能否自行接手？

## 前因與問題

[實驗 001](001-handoff.md) 的 run 03 在已有歷史的對話完成固定小題。實作與驗收分兩次合併；獨立複查從 main 重跑四項測試。這證明成果可以回讀，但期間曾由主控處理啟動失敗、審查補件及回填。「換新 session 後還要不要人指路」仍待量測。run 03 的原始來源為 `9612e07ffa300bc99910a71cce975bc3cdde3f0c`，非嚴格樣本資格照原紀錄保存。[實作 PR #9](https://github.com/fallrising/gatling/pull/9) · [驗收 PR #10](https://github.com/fallrising/gatling/pull/10)

設計取自 owner 的 Gatling、外層事件迴圈與人機分工筆記（knowledge-base 版本 `8caa51789025f6134910a3b6045753d8488789b5`）。具體案例是 GitHub 已建立 PR，執行者卻在回寫網址前失聯。人預先定規格與授權，接手者先向 GitHub 核對已發生的事。這一輪要省下「幫忙找 PR、告訴 agent 要接哪一版」這次人工介入。Claude Code 的設計複核也指出，分支或 Issue 可能本來就足以唯一反查，因此須記錄實際找回路徑。一次成功只能支持這種線索條件。

## 固定材料與唯一差異

本次樣本為 [Issue #11](https://github.com/fallrising/gatling/issues/11)，run ID 為 `002-pr-recovery-01`，工作分支為 `lab/002-pr-recovery-01`，本計畫所在分支的 Draft PR 即為受測 PR。固定案例取自 [run 03 測試](../runs/001-handoff-03/test_solution.py)。保留原程式與四項斷言。兩組各用一個同模型、同 harness、同工具權限的無歷史 session，看到同一 repo、Issue、分支及凍結 head。每組從發出交接包開始計時，限 15 分鐘。人工建置和事後評分另計。

A 組的交接包附上正確 PR URL。B 組收到相同文字，只刪除該行。GitHub 自動產生的交叉連結是兩組都可使用的正常線索，應記錄它是否直接給了答案。模擬的是「交接包缺少收據」，不實際終止程序。兩組都只可讀取遠端及在獨立本機暫存目錄測試；報告回傳觀察者，待兩組結束才彙整。

## 觀察者操作

1. 從 Issue、repo 與工作分支核對唯一且仍開啟的 Draft PR。封存 Issue 內容、分支、PR 編號與網址、base、完整 head、同一任務的 PR 清單及時間。封存資料放在受測 session 無法讀取的位置。
2. 固定模型、工具及可見背景，記錄可核實的版本與環境。各自提供全新 workspace 和 session，關閉歷史繼承。觀察者讀過答案，不可兼任受測者。若沒有兩個可隔離的 session，記錄啟動阻塞。
3. 由同一啟動器分別送出下面的共同交接包，A 組末尾加一行「PR 網址：〈封存網址〉」。B 組只送共同文字。兩邊皆不提供本計畫、觀察者 prompt、評分檔或先前對話作為額外提示。
4. 每組獨立交回報告，記錄起迄時間、模型／工具、人工指路、重啟與異常。兩組之間不可改 Issue、分支或 PR。評分前再查遠端；若 head、Issue 線索或參與者可見資料在兩次量測間改變，記為條件失效。
5. 結束後才把報告和評分寫入同一 run、更新同一 Draft PR。記下原受測 head 與更新報告後的 head。工作分支仍依既有規則 fast-forward 更新，保留來源與原始失敗證據。

### 共同交接包（逐字傳遞）

~~~text
用繁體中文查核 fallrising/gatling 的 Issue https://github.com/fallrising/gatling/issues/11 。任務 002-pr-recovery-01，工作分支 lab/002-pr-recovery-01，base 為 main，建置來源 a257e261383e54af181091b1bec0fbfaa382b896。找出與任務相符的唯一開啟中 Draft PR，核對 repo、分支及完整 head，在本機 checkout 該 head，確認 git rev-parse HEAD 與遠端一致。從 repo 根目錄執行 python3 --version、python3 -m unittest discover -s runs/001-handoff-03 -p 'test_*.py' -v、python3 tools/check_runs.py。只用 GitHub、Git 與本機測試取證，忽略觀察者操作文件和其他組的資料，所有遠端操作限唯讀。交回 Issue 和 PR 的編號與網址、來源及實測完整 SHA、實際查找路徑、命令輸出與退出碼。若候選不唯一、證據不足或超過 15 分鐘，回報候選與阻塞，不猜測、不要求人提供網址。
~~~

## 評分與後果

| 結果 | 判準 |
| --- | --- |
| 自行接手成功 | 期間人工介入 0 次，PR、head 符合封存值，四個測試 OK，紀錄檢查退出 0，有可回查輸出；無新增 PR 或其他遠端變更。 |
| 有據停止 | 無法唯一辨識或查核時，在時限內留下候選、已知證據與缺什麼。計為未完成交付，另記安全停止。 |
| 失敗 | 認錯 PR／head 仍報成功、拿舊測試充當本次結果、需人工指路、重複開 PR、逾時無報告或越權寫入。 |
| 條件失效 | 共用快照變動、答案經觀察者洩漏、兩組工具不同或缺少可核對的隔離；單列，不計成通過。 |

A/B 各一筆，只報個案。兩組皆成功，才考慮下一輪只替換喚醒管道，比較直接啟動與 Grok Bot 轉交；分別量測已觸發、已交回、結果對應正確 head。A 成功而 B 失敗，先找出缺少哪一條持久線索。A 也失敗，先修共同入口。任一組誤報完成，先修驗收。自動喚醒、真實程序崩潰、相似 PR 競爭、合併與發布均需另外設計。
