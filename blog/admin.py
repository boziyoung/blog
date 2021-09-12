from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    # 列表显示tab名 标题名列表接口
    list_display = ("title", "author", "publish")
    # 列表过滤器接口
    list_filter = ("publish", "author")
    # 页面搜索接口 以title ,body内容为准
    search_fields = ("title", "body")
    # 显示外键的详细信息
    raw_id_fields = ("author",)
    # 根据你指定的日期相关的字段，为页面创建一个时间导航栏，可通过日期过滤对象。
    date_hierarchy = "publish"
    ordering = ["publish", "author"]


# 将BlogArticles 类注册到该admin中， 这样django才知道
admin.site.register(BlogArticles, BlogArticlesAdmin)
# Register your models here.
