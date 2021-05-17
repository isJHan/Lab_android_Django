
from django.urls import path, re_path
from . import views

appname = 'accounts'

urlpatterns = [
    path(r'register/', views.register), # 注册
    path(r'login/', views.login), # 登录
    path(r'getMyInfo/', views.getMyInfo), # 获取我的信息
    re_path(r'^getUserInfo/$', views.getUserInfo), #　获取uid用户信息
    # path(r'illegal/', views.illegal), # 需要登陆的操作
    # path(r'getToken/', views.getToken), # 获取Token, 以便使用Django的认证系统
    path(r'logout/', views.logout), # 退出登录
]


