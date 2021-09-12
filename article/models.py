from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name="article_column", on_delete=models.CASCADE)      # related_name:# 指定反向访问的名字
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        """ 将一个类实例转换为一个字符穿对象调用 ，只有在str()函数和 使用 print 对象实例时调用
            推荐使用 __repr__
        """
        return self.column
