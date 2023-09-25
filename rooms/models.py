from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    
    """ Room Model Definition"""
    
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place","Entire Place")
        PRIVATE_ROOM = ("private_room","Private Room")
        SHARED_ROOM =  ("shared_room","Shared_Room")
    
    name = models.CharField(max_length=180, default ="",)
    country = models.CharField(max_length=50,default ="한국")
    city = models.CharField(max_length=80,default="서울")
    price= models.PositiveIntegerField()
    rooms = models.PositiveBigIntegerField()
    toilets = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=True,)
    kind = models.CharField(max_length=20,choices=RoomKindChoices.choices,)
    owner = models.ForeignKey("users.User",on_delete=models.CASCADE,
                              #SET_NULL로 하면 지워도 남아있음
                              )
    amenities = models.ManyToManyField("rooms.Amenity",)
    
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    
    def __str__(self):
      return self.name
    
class Amenity(CommonModel):
    
    """Amenity definition"""
    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150,null=True,blank = True,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"
        #모델이름의 복수형을 사용자 정의하고 싶을때 쓴다
        