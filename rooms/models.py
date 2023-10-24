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
    owner = models.ForeignKey("users.User",
                              on_delete=models.CASCADE,
                              #SET_NULL로 하면 지워도 남아있음
                              related_name="rooms",
                        )
    amenities = models.ManyToManyField("rooms.Amenity",
                                       related_name="rooms",)
    
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )
    
    def __str__(self):
        return self.name
    
    # ORM으로 결합하는 방법1 model 안에 메서드 넣기
    #admin display에 무언가 있으면 먼저 admin에서 찾아보고, 다음으로 model에서 찾아본다
    #근데도 없으면 model의 함수 내에서 찾아본다
    def total_amenities(self):
    #    print(self)
       return self.amenities.count()
    
    def rating(room):
        count = room.reviews.count()
        if count == 0:
            return "NO reviews"
        else:
            total_rating = 0
            for review in room.reviews.all().values("rating"):
                #이렇게 하면 쿼리셋을 받아온다 (별점만 받아옴), 그리고 딕셔너리임
                #이렇게 쿼리셋을 가져오게 되면 review객체는 사라진다 =>  review.rating을 못쓴다
                # print(room.reviews.all().values("rating"))
                # print(room.reviews.all())
                # print(dir(review))
                
                total_rating +=review["rating"]
            return round(total_rating / count,2)
        
        
    #이곳의 reviews 는 review_set이다
    
    
    
class Amenity(CommonModel):
    
    """Amenity definition"""
    name = models.CharField(max_length=150,)
    description = models.CharField(max_length=150,null=True,blank = True,)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"
        #모델이름의 복수형을 사용자 정의하고 싶을때 쓴다
        