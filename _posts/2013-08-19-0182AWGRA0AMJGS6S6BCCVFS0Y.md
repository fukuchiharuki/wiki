---
title: "障害メモ/qmailのsmtp接続が非常に遅い"
date: 2013-08-19T17:54:32+09:00
last_modified_at: 2013-08-19T17:54:32+09:00
---

# キーワード

- qmail
- DNS
- 逆引き
- resolv.conf

# 現象
qmail の smtp 接続がめっちゃ遅くて困る。

# 原因
接続元の確認で逆引きがどうのこうのって(ごめん、よく分ってない)。

# 対策
DNS の設定をする

- /etc/resolv.conf

{% raw %}
```
nameserver (DNSサーバー)
```
{% endraw %}

とにかくタイムアウトするようにしちゃうこともできる(1秒の試行を1回であきらめる)？

- /etc/resolv.conf

{% raw %}
```
nameserver (なにか適当に)
options timeout:1
options attempts:1
```
{% endraw %}

tcpserver のオプションで回避する手もあるらしいけどうまくいかなかった。

# 参考

- [qmailへのsmtp接続が遅い2 - てんぷろぐ](http://tmp.blogdns.org/archives/2009/07/qmailsmtp2.html)
- [特定の接続先からのみ qmail 認証が遅い場合 :: drk7jp](http://www.drk7.jp/MT/archives/000806.html)
