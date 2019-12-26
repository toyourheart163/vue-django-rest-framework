# blog.models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Category(models.Model):
    '''分类'''
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    '''博客'''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.update_at = timezone.now()
        super().save(*args, **kwargs)

class Comment(models.Model):
    '''评论'''
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE, null=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录", related_name='sub_comment', default='')
    user = models.CharField(max_length=70, default='匿名')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
