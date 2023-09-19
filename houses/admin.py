from django.contrib import admin
from .models import House


# Register your models here.

#admin.register 데코레이터를 사용하여 모델을 등록한다
#이렇게 하면 관리자 페이지에서 관리 가능
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    #admin.modelAmin을 통해서 필터,검색,액션 등의 기능을 불러올 수 있다
    # pass    
    # fields = ("name","address",("price_per_night","pets_allowed"),)
    list_display = (
        #models에 있는 데이터이름과 같아야 한다
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )
    list_filter=("price_per_night","pets_allowed")
    #원하는 순서대로 입력하면 그대로 필터된다
    #search_fields = ("name__startswith",)
    #튜플에 값이 하나만 있으면 꼭 ,를 끝에 찍어줘야 튜플로 인식한다
    #무엇을 검색하고 싶나?
    #starswith로 하면 포함한 글자로 시작하는 컨텐츠를 보여준다
    #list_display_links=("name","address")
    #list_editable=("pets_allowed",)
    