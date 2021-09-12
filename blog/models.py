from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# 数据模型类  - 用于创造数据库自动生成脚本的类
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    # foreginkey 外键必须设置 on_delete参数
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.PROTECT)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title