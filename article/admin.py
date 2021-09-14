from django.contrib import admin
from .models import ArticleColumn


class ArticleColumnAdmin(admin.ModelAdmin):
    # 列表显示tab名 标题名列表接口
    list_display = ('column', 'created', 'user')
    # 显示列表过滤器
    list_filter = ('column',)


admin.site.register(ArticleColumn, ArticleColumnAdmin)