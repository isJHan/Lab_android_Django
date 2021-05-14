
from django.urls import path
from . import views

appname = 'accounts'

urlpatterns = [
    path(r'register/', views.register), # 注册
    path(r'login/', views.login), # 登录
    path(r'getUserInfo/', views.getUserInfo),
    # path(r'illegal/', views.illegal), # 需要登陆的操作
    # path(r'getToken/', views.getToken), # 获取Token, 以便使用Django的认证系统
    path(r'logout/', views.logout), # 退出登录
]


