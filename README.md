# vue-django-rest-framework

This is a example for an application using Vue and Django.

* 使用 Element UI 搭建前端模板
* 后端使用 django-rest-framework 提供 api
* swagger 前后端 api 对接文档

## 已实现的功能

* 三层评论
* JWT 登陆
* faker 模拟数据，比前端的Mock更强大
* api操作，前端使用axios， 后端使用rest_framework
* 标签云
* Timeline

推荐使用httpie替代curl操作api, 非常简单

```bash
http :8000/api/
http -a bar:ok :8000/api/blogs/  # 获取需要登陆的数据
http :8000/api/tags/ name=vue  # post 操作
```

[rest_framework](https://www.django-rest-framework.org)官网有很多好东西。文档也写得很好，注释了很多需要的东西。

## 使用说明

Setup
```
$ npm install
$ pip install -r requirements.txt
$ python manage.py migrate
```

```
$ python manage.py runserver
```
[`localhost:8000`](http://localhost:8000/)

另一个终端窗口

```
npm run dev
```
[`localhost:9528`](http://localhost:9528/)

swagger 前后端 api 对接文档
[docs](http://localhost:8000/docs/)

```
$ npm run build:prod
$ python manage.py runserver
```

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser username=bar
python manage.py changepassword bar  # 因为改写了 AUTH_USER_MODEL = 'user.UserProfile'
```

## Deploy

* Set `ALLOWED_HOSTS` on [`rest.settings.prod`](/rest/settings/prod.py)

### Heroku Server

记得替换 `django-vue-template-demo`
```
$ heroku apps:create django-vue-template-demo
$ heroku git:remote --app django-vue-template-demo
$ heroku buildpacks:add --index 1 heroku/nodejs
$ heroku buildpacks:add --index 2 heroku/python
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=rest.settings.prod
$ heroku config:set DJANGO_SECRET_KEY='...(your django SECRET_KEY value)...'

$ git push heroku
```

### Includes

* Django
* Django REST framework
* Django Whitenoise, CDN Ready
* Vue CLI 3
* Vue Router
* Vuex
* Element UI
* Gunicorn
* Configuration for Heroku Deployment
* rest_framework_swagger  # api 文档
* rest_framework_jwt  # JWT json 认证
* url_filter  # 使用 url 来搜索
* corsheaders  # 跨域使用
* debug_toolbar  # django debug 查看 ORM 过程
* graphene_django  # 比纯 api 节省宽带

### 文件夹目录

```
LICENSE
Pipfile
Procfile
README-backend.md  # 后端模板
README-zh.md  # 前端模板
README.md
app.json
apps
babel.config.js
build
jest.config.js
jsconfig.json
manage.py
mock
package-lock.json
package.json
postcss.config.js
public
rest
runtime.txt
requirements.txt
src
tests
todo.md
vue.config.js
why.md  # 一些思考过程
```

src/views/demo 用来练习

[后端模板](https://github.com/gtalarico/django-vue-template)
[README-backend](./README-backend.md)

[前端模板](https://github.com/PanJiaChen/vue-admin-template)
[README-zh](./README-zh.md)

##### Heroku One Click Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gtalarico/django-vue-template)
