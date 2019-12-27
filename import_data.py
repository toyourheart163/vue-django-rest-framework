'''
General faker data
init data
'''

__author__ = 'mikele'

import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
print(pwd)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest.settings.dev")

import django
django.setup()

from django.contrib.auth import get_user_model
from faker import Faker

from blog.models import Blog, Category, Tag
from user.models import Role

fake = Faker('zh-cn')
User = get_user_model()

if not Role.objects.first():
    roles = ['admin', 'editor']
    names = ['bar', 'foo']
    for _role, username in zip(roles, names):
        role = Role.objects.create(name=_role)
        print('create new role ' + _role)
        if not User.objects.first():
            user = role.userprofile_set.create(username=username)
            if username == 'bar':
                user.is_superuser = True
                user.is_staff = True
            user.set_password('ok')
            user.save()
    print('批量新建角色完成')

if not User.objects.first():
    user = User(username='bar')
    user.is_superuser = True
    user.is_staff = True
    user.set_password('ok')
    user.save()
    print('生成一个用户')
user = User.objects.first()

# 批量新建分类
categories = ['IT', '编程', '心理学', '管理学', '哲学']
if not Category.objects.first():
    for category in categories:
        Category.objects.create(name=category)
    print('批量新建分类完成')

# 批量新建标签
tags = [
    'vue', 'django', 'rest_framework',
    'axios', 'vuex', 'elementUI',
    'vue-router', 'JWT'
]

if not Tag.objects.first():
    for tag in tags:
        instance = Tag(name=tag)
        instance.save()
    print('批量新建标签完成')

tags = Tag.objects.all()
categories = Category.objects.all()

# 批量新建博客
if not Blog.objects.first():
	for tag in tags:
	    for category in categories:
	        tag.blog_set.create(
	            category=category, owner=user,
	            body=fake.text(), title=fake.sentence()
	        )
	print('批量新建博客完成')
