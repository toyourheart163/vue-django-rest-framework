from rest_framework import routers

from blog.viewsets import BlogViewSet, TagViewSet, CategoryViewSet, CommentViewSet
from user.viewsets import UserViewSet, SmsCodeViewset

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet)
router.register('users', UserViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register('comments', CommentViewSet)
router.register('code', SmsCodeViewset)
