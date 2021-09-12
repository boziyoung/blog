from django.urls import path
from . import views
from django.contrib.auth import views as auth_vies

app_name = "account"
urlpatterns = [
    # 自定义login
    # path("login", views.user_login, name="user_login"),
    # django 内置的auth login template_name读取setting 设置的template 地址，无需指定上一级templates目录
    path("login/", auth_vies.LoginView.as_view(template_name='account/login2.html'), name='user_login'),
    path("logout/", auth_vies.LogoutView.as_view(template_name='account/logout.html'), name="user_logout"),
    path("register/", views.register, name='user_register'),
    path("password-change/", auth_vies.PasswordChangeView.as_view(template_name='registration/password_change_form.html', success_url="/account/password-change-done/"), name="password_change"),
    path("password-change-done/", auth_vies.PasswordChangeView.as_view(template_name= 'registration/password_change_done.html', success_url="/account/password-change-done/"), name="password_change_done"),
    path('password-reset/', auth_vies.PasswordResetView.as_view(template_name="account/password_reset_form.html",
                                                                 email_template_name="account/password_reset_email.html",
                                                                 success_url='/account/password-reset-done/'),
         name='password_reset'),
    path('password-reset-done/',
         auth_vies.PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_vies.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",
                                                     success_url='/account/password-reset-complete/'),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_vies.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),
    path('my-information/', views.myself, name="my_information"),
    path('edit-my-information/', views.myself_edit, name="edit_my_information"),
    path('my-image/', views.my_image, name="my_image")
]
"""django 3.2版本修改了 auth 中views 的login函数"""

