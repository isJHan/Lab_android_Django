from django.urls import path, re_path
from . import views
appname = "comments"

urlpatterns = [
    path('dzcard/', views.dzCard),
    path('comment/', views.comment),
    path('collect/', views.collectCard),
    re_path(r'^getCommentInfo/$', views.getCommentsInfo),
]
