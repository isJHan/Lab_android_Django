from django.http.response import JsonResponse
# from django.shortcuts import render
# from YikE.todayCard.models import TodayCard
from todayCard.models import TodayCard
from accounts.decorator import check_login
from .models import comment as commentTable
from accounts.models import user as userTable
# Create your views here.

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
    theCard.commentcount += 1
    theUser = userTable.objects.filter(pk=uid).first()
    commentTable.objects.create(tcid = theCard, ctext = ctext, uid = theUser)
    theCard.save()
    # 新开线程对评论内容进行审核, 审核不通过则删除信息
    return {'error': False}

@check_login
def comment(request):
    tcid = request.POST['tcid']
    uid = request.session.get('user')
    ctext = request.POST['ctext']
    return JsonResponse(__cmt(tcid, uid, ctext))

