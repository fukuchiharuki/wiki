---
title: "Spring Boot/ログインユーザー情報を取得する"
date: 2017-05-30T10:35:43+09:00
last_modified_at: 2017-05-30T10:35:43+09:00
---

# キーワード
- Spring Boot
- Spring Security

# したいこと

Spring Securityでログインしたログインユーザーの情報(LoggedInUser implements UserDetails)を取得したい。

# どうやって

ControllerAdviceで@ModelAttributeをセットしておくのが楽だと思う。

```
@ControllerAdvice
public class PrincipalControllerAdvice {

	@ModelAttribute
	public LoggedInUser getLoggedInUser(Principal principal) {
		return
		Optional.ofNullable(principal)
		.filter(p -> p instanceof Authentication).map(p -> (Authentication) p)
		.map(a -> a.getPrincipal())
		.filter(p -> p instanceof LoggedInUser).map(p -> (LoggedInUser) p)
		.orElse(null);
	}

}
```

リクエストハンドラでは@ModelAttributeで取得できる。

```
@RequestMapping("/nanika")
public String nanika(
    @ModelAttribute LoggedInUser loggedInUser,
    Model model
) { /* 処理 */ }
```

# ノート

- 定形処理はアスペクトにしておくのが吉
- 毎リクエストごとにデータベースから取得するなら、<br>
ここで取得できるusernameを使ってLoadServiceを呼べばいい

# 参考
- [java - How to get active user&#39;s UserDetails - Stack Overflow](https://stackoverflow.com/questions/8764545/how-to-get-active-users-userdetails)
