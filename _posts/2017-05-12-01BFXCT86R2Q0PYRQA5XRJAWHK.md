---
title: "障害メモ/JUnitがConflictingBeanDefenitionExceptionで失敗する"
date: 2017-05-12T12:56:39+09:00
last_modified_at: 2017-05-12T12:56:39+09:00
---

# キーワード

- JUnit
- FAILED
- IllegalStateException
- BeanDefinitionStoreException
- ConflictingBeanDefinitionException

# 現象

すべてのテストが次の例外で失敗する。

{% raw %}
```
    java.lang.IllegalStateException
        Caused by: org.springframework.beans.factory.BeanDefinitionStoreException
            Caused by: org.springframework.context.annotation.ConflictingBeanDefinitionException
```
{% endraw %}

# 原因

分からない。分からないがこれが起こる前にプロジェクトのフォルダ名をrenameした。

# 対策

{% raw %}
```
gradle clean
```
{% endraw %}

したら直った。

# 備考

こういうの困る。

# 参考

- [java - Spring Boot ConflictingBeanDefinitionException: Annotation-specified bean name for @Controller class - Stack Overflow](http://stackoverflow.com/questions/28498295/spring-boot-conflictingbeandefinitionexception-annotation-specified-bean-name-f)
