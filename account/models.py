from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 新建model
class UserProfile(models.Model):   # 数据表名默认 : app名_model 名 ，可以使用 class meta 内部类修改
    # OneToOneField 一一对应的 User类 与 UserProfile 类的
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    # 限制了dateFiled 的日期格式
    birth = models.DateField(blank=True, null=True)

    phone = models.CharField(max_length=20, null=True)

    def __str__(self):             # 用来返回对象的字符串表达式
        return 'user{}'.format(self.user.username)


class UserInfo(models.Model):
    """保存用户的个人信息"""
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        """返回对象的字符串"""
        return "user:{}".format(self.user.username)