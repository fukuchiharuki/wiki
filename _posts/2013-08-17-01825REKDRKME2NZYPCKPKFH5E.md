---
title: "Java/前週や前月の開始日と終了日を計算する"
date: 2013-08-17T18:07:15+09:00
last_modified_at: 2013-08-17T18:07:15+09:00
---

# キーワード
- Java
- Calendar
- java.util.Date

# 関連
- [Java/Date型とString型を相互に変換する]({% post_url 2013-08-17-01825REKDRD4NZHM3GSCNV8DVW %})

# 概要
今日を基準日として、前週や前月の開始日と終了日を計算します。 <br>
※月曜始まりとする

# 方法
まずはこれだけ用意して、
```
Calendar today = Calendar.getInstance();
Calendar start = Calendar.getInstance();
Calendar end = Calendar.getInstance();
today.setTime(new java.util.Date());
```

## 今週
```
int diff = (today.get(Calendar.DAY_OF_WEEK) + 5) % 7;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
end.setTime(start.getTime());
end.add(Calendar.DATE, 6);
```

## 前週
```
int diff = (today.get(Calendar.DAY_OF_WEEK) + 5) % 7 + 7;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
end.setTime(start.getTime());
end.add(Calendar.DATE, 6);
```

## 前々週
```
int diff = (today.get(Calendar.DAY_OF_WEEK) + 5) % 7 + 7*2;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
end.setTime(start.getTime());
end.add(Calendar.DATE, 6);
```

## 今月
```
int diff = (today.get(Calendar.DATE)) - 1;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
end.setTime(start.getTime());
end.add(Calendar.MONTH, 1);
end.add(Calendar.DATE, -1);
```

## 前月
```
int diff = (today.get(Calendar.DATE)) - 1;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
start.add(Calendar.MONTH, -1);
end.setTime(start.getTime());
end.add(Calendar.MONTH, 1);
end.add(Calendar.DATE, -1);
```

## 前々月
```
int diff = (today.get(Calendar.DATE)) - 1;
start.setTime(today.getTime());
start.add(Calendar.DATE, -diff);
start.add(Calendar.MONTH, -1*2);
end.setTime(start.getTime());
end.add(Calendar.MONTH, 1);
end.add(Calendar.DATE, -1);
```

<br>
最後に、
```
start.set(Calendar.HOUR_OF_DAY, 0);
start.set(Calendar.MINUTE, 0);
start.set(Calendar.SECOND, 0);
end.set(Calendar.HOUR_OF_DAY, 23);
end.set(Calendar.MINUTE, 59);
end.set(Calendar.SECOND, 59);
```

# 解説
[Calendar#add(int, int)](http://e-class.center.yuge.ac.jp/jdk_docs/ja/api/java/util/Calendar.html#add%28int,%20int%29)で足したり引いたりするだけです。
最初の引数で月や日を選択することができるので割と自在です。

# 参考
- http://e-class.center.yuge.ac.jp/jdk_docs/ja/api/java/util/Calendar.html
