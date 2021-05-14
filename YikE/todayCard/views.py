# from django.shortcuts import render
from json.encoder import JSONEncoder
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from .models import TodayCard
from datetime import datetime
# Create your views here.



def getTodayInfo(request):
    todayCards = TodayCard.objects.filter(carrddate = datetime.today().date())
    print(todayCards)
    # 序列化
    # 转化成python字典

    # print(type(todayCards))
    # for i in todayCards:
    #     print(type(i))
    #     print(serializers.serialize('json', i))
    # todayCardsxSeri = serializers.serialize('json', TodayCard.objects.all())
    
    # print(todayCardsSeri)

    # ret = "{" + "{}".format(todayCardsSeri) + "}"
    
    return HttpResponse(serializers.serialize("json", todayCards)) 





