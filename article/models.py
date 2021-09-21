from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 9月21日
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name="article_column", on_delete=models.CASCADE)      # related_name:# 指定反向访问的名字
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        """ 将一个类实例转换为一个字符穿对象调用 ，只有在str()函数和 使用 print 对象实例时调用
            推荐使用 __repr__
        """
        return self.column


# 9月21日
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE, related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):
        self.slug = slugify(self.title)
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])