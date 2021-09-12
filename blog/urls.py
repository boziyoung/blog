from django.urls import path
from . import views

app_name = "blog"
"""
path : name 表示的是route匹配到的URL的一个别名
"""
urlpatterns = [
    path("", views.blog_title, name='blog_title'),
    path("<article_id>", views.blog_article, name="blog_article")
]
