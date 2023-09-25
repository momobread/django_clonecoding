from django.db import models

# Create your models here.
#다른 model에 재사용하기 위한 blueprint다
# 원래는 model에 만들면 바로 db에 추가했지만, 얘는 그렇게 안해줄꺼임



class CommonModel(models.Model):
    
    """common model definition"""
    
    created_at = models.DateTimeField(auto_now_add=True)
    # 처음 생성되었을때를 기준으로 추가된다
    updated_at = models.DateTimeField(auto_now = True)
    # 업데이트를(저장될때 기준)할때마다 설정된다
    #https://docs.djangoproject.com/en/4.2/ref/models/fields/#datetimefield
    
    class Meta:
        abstract =True
    
    #이렇게 하면 db에 추가 안하는걸로 장고가 이해한다