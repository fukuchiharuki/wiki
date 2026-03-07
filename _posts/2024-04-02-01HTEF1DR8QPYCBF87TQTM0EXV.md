---
title: "Kotlin/4つ要素以上のタプルを作りたい"
date: 2024-04-02T12:53:25+09:00
last_modified_at: 2024-04-02T12:53:25+09:00
---

# キーワード
- Kotlin
- Tuple

# したいこと

PairやTripleはあるが4つ5つの要素のタプルがないので作りたい。

# どうやって

## 正攻法

素直にデータクラスを作る。

Tripleの実装と同じようにQuadrupleやQuintupleを作る。
data classにすればcomponentN()も定義されるので分解宣言できる。

```
data class Quadruple<out A, out B, out C, out D>(
    val first: A,
    val second: B,
    val third: C,
    val fourth: D
) : Serializable {
    override fun toString(): String = "($first, $second, $third, $fourth)".apply {  }
}

fun <T> Quadruple<T, T, T, T>.toList(): List<T> = listOf(first, second, third, fourth)
```

```
data class Quintuple<out A, out B, out C, out D, out E>(
    val first: A,
    val second: B,
    val third: C,
    val fourth: D,
    val fifth: E,
) : Serializable {
    override fun toString(): String = "($first, $second, $third, $fourth, $fifth)"
}

fun <T> Quintuple<T, T, T, T, T>.toList(): List<T> = listOf(first, second, third, fourth, fifth)
```

## 変化球

次のようにtypealiasと拡張プロパティでそれっぽくできる（が、分解宣言できないので正攻法のように*素直にデータクラスを作る*のがよいはず）。

```
typealias KTuple4<A, B, C, D> = Pair<Pair<Pair<A, B>, C>, D>
typealias KTuple5<A, B, C, D, E> = Pair<Pair<Pair<Pair<A, B>, C>, D>, E>

@Suppress("UNUSED", "FunctionName")
fun <A, B, C, D> KTuple(a: A, b: B, c: C, d: D): KTuple4<A, B, C, D> = a to b to c to d
@Suppress("UNUSED", "FunctionName")
fun <A, B, C, D, E> KTuple(a: A, b: B, c: C, d: D, e: E): KTuple5<A, B, C, D, E> = a to b to c to d to e

val <A, B, C, D> KTuple4<A, B, C, D>.t1
    @JvmName("tuple4t1")
    get() = first.first.first
val <A, B, C, D> KTuple4<A, B, C, D>.t2
    @JvmName("tuple4t2")
    get() = first.first.second
val <A, B, C, D> KTuple4<A, B, C, D>.t3
    @JvmName("tuple4t3")
    get() = first.second
val <A, B, C, D> KTuple4<A, B, C, D>.t4
    @JvmName("tuple4t4")
    get() = second

val <A, B, C, D, E> KTuple5<A, B, C, D, E>.t1
    @JvmName("tuple5t1")
    get() = first.first.first.first
val <A, B, C, D, E> KTuple5<A, B, C, D, E>.t2
    @JvmName("tuple5t2")
    get() = first.first.first.second
val <A, B, C, D, E> KTuple5<A, B, C, D, E>.t3
    @JvmName("tuple5t3")
    get() = first.first.second
val <A, B, C, D, E> KTuple5<A, B, C, D, E>.t4
    @JvmName("tuple5t4")
    get() = first.second
val <A, B, C, D, E> KTuple5<A, B, C, D, E>.t5
    @JvmName("tuple5t5")
    get() = second
```

### つくりかた

```
KTuple(1, 1.0, "1", true)
```

または

```
1 to 1.0 to "1" to true
```

# 参考
- [可変長タプル on Kotlin? \| KisaragiEffective.github.io](https://kisaragieffective.github.io/blog/entry/10.html)
