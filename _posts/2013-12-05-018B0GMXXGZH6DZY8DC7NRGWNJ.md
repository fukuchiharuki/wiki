---
title: "サーバ管理/nfs設定する"
date: 2013-12-05T13:35:58+09:00
last_modified_at: 2013-12-05T13:35:58+09:00
---

# キーワード
- nfs
- UID
- GID

# 概要
マウントされる側とする側の設定をします。

# 方法
## マウントされる側

### マウントされるディレクトリを作成する

{% raw %}
```
# mkdir -p /var/nfs/hoge
```
{% endraw %}

### パーミション設定する
ここはマウントする側のUIDとGIDに合わせます。

{% raw %}
```
# chown -R 500:500 /var/nfs/hoge
```
{% endraw %}

### マウントされる口を空ける
- /etc/exports

{% raw %}
```
/var/nfs  192.168.100.*/255.255.255.0(rw,no_root_squash)
```
{% endraw %}

### nfsを起動する
既に起動しているなら restart します。

{% raw %}
```
# /etc/init.d/nfs start
```
{% endraw %}

## マウントする側

### マウントポイントを作成する

{% raw %}
```
# mkdir /var/moge
```
{% endraw %}

### 起動時にマウントするように設定する

- /etc/fstab

{% raw %}
```
{ホスト名}:/var/nfs/hoge /var/moge nfs rw 0 0
```
{% endraw %}

### 今すぐマウントする

{% raw %}
```
# mount -a
```
{% endraw %}

# 解説

パーミションの設定が少し厄介です。名前ではなくUIDやGIDが同じでなければいけません。別の言い方をするとUIDやGIDが同じでなければ同じ名前でもだめです。なので、サーバ構成を考えるときにはユーザー名とともに番号も考えておくとよいと思います。
