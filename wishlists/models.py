from django.db import models
from common.models import CommonModel
# Create your models here.


class Wishlist(CommonModel):
    
    """ WishList model definition"""
    
    
    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField("rooms.Room",
                                   related_name="wishlists",)
    experience = models.ManyToManyField("experiences.Experience",
                                        related_name="wishlists",)
    user = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="wishlists",)
    
    
    def __str__(self):
        return self.name
    