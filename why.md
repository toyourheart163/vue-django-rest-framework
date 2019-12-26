---
# Title: Think
# author: mikele
# date: 2019-12-25
tags: [What, How, Why]
---

## 一些疑问

#### what
为什么导航到404后就清除了token。
不要清除

#### How
save `username = name`

#### Why

because frontend `Cookie.set('name', name)`
so backend must offer name not username.

### csrftoken

这是要自己生成的节奏吗？
当请求的port相同时才看到csrftoken
因为都设置到cookies.set的是port

### 使用了watch就不要使用created，避免重复请求数据。

### 准备部署时看到好多配置文件，就不能放在一个文件里吗？