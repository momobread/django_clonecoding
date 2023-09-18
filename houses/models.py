from django.db import models

# Create your models here.
# 이페이지에서 데이터 타입을 설명해줘야한다
#house에 들어가있는 필드들의 데이터 타입말이다

class House(models.Model):
    """Model Definition for House"""
    
    name = models.CharField(max_length=140) 
    #텍스트지만 길이가 제한이 있는
    price = models.PositiveIntegerField() 
    #양의정수
    descirption = models.TextField()
    #길이가 긴 텍스트
    address = models.CharField(max_length=140)
    
    
    
     