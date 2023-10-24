from django.contrib import admin
from .models import Room,Amenity
# Register your models here.


@admin.action(description="set all prices to zero")
def reset_prices(model_admin,request,rooms):  
                # = (model_admin,request,queryset)
    #(RoomAmdin을 호출,액션을 누가 호출했는지,선택한 객체의 모든 객체 리스트)
    #3개의 파라미터를 반드시 가져야 한다
    #액션을 가지고 있는 modeladmin, 그 동작을 요청하는 user에 대한 정보등, 객체리스트
    # print(model_admin)
    # print(dir(request))
    # print(queryset)
    for room in rooms:
        room.price=0
        room.save()
    

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    
    actions = (reset_prices,)
    
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
        
    )
    # def total_amenities(self,room):
    #     print(f"{self} 첫번쨰이니다")
    #     #Roomadin을 가지고 두반째 매개변수로 room을 가진다
    #     return room.amenities.count()
    #     #object마다 함수를 호출한다
    
    search_fields = (
        "^name", #이렇게하면 name로 시작하는 글자로 찾겠다가 됌
        "=price", #이렇게하면 정확히 일치하는 price로 찾겠다가 됌 
        "owner__username"
    )    
    
    list_filter=(
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    
    readonly_fields=(
        "created_at",
        "updated_at",
    )

