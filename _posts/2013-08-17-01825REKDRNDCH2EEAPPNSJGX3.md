---
title: "サーバ管理/ユーザを管理する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# 手順

## ユーザ管理
### ユーザを追加する
```
# useradd <ユーザ名>
```
すぐさまユーザのパスワードを設定する。
```
# passwd <ユーザ名>
New UNIX password: （ここでパスワードを入力）
Retype new UNIX password: （ここでパスワードを再入力）
passwd: all authentication tokens updated successfully.
```
### ユーザを削除する
```
# userdel [ -r ] login
```
rオプションはホームディレクトリの削除を指示する

## グループ管理
### グループを追加する
```
# groupadd <グループ名>
```
### ユーザの所属グループを確認する
```
$ id
```
### グループを確認する
```
$ groups
```
### グループを変更する
```
# usermod -G <グループ名>[,<グループ名>] <ユーザ名>
```
### デフォルトグループを変更する
```
# usermod -g <グループ名> <ユーザ名>
```

# 参考
