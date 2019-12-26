# user.models.py

'''
Save username as name for frontend.
'''

from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    """
    用户角色，作为权限判断。
    """
    name = models.CharField(max_length=10, verbose_name="角色名")

    def __str__(self):
        return self.name

class UserProfile(AbstractUser):
    """
    user profiles
    """
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )
    #用户用手机注册，所以姓名，生日和邮箱可以为空
    name = models.CharField("姓名",max_length=30, null=True, blank=True)
    avatar = models.URLField('头像', default="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif")
    introduction = models.CharField('介绍', max_length=200, default="还没来得及介绍。。")
    roles = models.ManyToManyField(Role, blank=False)
    birthday = models.DateField("出生年月",null=True, blank=True)
    gender = models.CharField("性别",max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话",max_length=11,null=True, blank=True,help_text='手机号')
    email = models.EmailField("邮箱",max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        '''save username as name'''
        self.name = self.username
        super(UserProfile, self).save(*args, **kwargs)

class VerifyCode(models.Model):
    """
    短信验证码,回填验证码进行验证。可以保存在redis中
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.title
