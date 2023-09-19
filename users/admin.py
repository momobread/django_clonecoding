from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # User의 root
from .models import User #users models의 내가 만든 Uesr를 쓴다고 알려줘야함
# => admin register에 등록하기 위해서

# Register your models here.
# class CustomUserAdmin(admin.ModelAdmin) => 이것은 새로운 모델을 등록했을때

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
           ( "Profile",
                 {
                     "fields":("username","password",
                               "email","is_host"),
                     "classes" :("wide",)
                },
                 ),
                # section의 이름을(nav바에 보여지는 부분) 적어줘야 한다 그리고 fields라는 key를 가진 딕셔너리가 있어야함
           ("Permissions",
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                    "classes" : ("collapse",)
                    #classes callapse를 쓰면 section을 숨겼다 드러냈다 할 수 있음
                },
            ),
            ("Important Dates",
                {
                    "fields": ("last_login", "date_joined"
                               ),
                    "classes" : ("collapse",)
                 },
            ),
        
        )
    #이렇게 fields를 재설정하면 변경페이지에서 순서가 튜플에 있는데로 바뀐다
    #fieldset은 나만의 section을 만들수 있고,확장가능
     # => 반드시 튜플로 되어있어야 하고 그안에 또 튜플이 있어야 한다

    list_display=("username","email","name","is_host")
    #수정화면 말고 처음 화면에 보여지는 순서 조정할 수 있다
    