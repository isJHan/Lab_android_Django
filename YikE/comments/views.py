from django.http.response import JsonResponse
from django.core import serializers
from django.http.response import HttpResponse

# from django.shortcuts import render
# from YikE.todayCard.models import TodayCard
from todayCard.models import TodayCard
from accounts.decorator import check_login
from .models import comment as commentTable
from accounts.models import user as userTable

# Create your views here.

"""
    修改数据库操作单独写成函数
"""


def __dZ(tcid):
    theCard = TodayCard.objects.filter(pk = tcid).first()
    theCard.dzcount += 1
    count = theCard.dzcount
    theCard.save()
    
    return count

@check_login
def dzCard(request):
    tcid = request.POST['tcid']
    print(tcid)
    return JsonResponse({'count': __dZ(tcid)})

def __cmt(tcid, uid, ctext):
    theCard = TodayCard.objects.filter(pk = tcid).first()
    # theCard.commentcount += 1 # 增加评论数
    theUser = userTable.objects.filter(pk=uid).first()
    commentTable.objects.create(tcid = theCard, ctext = ctext, uid = theUser) # 创建新行
    theCard.save()
    count = theCard.comment_set.all().count()
    print(count)
    theCard.commentcount = count # 更新评论数
    theCard.save()
    # 新开线程对评论内容进行审核, 审核不通过则删除信息
    return {'error': False, 'commentcount': count}

@check_login
def comment(request):
    tcid = request.POST['tcid']
    uid = request.session.get('user')
    ctext = request.POST['ctext']
    ret = __cmt(tcid, uid, ctext)
    return JsonResponse(ret)



def __clt(uid, tcid):
    theUser = userTable.objects.filter(uid = uid).first()
    cltCard = TodayCard.objects.filter(pk = tcid).first()

    # print(cltCard.collectid.all()) # 收藏此card的用户, 来自于user表中的多对多关联, 中间表查询
    # print(cltCard.comment_set.all()) # 来自于 comment表的关联(外键)

    theUser.collectid.add(cltCard)
    
    theUser.save()
    # 获取收藏数
    count = cltCard.collectid.all().count()
    print(count)
    cltCard.collectcount = count # 更新收藏数
    return {'error': False, 'collectcount': count}

@check_login
def collectCard(request):
    # POST
    uid = request.session.get('user')
    tcid = request.POST['tcid']

    # theUser = userTable.objects.filter(uid = uid).first()
    # print(type(theUser.collectid)) # 获取收藏id
    # collectid = theUser.collectid
    # print(collectid.all()) #　QuerySet[]
    # print('ending')
    ret = __clt(uid, tcid)
    return JsonResponse(ret)


@check_login
def getCommentsInfo(request):
    # GET
    tcid = request.GET.get('tcid')
    allComments = commentTable.objects.filter(tcid = tcid)
    return HttpResponse(serializers.serialize("json", allComments)) # 序列化
