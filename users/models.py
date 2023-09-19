from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#django의 모든것을 상속해서 한다 
# models.Models을 사용하면 직접 처음부터 만들어야함

#models를 변경할때마다 migrations을 하고 migrate를 다시 해야함
# =>python코드에 있는 모델구조와 DB를 동기화하기 위해서 그렇다
class User(AbstractUser):
    # 건드리고 싶지 않은 필드는 editable하면 안됨(어차피 관리자 페이지에 안나타남 /#5-2)
    first_name = models.CharField(max_length =150,editable=False)
    last_name = models.CharField(max_length=150,editable=False)
    name = models.CharField(max_length=150)
    is_host = models.BooleanField(default=True)
    
    