---
title: "サーバ管理/ユーザを管理する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 手順

## ユーザ管理
### ユーザを追加する

{% raw %}
```
# useradd <ユーザ名>
```
{% endraw %}

すぐさまユーザのパスワードを設定する。

{% raw %}
```
# passwd <ユーザ名>
New UNIX password: （ここでパスワードを入力）
Retype new UNIX password: （ここでパスワードを再入力）
passwd: all authentication tokens updated successfully.
```
{% endraw %}

### ユーザを削除する

{% raw %}
```
# userdel [ -r ] login
```
{% endraw %}

rオプションはホームディレクトリの削除を指示する

## グループ管理
### グループを追加する

{% raw %}
```
# groupadd <グループ名>
```
{% endraw %}

### ユーザの所属グループを確認する

{% raw %}
```
$ id
```
{% endraw %}

### グループを確認する

{% raw %}
```
$ groups
```
{% endraw %}

### グループを変更する

{% raw %}
```
# usermod -G <グループ名>[,<グループ名>] <ユーザ名>
```
{% endraw %}

### デフォルトグループを変更する

{% raw %}
```
# usermod -g <グループ名> <ユーザ名>
```
{% endraw %}

# 参考
