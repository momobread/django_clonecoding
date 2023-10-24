from django.db import models
from common.models import CommonModel

class Booking(CommonModel):
    """ Booking model definition"""


    class BookingKindChoices(models.TextChoices):
        ROOM = "room","Room"
        EXPERIENCE = "experience","Experience"
        
        
    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices.choices,
        )
    
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    #유저는 여러개를 예약 할 수 있지만,예약은 오직 한명의 유저밖에 가질 수 없다
    
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bookings',
    )
    #예약은 여러개의 방을 가질 수 없지만, 한개의 방은 많은 예약을 가질 수 있다
    
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='bookings',
    )
    
    check_in = models.DateField(null=True,blank=True,)
    check_out = models.DateField(null=True,blank=True,)
    # experinece만 예약하면 날짜 확인이 필요없어용 그래서 null값이랑 blank가 필요해욧
    experience_time = models.DateTimeField(
        null=True,
        blank=True,)
    # 그와 반대로 experience를 예약안하고 숙박을 예약할수도 있어서 이것또한  null이 필요
    
    guests = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.kind} /{self.user}"
    
    # title()하면 앞글자가 대문자가 되지롱
    
    
    