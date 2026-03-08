---
title: "サーバ管理/RSA公開鍵認証でsshする"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 手順
## sshdを設定する
- /etc/ssh/sshd_config
  - RSA公開鍵認証を有効化する

{% raw %}
```
RSAAuthentication yes 
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```
{% endraw %}

  - rootでのログインを不可にする

{% raw %}
```
PermitRootLogin no
```
{% endraw %}

  - パスワード認証を不可にする

{% raw %}
```
RhostsRSAAuthentication no
PasswordAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
```
{% endraw %}

## sshdをリブートする

{% raw %}
```
# /etc/init.d/sshd restart
```
{% endraw %}

## 鍵を作成する

{% raw %}
```
$ cd
$ mkdir .ssh
$ chmod 700 .ssh
```
{% endraw %}

{% raw %}
```
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/<ユーザ名>/.ssh/id_rsa): （ここでそのままリターン）
Enter passphrase (empty for no passphrase): （ここでパスワードを入力）
Enter same passphrase again: （ここでパスワードを再入力）
```
{% endraw %}

{% raw %}
```
$ cd
$ cd .ssh
$ chmod 600 *
$ cat id_rsa.pub >> authorized_keys
$ rm id_rsa.pub
```
{% endraw %}

# 参考
- http://www.atmarkit.co.jp/flinux/rensai/linuxtips/432makesshkey.html
- http://gentoo.reichsarchiv.jp/item/17
