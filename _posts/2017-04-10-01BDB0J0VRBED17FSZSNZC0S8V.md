---
title: "障害メモ/SpringApplicationConfigurationが見つからない"
date: 2017-04-10T13:04:43+09:00
last_modified_at: 2017-04-10T13:04:43+09:00
---

# キーワード
- SpringApplicationConfiguration
- SpringBootTest
- Spring Boot
- ユニットテスト

# 現象

{% raw %}
```
SpringApplicationConfiguration cannot be resolved to a type
```
{% endraw %}

# 原因

@SpringApplicationConfigurationはもう使わない、ということらしい。

# 対策

@SpringApplicationConfigurationは@SpringBootTestに変更する。

# 備考

@SpringApplicationConfigurationを記載の記事が多くて焦ってしまった。依存関係の指定が足りないのか？と思ったら今はそれじゃない、ということだったようだ。

# 参考
- [Spring Boot 1.3.x の Web アプリを 1.4.x へバージョンアップする ( その４ )( build.gradle 修正後の Rebuild で出た Warning を解消する ) - かんがるーさんの日記](http://ksby.hatenablog.com/entry/2017/02/11/094253#2)
- [Spring Boot 1.4 Release Notes · spring-projects/spring-boot Wiki · GitHub](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-1.4-Release-Notes)
