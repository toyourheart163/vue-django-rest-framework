# blog.serializers.py
from rest_framework import serializers

from .models import Blog, Tag, Category, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer3(serializers.ModelSerializer):
    '''三级评论'''
    class Meta:
        model = Comment
        fields = ['id', 'parent_comment', 'content', 'created', 'user']

class CommentSerializer2(serializers.ModelSerializer):
    '''二级评论'''
    sub_comment = CommentSerializer3(many=True, required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    '''一级评论'''
    sub_comment = CommentSerializer2(many=True, required=False)
    #blog = serializers.ReadOnlyField(allow_blank=True)

    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    '''blog'''
    owner = serializers.ReadOnlyField(source='owner.username')
    #tags = TagSerializer(many=True, read_only=True)
    #comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        #fields = ('id', 'owner', 'title', 'body', 'created', 'category', 'tags')
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    '''category'''
    blogs = BlogSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

