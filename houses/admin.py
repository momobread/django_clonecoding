from django.contrib import admin
from .models import House


# Register your models here.

#admin.register 데코레이터를 사용하여 모델을 등록한다
#이렇게 하면 관리자 페이지에서 관리 가능
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    #admin.modelAmin을 통해서 필터,검색,액션 등의 기능을 불러올 수 있다
    pass    