from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
"""从django 内置库中的用户认证 和 管理应用 引入两个方法"""
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import UserInfo, UserProfile
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm, UserInfoForm


# Create your views here.
def register(request):
    if request.method == "POST":
        # request.POST 用于数据传递， 提交的表单数据，也是一个类字典对象
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            # user_form.is_valid()*userprofile_form.is_valid() 使用* 类似 TRUE*TRUE 
            # is_valid()验证数据是否合法
            """ modelForm 类或者它的子类都具有 save（）方法， 将数据保存到数据库中； commit=Fasle，
                其结果是数据并没有保存到数据库，而仅生成一个数据对象，
            """
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            # 解决user info 错误
            UserInfo.objects.create(user=new_user)
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry, you can not register.")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, "account/register.html", {"form": user_form, "profile": userprofile_form})


def user_login(request):
    """创建了一个关于登录的视图函数
    在这个视图函数中处理前端提交的数据，并支持前端的显示请求，
    视图函数，必须使用request作为第一个参数"""

    # request.method为 HttpRequest对象的一个常用属性，它返回HTTP请求类型的字符串
    if request.method == "POST":
        # request.POST 用于数据传递， 提交的表单数据，也是一个类字典对象
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # is_valid()验证数据是否合法
            cd = login_form.cleaned_data
            # cleaned_data 得到字典类型的数据
            """authenticate()函数： 检验此用户是否为本网站项目的用户，以及其密码是否正确，
            if TRUE。就返回一个USER实例对象，否则 返回 None"""
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Wellcome you. you have been authenticated successfully")
            else:
                return HttpResponse("Sorry. your username or password is not right. ")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'account/login.html', {"form": login_form})


# 展示个人信息的视图函数
@login_required(login_url='/account/login/')
def myself(request):

    """request.user.username : user：user 只有当Django 启用 AuthenticationMiddleware 中间件时才可用。它的值是一个 setting.py
    里面AUTH_USER_MODEL 字段所定义的类的对象，表示当前登录的用户。如果用户当前没有登录，user 将设为
    django.contrib.auth.models.AnonymousUser 的一个实例。你可以通过 is_authenticated() 区分它们。
    """
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)

    return render(request, "account/myself.html", {"user": user,  "userinfo": userinfo, "userprofile": userprofile})

# 编辑个人信息的视图函数
@login_required(login_url='/account/login/')
def myself_edit(request):
    # 获取一个对应条件的事务对象
    # django 默认的用户表user 记录pw 、 last_login 、is_supperuser 、first_name 、 last_name 、 Email \、
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    # 判断请求对象的请求方式
    if request.method == "POST":
        # 通过表单类去处理request传入的数据
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)

        if user_form.is_valid()*userprofile_form.is_valid()*userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            # 得到数据字典类型数据
            userprofile_cd = userprofile.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd["email"])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()

            # 重定向到新页面中HttpResponseRedirect
        return HttpResponseRedirect('/account/my-information')

    else:

        user_form = UserForm(instance=request.user)
        userprofile_form = UserProfileForm(initial={"birth": userprofile.birth, "phone": userprofile.phone})
        userinfo_form = UserInfoForm(initial={"school": userinfo.school, "address": userinfo.address, "aboutme": userinfo.aboutme
                                              , "company": userinfo.company, "profession": userinfo.profession})

        return render(request, "account/myself_edit.html", {"user_form": user_form, "user_profile": userprofile_form, "userinfo_form": userinfo_form})


@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == "POST":
        img = request.POST['img']
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request, "account/imagecrop.html")




