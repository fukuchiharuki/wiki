---
title: "Java/Date型とString型を相互に変換する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- Java
- java.util.Date

# 関連
- [Java/前週や前月の開始日と終了日を計算する]({{ site.baseurl }}{% post_url 2013-08-17-01825REKDRKME2NZYPCKPKFH5E %})

# 概要
Date型のオブジェクトをString型に、またString型のオブジェクトをDate型に変換したい。

# 方法

{% raw %}
```
/** フォーマット */
static public final String DATE_PATTERN ="yyyy-MM-dd'T'HH:mm:ss";

/**
 * Date型のオブジェクトをString型に変換します.
 */
public String convertDate2String(java.util.Date date) {
  return (new SimpleDateFormat(DATE_PATTERN)).format(date);
}
	
/**
 * String型のオブジェクトをDate型に変換します.
 */
public java.util.Date convertString2Date(String source) {
  try {
    return (new SimpleDateFormat(DATE_PATTERN)).parse(source);
  } catch (ParseException e) {
    return null;
  }
}
```
{% endraw %}

# 解説
SimpleDateFormatを使うとサクッと変換することができます。

# 参考
- http://java.sun.com/javase/ja/6/docs/ja/api/java/text/SimpleDateFormat.html
- http://www.syboos.jp/java/doc/convert-string-date-by-simpledateformat.html
