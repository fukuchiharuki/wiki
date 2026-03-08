---
title: "障害メモ/Jekyllの時間がずれる"
date: 2017-04-10T10:13:50+09:00
last_modified_at: 2017-04-10T10:13:50+09:00
---

# キーワード

- Jekyll
- timezone
- 時間
- ずれ

# 現象

作成日や更新日がずれて表示される。

# 原因

タイムゾーンの設定が正しくないから。

# 対策

__config.ymlに次を追記する。

{% raw %}
```
timezone: Asia/Tokyo
```
{% endraw %}

# 備考

timezoneに何を設定できるのかは参考のリンクで。

# 参考

- [Configuration \| Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/configuration/)
- [List of tz database time zones - Wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
