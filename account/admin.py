from django.contrib import admin
from .models import UserProfile, UserInfo


class UserProfileAdmin(admin.ModelAdmin):
    """
    UserProfileAdmin用于管理userprofile 的展示样式
    """
    # list_display 作用 列出列表中的项目
    list_display = ("user", "birth", "phone")
    # list_filter 作用规定 网页右边filter的显示内容
    list_filter = ("phone",)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "school", "profession", 'address', "aboutme", "photo")


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
# Register your models here.
