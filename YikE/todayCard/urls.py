
from django.urls import path

from . import views

appname = 'todayCard'

urlpatterns = [
    path('getTodayInfo/', views.getTodayInfo),
    path('getQnjrInfo/', views.getQnjrInfo),
    # path('qnjr/', ),
    # path('dzcard/', ),
    # path('comment/', ),
    # path('collect/', ),
    # path('contribute/', ),
]

