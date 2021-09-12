"""
该文件用于专门存放各种与表单有关的类
"""

from django import forms
# 引入django默认的用户模型User类，在这个表单类中就应用User模型，不需要再新建用户
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    # 使用widget 来规定表单类的字段 在HTML中的某种元素类型展现
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:    # 内部类， 需要声明本表单类所应用的数据模型，也是
        model = User   # 将来表单的内容会写入到那个数据库表中的那些记录里面
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd["password2"]:   # 判断是否不相等
            raise forms.ValidationError("password do not match.")    # 抛出异常
        return cd["password2"]


class UserProfileForm(forms.ModelForm):
    """继承自django模型的内部类 django模型"""
    class Meta:
        model = UserProfile
        # 使用fields来限定所选用的属性（数据库表中的字段），or 使用exclude 列表说明所排除的属性
        fields = ("phone", "birth")


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("school", "company", "profession", "address", "aboutme", "photo")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", )