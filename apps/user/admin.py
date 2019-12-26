from django.contrib import admin

# Register your models here.
from .models import UserProfile, VerifyCode, Role

admin.site.register(UserProfile)
admin.site.register(VerifyCode)
admin.site.register(Role)
