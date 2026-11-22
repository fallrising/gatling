# 下一個對話：擔任實驗 002 觀察者

以下整段交給觀察者。A/B 受測者的輸入由計畫內的共同交接包產生。

~~~text
請用繁體中文擔任 fallrising/gatling 實驗 002 的觀察者。由 Issue #11 與遠端分支 lab/002-pr-recovery-01 接手，先回讀 AGENTS.md、plans/002-pr-recovery.md、runs/002-pr-recovery-01/run.json。沿用既有 Draft PR 與原認領，先確認狀態與尚未執行的組別。依計畫封存遠端真值，使用兩個無歷史、互相隔離、同設定的 session 分別執行 A/B；只傳指定交接包。保存各組獨立輸出，核對完整 SHA、測試退出碼、人工介入與遠端副作用，再於同一 Draft PR 彙整。若已完成就回報既有結果；若無法隔離或凍結條件就記錄阻塞。授權到更新這個 Draft PR，不合併、不發布，本次不啟動 Grok。
~~~
