
from django.urls import path
from . import views

appname = 'accounts'

urlpatterns = [
    path(r'login/', views.login), # 登录
]


