from django.urls import path
from . import views
appname = "comments"

urlpatterns = [
    path('dzcard/', views.dzCard),
    path('comment/', views.comment),
    path('collect/', views.collectCard),
]
