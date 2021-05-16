"""YikE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from .settings import MEDIA_PATH

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/todayCard/', include('todayCard.urls')),
    path('api/comments/', include('comments.urls')),
    # path('api/media/', include('media.urls')),
    # path('admin/', admin.site.urls),
    # 访问静态文件, url按顺序匹配, 下面这行优先级最低, 必须放到最后一行
    re_path(r'^api/(?P<path>.*)$', serve, {"document_root":MEDIA_PATH}), # 疑问, 为什么可以匹配这个而不影响其他路由的匹配
]
