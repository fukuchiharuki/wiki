---
title: "障害メモ/ポート番号が使われてJBossが立ちあがらない"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 関連
- JBoss (Tomcat)
- netstat

# 現象
JBoss (Tomcat)を起動しようとすると次のエラーになる。
```
ERROR [AbstractKernelController] Error installing to Start: （どうのこうの）
java.rmi.server.ExportException: Port already in use: 1090; nested exception is: 
```

# 原因
ポート番号が既に使われているために起動できない様子。

# 対策
まずnetstatでポート番号を使っているプロセスを特定する。
```
> netstat -no

Active Connections

  Proto  Local Address          Foreign Address        State           PID
          ～省略～
  TCP    xxx.xx.xxx.xxx:1090    xxx.xx.xxx.xxx:6080    ESTABLISHED     3088
          ～省略～
```

次にタスクマネジャで該当するプロセスを殺す。<br>
netstat で State が ESTABLISH になっている場合は大丈夫かどうか確認を。

# 参考
- http://www.atmarkit.co.jp/fwin2k/win2ktips/234netstat/netstat.html
