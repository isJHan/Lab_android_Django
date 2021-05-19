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


def __checkCtb(pk):

    #   设置阈值  #
    hentaiThreshold = 0.1
    pornThreshold = 0.2
    sexyThreshold = 0.2
    # 设置阈值 结束 #



    imgPath = str(TodayCard.objects.filter(pk = pk).first().picture)
    from os import get_exec_path
    imgPath = get_exec_path() + imgPath # 获取绝对路径
    from .nsfw import predict
    value = predict(imgPath)['probabilities']

    # 获取预测结果
    hentai = value['hentai']
    porn = value['porn']
    sexy = value['sexy']
    if(hentai < hentaiThreshold and porn < pornThreshold and sexy < sexyThreshold):
        pass
    else:
        # 相应处理(删除投稿)
        TodayCard.objects.get(pk=pk).delete()



@check_login
def contribute(request):
    type = request.POST['type']
    title = request.POST['title']
    text = request.POST['text']
    text_author = request.POST['author']

    fieldName = "picture" 
    picture = request.FILES[fieldName] # 获取图片

    id = TodayCard.objects.create(
        carrddate = datetime.today().date(),
        type = type,
        title = title,
        text = text,
        text_author = text_author,
        picture = picture,
        ).id
    
    
    # 新开线程审核
    import _thread
    _thread.start_new_thread(__checkCtb(id))
