from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#django의 모든것을 상속해서 한다 
# models.Models을 사용하면 직접 처음부터 만들어야함

#models를 변경할때마다 migrations을 하고 migrate를 다시 해야함
# =>python코드에 있는 모델구조와 DB를 동기화하기 위해서 그렇다
class User(AbstractUser):
    
    class GenderChoices(models.TextChoices):
        MALE = ("male","Male") #첫번째는 DB에 들어갈 value, 두번째는 label
        FEMALE = ("female","Female")
    
    class LanguageChoices(models.TextChoices):
        KR = ("kr","Korea")
        EN = ("en","English")
    
    class CurrencyChoices(models.TextChoices):
        WON = ("won","Korean Won")
        USD = ("usd","Dollar")
        
        
    # 건드리고 싶지 않은 필드는 editable하면 안됨(어차피 관리자 페이지에 안나타남 /#5-2)
    first_name = models.CharField(max_length =150,editable=False)
    last_name = models.CharField(max_length=150,editable=False)
    avator = models.ImageField(blank=True) 
    #blank=True는 필드가 필수로 설정 안되게 한다
    name = models.CharField(max_length=150,default="")
    is_host = models.BooleanField(default=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    #GENDER = (
    #("male", "Male"),
    #female", "Female")
    #) 이렇게 튜플 변수를 만들어서 해도 됨
    
    language_A = models.CharField(
        max_length=2,choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,choices=CurrencyChoices.choices,
        #models.TextChoices를 상속받아서 쓰는 거여서 메서드 choices를 해야한다
        
    )