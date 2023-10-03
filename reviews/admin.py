from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review
# Register your models here.

class WordFilter(admin.SimpleListFilter):
    
    title = "Filter by Words"
    
    parameter_name = "word"
    
    def lookups(self,request,model_admin):
        return [
            ("good","Good"),
            ("great","Great"),
            ("awesome","Awesome"),
            #첫번째는 url에 나타날 부분,두번째는 admin에 보여질 부분
        ]
    #def queryset(self,request,queryset): 밑에꺼랑 같은 의미임
    def queryset(self,request,reviews):
        # print(request.GET) 이렇게 url의 값을 빼올수도 있지만 밑에꺼처럼 해도된다
        print(self.value())
        word = self.value() #url에 있는 word를 준다
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews
            
            
class ratingFilter(admin.SimpleListFilter):  
    
    title = "별점필터"
    
    parameter_name="reivew_rate"
    
    def lookups(self,request,model_admin):
        return [
            ("good","좋아요"),
            ("bad","그저그래요"),
            ]
    
    def queryset(self,request,reviews):
        rate = self.value()
        print("여기입니다")
        print(self.value())
        if rate=="bad":
                return reviews.filter(rating__lt=3)
        elif rate =="good":
                return reviews.filter(rating__gte=3)
        else:
            reviews




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__",
        "payload"
    )
    
    list_filter=("rating",
                 "user__is_host",
                 "room__category", #이런식으로 fk를 이용해서 필터링 할 수 있따
                 #room의 category가 FK로 되어있다
                 #그리고 FK이니까 타고타고 넘어갈수도 있다
                 #room__category__asksdskd__ggkgkgkg
                 "room__pet_friendly",
                 WordFilter,
                 ratingFilter,
                 
                 )