---
title: "障害メモ/DataTablesの「No data available in table」が邪魔"
date: 2017-10-03T18:47:22+09:00
last_modified_at: 2017-10-03T18:47:22+09:00
---

# キーワード
- DataTables
- drawCallback

# 現象

データが存在しないと次の内容の行ができてしまう。

```
No data available in table
```

# 原因

障害というか、DataTablesの仕様。

# 対策

描画後に無理やり消してやる。

```
.DataTable({
  .. options ..
  drawCallback: function(settings) {
    $('.dataTables_empty').parent().hide();
  }
});
```

# 備考

この行を出力しないためのオプションはないっぽい。

# 参考
- [drawCallback](https://datatables.net/reference/option/drawCallback) (Official)
