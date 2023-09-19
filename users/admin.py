from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # User의 root
from .models import User #users models의 내가 만든 Uesr를 쓴다고 알려줘야함
# => admin register에 등록하기 위해서

# Register your models here.
# class CustomUserAdmin(admin.ModelAdmin) => 이것은 새로운 모델을 등록했을때

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
