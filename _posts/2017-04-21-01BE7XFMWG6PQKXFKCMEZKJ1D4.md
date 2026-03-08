---
title: "障害メモ/DBUnitのExpectedDatabaseでテーブル数が違う"
date: 2017-04-21T18:28:58+09:00
last_modified_at: 2017-04-21T18:28:58+09:00
---

# キーワード
- DBUnit
- ExpectedDatabase

# 現象

CSVを用意して@DatabaseSetupで事前条件と@ExpectedDatabaseで事後条件をセットすると、次の失敗になる。

{% raw %}
```
junit.framework.ComparisonFailure: table count expected:<[3]> but was:<[47]>
```
{% endraw %}

ここのexpected:<[3]>はCSVで用意したテーブル数。was:<[47]>は実際のテーブル数。

# 原因

実際のテーブル数がみられている。

# 対策

@ExpectedDatabaseに検査対象のテーブルを指定する。

{% raw %}
```
@ExpectedDatabase(value="/path/to/csv/", table="your_table_name")
```
{% endraw %}

# 備考

%%複数のテーブルを検査したいときにやっぱり困る。%%<br>
→複数行@ExpectedDatabaseを書けばいいのかな？

# 参考
- [java - DBUnit Test Comparison Failure - Stack Overflow](http://stackoverflow.com/questions/21909399/dbunit-test-comparison-failure)
