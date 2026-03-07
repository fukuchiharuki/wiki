---
title: "MySQL/ユーザを削除する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 目標
- 表題のとおり

# 手順

```
> REVOKE ALL PRIVILEGES, GRANT OPTION FROM ユーザー名@ホスト名;
> DROP USER ユーザー名@ホスト名;
> flush privileges;
```
