# user.views.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q

from rest_framework import serializers

from .serializers import UserSerializer

User = get_user_model()

class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            #用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'code': 20000,
        'data': {
            'token': token,
        }
    }

def user_detail(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerializer(user)
    datas = serializer.data
    datas['name'] = datas['username']
    data = {
        'code': 20000,
        'data': datas
    }
    return JsonResponse(data)

