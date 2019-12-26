'''
if use url_filter for filter, add `filter_fields = '__all__'`.
url_filter must kown which fields, 
if you want to search, must be set search_fields

'''
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.db.models import Q

#from django_filters.rest_framework import DjangoFilterBackend
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Blog, Tag, Category, Comment
from .serializers import (
    BlogSerializer, CategorySerializer,
    TagSerializer, CommentSerializer)
from blog.permissions import IsOwnerOrReadOnly

class BlogViewSet(viewsets.ModelViewSet):
    '''博客视图'''
    queryset = Blog.objects.all().order_by('-created')
    serializer_class = BlogSerializer
    filter_fields = '__all__'
    search_fields = ['body', 'title']
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        '''save'''
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        '''get detail'''
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        datas['category'] = Category.objects.get(pk=datas['category']).name
        print(type(datas['tags']))
        data = {
            'code': 20000,
            'item': datas
        }
        return Response(data)

    def create(self, request, *args, **kwargs):
        '''创建博客'''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'code': 20000,
            'items': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

class TagViewSet(viewsets.ModelViewSet):
    '''标签'''
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = '__all__'

class CategoryViewSet(viewsets.ModelViewSet):
    '''分类视图'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    '''评论视图'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_fields = '__all__'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'code': 20000,
            'items': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

