# gatling

fallrising 的多 agent 協作實驗庫。人決定問題、規格、驗收條件與框架方向，agent 負責實作、測試及交接。

## 從手機開一輪實驗

開一個新的對話，貼上[入口提示](prompts/NEXT.md)原文。接續已開始的實驗時，先讀工作分支上的 `runs/<run-id>/run.json`；一輪交付後，可直接複製紀錄中 `next_prompt` 所指的提示。

| 想知道什麼 | 從哪裡讀 |
| --- | --- |
| 本輪固定什麼、如何驗收 | [實驗 001　乾淨環境交接](plans/001-handoff.md)（含各 run 的分支與盲做規則） |
| 開 PR 後遺失交接網址，能否自行接手 | [實驗 002 計畫](plans/002-pr-recovery.md) · [觀察者啟動提示](runs/002-pr-recovery-01/next.md) |
| 從既有 SDD 選一題 | [案例與選題說明](cases/README.md) · [公開規格目錄](cases/catalog.json) · [18 個私有來源的離線題](cases/curated-private/README.md) |
| 某次嘗試的狀態、證據及下一步 | [執行紀錄格式](runs/README.md) |
| 分工、認領與送審方式 | [協作規則](AGENTS.md) |
| 檢查所有執行紀錄 | 從 repo 根目錄跑 `python3 tools/check_runs.py`（[檢查器](tools/check_runs.py)） |
