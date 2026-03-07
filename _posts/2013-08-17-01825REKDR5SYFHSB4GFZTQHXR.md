---
title: "障害メモ/EclipseからJBossを起動すると例外が起こる"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JBoss
- Eclipse

# 現象
EclipseからJbossを起動すると以下の例外が起こる。
```
ERROR [AbstractKernelController] Error installing to Instantiated: ...
```

## 詳しい状況
- JBoss 6 を JBoss 5 のサーバ設定で動かしている。
- これはEclipseにテンプレートが存在しなかったため。

# 原因
EclipseがJVMのオプションをいい感じにしてくれていない。

# 対策
サーバ設定のテンプレートを作成してくれている人がいるので使わせてもらう。
- http://www.cs.hs-rm.de/~knauf/public/index.html

# 参考
- http://community.jboss.org/thread/160526
