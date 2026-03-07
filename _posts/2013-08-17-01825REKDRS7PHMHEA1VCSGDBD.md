---
title: "サーバ管理/RSA公開鍵認証でsshする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 手順
## sshdを設定する
- /etc/ssh/sshd_config
  - RSA公開鍵認証を有効化する
```
RSAAuthentication yes 
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```
  - rootでのログインを不可にする
```
PermitRootLogin no
```
  - パスワード認証を不可にする
```
RhostsRSAAuthentication no
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
```

## sshdをリブートする
```
# /etc/init.d/sshd restart
```

## 鍵を作成する
```
$ cd
$ mkdir .ssh
$ chmod 700 .ssh
```

```
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<ユーザ名>/.ssh/id_rsa): （ここでそのままリターン）
Enter passphrase (empty for no passphrase): （ここでパスワードを入力）
Enter same passphrase again: （ここでパスワードを再入力）
```

```
$ cd
$ cd .ssh
$ chmod 600 *
$ cat id_rsa.pub >> authorized_keys
$ rm id_rsa.pub
```

# 参考
- http://www.atmarkit.co.jp/flinux/rensai/linuxtips/432makesshkey.html
- http://gentoo.reichsarchiv.jp/item/17
