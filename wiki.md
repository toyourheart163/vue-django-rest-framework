---
# author: mikele
# date: 2019-12-26
---
## 一些说明

### 前端

* src/store 
用 vuex 保存状态
如 name，token
可保存在cookie中或localStorage中

* src/api
与后端api接口 使用axios

* src/router
路由，即导航的url与`*.vue`文件对接
如果太多了要分类，

### 在src/router/index引用src/router/modules

```javascript
// src/router/modules/blog.js
const blogRouter...
```

```javascript
// src/router/index.js
import blogRouter from './modules/blog'
...

export const constantRoutes = [
...
  blogRouter,
]
```

* src/components
经常使用的，封装成组件，比如comment, 三层评论

* src/filters
时间过滤

```javascript
// 使用
{{ created | parseTime }}
```

* src/layout
后台框框, 也可弄成前台框框

```vue
<navbar />
<sideBar />
<app-main />
```

* src/permission.js

判断角色是 admin or editor

* src/settings.js
标题、logo

* src/styles
全局styles
```javascript
// src/styles/element-ui.scss

// for mobile phone
@media only screen and (max-width:414px) {
  .hidden-s-only {
    display: none !important
  }
}

@media only screen and (min-width:415px) {
  .hidden-s-and-up {
    display: none !important
  }
}
```

* src/utils
请求中间件，类似python中的middleware

```javascript
// src/utils/api.js
config.headers['Authorization'] = getToken()
```

```javascript
// src/utils/auth.js
const TokenKey = 'Authorization'
...
export function setToken(token) {
  return Cookies.set(TokenKey, 'JWT ' + token)
}
```

#### 三层评论

```html
<div v-for="(item, i) in comments" :key="i" class="item">
  <Comment :comment="item" />
  <div class="item-comment">
    <div class="message">
      <!-- 第二层回复 -->
      <el-button size="small" @click="showCommentModal(item.id, item.content, 2)">回复</el-button>
    </div>
  </div>
  <div v-for="(e, i2) in item.sub_comment" :key="i2" class="item-other">
    <Comment :comment="e" />
    <!-- 第三层回复 -->
    <el-button size="small" @click="showCommentModal(e.id, e.content, 3)">回复</el-button>
    <div v-for="(j, i3) in e.sub_comment" :key="i3" class="item-other">
      <Comment :comment="j" />
    </div>
  </div>
</div>
```

```js
...
data() {
  return {
    level: null
  }
}
...
if (comment.blog) {
  // 一级评论
  this.comments.unshift(data)
  console.log('add 1 level')
} else if (this.level === 3) {
  // 三级评论
  this.comments.forEach((x, i, comments) => {
    // console.log(i, x)
    x.sub_comment.forEach((xs, j, c) => {
      // console.log(j, xs)
      if (xs.id === data.parent_comment) {
        xs.sub_comment.unshift(data)
        // console.log('add 3 level')
      }
    })
  })
  console.log('level 3')
} else if (this.level === 2) {
  // 二级评论
  this.comments.forEach((x, i, comments) => {
    if (x.id === data.parent_comment) {
      x.sub_comment.unshift(data)
      console.log('add 2 level')
    }
  })
}
```

* 对应后端三个CommentSerializer

### 后端

```zsh
# ~/.zshrc 缩短命令
alias dapp="python3 manage.py startapp"
alias pm="python manage.py"
alias dsp="django-admin startproject"
alias dev="npm run dev"
```

#### 如新建app再移到apps

`dapp comment & mv comment apps`

* apps/blog/

- serializers.py # 序列化python dict为json数据
- permissions.py # 权限配置
- pagination.py  # 自定义分页, 返回code = 20000
- viewsets.py
- models.py

* rest/router.py

```python
from rest_framework import routers

from blog.viewsets import BlogViewSet, TagViewSet, CatoryViewSet, CommentViewSet
from user.viewsets import UserViewSet, SmsCodeViewset

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet)
router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('catories', CatoryViewSet)
router.register('comments', CommentViewSet)
router.register('code', SmsCodeViewset, base_name='code')  # 模拟短信注册
```

### graphql 使用

* rest/schema.py
graphql 接口, 节省宽带的api

[`localhost:8000/graphql`](http://localhost:8000/graphql)

```javascript
// 复制到文本框，然后点运行
{
  users {
    id,
    username
  }
}
```

### swagger 前后端 api 对接文档

[docs](http://localhost:8000/docs/)

* apps/blog/viewsets.py

```python
filter_fields = '__all__' # 如果用url_filters过滤
search_fields = '__all__' # 如果要搜索q=vue
```

```python
# apps/user/models.py
    ...
    def save(self, *args, **kwargs):
        '''save username as name'''
        self.name = self.username
        super(UserProfile, self).save(*args, **kwargs)
```

* 设置`unique=True` tag 不重复

```bash
python manage.py makemigrations
python manage.py migrate
```

如果重复了，先把重复的删除掉再执行上2行命令。

```python
# apps/blog/models.py
class Tag(models.Model):
    name = models.CharField(max_length=70, unique=True)
```

* ORM操作注意事项

多对多操作取决于`ManyToManyField`在哪个model

现在来假设有个学生要找个学校读书，你得建个学校，才有对应的学校名，才能决定是哪个学校。

```python
# models.py
class Blog(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)

# ORM
tag = Tag.objects.first()
tag.blog_set.create(
    category=category, owner=user,
    body=fake.text(), title=fake.sentence()
)
```

### 部署到heroku前，要在本地测试一下。

如果不想在本地使用`postgrasql`，修改一下DATABASES，部署的时候记得修改回来。。。

```python
# rest/settings/prod.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

本地预览

```bash
heroku local
```
