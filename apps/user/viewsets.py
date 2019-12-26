'''
register, user viewsets, smscode
'''

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from faker import Faker

from .serializers import UserRegSerializer, SmsSerializer, UserSerializer
from .models import VerifyCode

User = get_user_model()

# ViewSets define the view behavior.
class UserRegViewSet(viewsets.ModelViewSet):
    '''用户注册'''
    queryset = User.objects.all()
    serializer_class = UserRegSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''用户数据'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('id', 'username',)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        datas['name'] = datas['username']
        data = {
            'code': 20000,
            'data': datas
        }
        return Response(data)

class SmsCodeViewset(viewsets.ModelViewSet):
    '''
    手机验证码
    '''
    queryset = VerifyCode.objects.all()
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        """
        faker = Faker()
        return faker.numerify('####')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        #验证合法
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]

        #生成验证码
        code = self.generate_code()
        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        return Response({
            "mobile": mobile,
            "code": code
        }, status=status.HTTP_201_CREATED)
