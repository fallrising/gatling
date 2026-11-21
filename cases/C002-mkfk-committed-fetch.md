# C002　MKFK 的已提交讀取邊界

**狀態**　可選案例，尚待選入實驗。適合驗證接手的 agent 是否會把本機已有的資料誤算為消費者可讀的資料。

## 問題與設計

一個 partition 已將三筆資料寫到本機，只有前兩筆完成提交。消費者從 offset 1 讀取，此時應回傳第二筆，第三筆繼續留在本機。若第一筆未提交的值改變，這次讀取結果應相同。

實作一個沒有 I/O 的函式。輸入為依 offset 排列的本機字串陣列 `local`、已提交區間的右界 `hw`、起讀位置 `offset`。第一筆 offset 為 0。測試輸入保證 `hw` 為整數且 `0 ≤ hw ≤ local.length`，`offset` 為整數。成功時回傳 `records` 與 `next_offset`，範圍錯誤時回傳 `OFFSET_OUT_OF_RANGE`。函式須保留原始陣列。

1. 當 `0 ≤ offset < hw`，依序回傳 `[offset, hw)` 的全部資料。下次從最後一筆的 offset 加一開始。
2. 當 `offset == hw`，立即回傳空陣列，`next_offset` 保持原值。
3. 當 `offset < 0` 或 `offset > hw`，回傳範圍錯誤。即使該位置已寫入本機，只要超過 `hw` 仍屬越界。

## 可重跑的驗收

| local | hw | offset | 預期 |
| --- | ---: | ---: | --- |
| `["a","b","c"]` | 2 | 0 | `records=["a","b"], next_offset=2` |
| `["a","b","c"]` | 2 | 1 | `records=["b"], next_offset=2` |
| `["a","b","changed"]` | 2 | 1 | `records=["b"], next_offset=2` |
| `["a","b","c"]` | 2 | 2 | `records=[], next_offset=2` |
| `["a","b","c"]` | 1 | 2 | `OFFSET_OUT_OF_RANGE` |
| `["a"]` | 1 | -1 | `OFFSET_OUT_OF_RANGE` |
| `[]` | 0 | 0 | `records=[], next_offset=0` |

交付函式、可重跑測試及執行結果。審查時另檢查輸入陣列在成功與失敗後均保持原值。

## 摘編依據

上游為 `fallrising/newclear` 的 MKFK 教學設計。沿用已提交讀取邊界、越界錯誤與 next offset 語意。為讓小會話可獨立完成，本題固定單一記憶體 partition、立即返回、無讀取量上限，並使用合成字串。原專案另有持久化、Raft、長輪詢、位元組預算與 HTTP 規格。

| 固定來源 | Git blob SHA |
| --- | --- |
| [MKFK 設計總綱，第 4 節](https://github.com/fallrising/newclear/blob/30a5bc3c212cd912b8c507200ca041c50fc5744b/systems/mkfk/SDD.md) | `0650067060d15b9d406f382ae819253ee5b0d22d` |
| [通訊協定，Fetch](https://github.com/fallrising/newclear/blob/30a5bc3c212cd912b8c507200ca041c50fc5744b/systems/mkfk/docs/sdd/03-protocol-clients.md) | `cf703e9b172c512df4ccaae98078696a5485f37d` |
