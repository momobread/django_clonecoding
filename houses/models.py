from django.db import models

# Create your models here.
# 이 페이지에서 데이터 타입을 설명해줘야한다
#house에 들어가있는 필드들의 데이터 타입말이다


#장고는 SQL 사용
class House(models.Model):
    
    """Model Definition for House"""
    
    name = models.CharField(max_length=30) 
    #텍스트지만 길이가 제한이 있는
    price_per_night = models.PositiveIntegerField(
        verbose_name="Price",
        #verbose_name쓰면 admin에 보여지는 타이틀을 설정할 수 있다
        help_text="Positive Numbers Only"
    ) 
    #양의정수
    description = models.TextField()
    #길이가 긴 텍스트
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True,
        help_text="Does this house allowed pets?",
        verbose_name="pets allowed??")
    
    
    
    def __str__(self):
        return self.name
    
