---
title: "シェル/シェルスクリプトのあるディレクトリに移動する"
date: 2013-12-04T17:53:26+09:00
last_modified_at: 2013-12-04T17:53:26+09:00
---

# キーワード

- dirname
- $0

# 概要
実行したシェルスクリプトのあるディレクトリに移動します。なお、移動はシェルスクリプト実行中だけで実行後は元に戻っています。

# 方法

- dir/sample.sh

{% raw %}
```
cd `dirname $0`
./echo.sh
```
{% endraw %}

- dir/echo.sh

{% raw %}
```
echo echo
```
{% endraw %}

次の実行結果を得ます。

{% raw %}
```
$./dir/sample.sh
echo
$
```
{% endraw %}

# 解説

<dl>
<dt>dirname</dt>
<dd>ファイルパスからファイル名を取り除いて親ディレクトリパスだけを抜き出します。</dd>
<dt>$0</dt>
<dd>実行中のコマンド名(シェルスクリプト名)です。</dd>
</dl>

# 参考

- [[Shell] $(cd $(dirname $0) &amp;&amp; pwd) を理解する \| それなりブログ](http://blog.kjirou.net/p/506)
