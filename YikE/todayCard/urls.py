
from django.urls import path

from . import views

appname = 'todayCard'

urlpatterns = [
    path('getTodayInfo/', views.getTodayInfo),
    # path('qnjr/', ),
    # path('dzcard/', ),
    # path('comment/', ),
    # path('collect/', ),
    # path('contribute/', ),
]

