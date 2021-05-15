# from django.shortcuts import render
from json.encoder import JSONEncoder
from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from .models import QnjrCard, TodayCard
from datetime import datetime
from accounts.decorator import check_login
# Create your views here.


@check_login
def getTodayInfo(request):
    # todayCards = TodayCard.objects.filter(state = 1)
    todayCards = TodayCard.objects.filter(carrddate = datetime.today().date(), state = 1) # 过滤审核过的当天卡片
    # for item in todayCards:
    #     print(item.state)
    #     print(type(item.state))
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
    
    return HttpResponse(serializers.serialize("json", todayCards)) # 序列化

@check_login
def getQnjrInfo(request):
    qnjrCards = QnjrCard.objects.filter(craddate = datetime.today().date())

    return HttpResponse(serializers.serialize("json", qnjrCards)) # 序列化




