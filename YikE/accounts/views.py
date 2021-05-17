# from django.shortcuts import render
from django.db import utils
from .decorator import check_login
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.models import User
# from django.contrib.auth import login as loginAuth, authenticate, logout as logoutAuth
# from django.middleware.csrf import get_token
from django.db.utils import IntegrityError
from django.core import serializers
from .models import user, password as myPassword

# Create your views here.

@csrf_exempt
def register(request):
    uid = request.POST['uid']
    pwd = request.POST['pwd']
    username = request.POST['user']

    # 修改数据库
    try:
        myuser = user.objects.create(uid = uid, username = username)
        myPassword.objects.create(uid =myuser, md5 = pwd)

        from .util import getRetInfo
        return JsonResponse(getRetInfo(uid = uid, username=username, error=False))
    except IntegrityError:
        from .util import getRetInfo
        retInfo = dict(getRetInfo())
        retInfo['errorInfo'] = "已存在用户名"
        return JsonResponse(retInfo)


@csrf_exempt
def login(request):
    from .util import getRetInfo

    uid = request.POST['uid']
    password = request.POST['pwd']
    
    myuser = user.objects.filter(uid = uid).first() # 查找用户
    myPwd = myPassword.objects.filter(uid = myuser).first() # 验证密码

    if myuser is not None and myPwd.isCorrect(password):
        

        
        request.session['is_login'] = True
        request.session['user'] = uid

        retInfo = getRetInfo(uid, myuser.username, False)
        return JsonResponse(retInfo)
    else:
        return JsonResponse(getRetInfo())
    

    
@check_login
def getMyInfo(request):
    # uid = "00001"

    # uid = request.GET.get("uid", default = "00001")
    from .util import getUidFrom
    uid =  getUidFrom(request) # 从session中获取uid
    theUser = user.objects.filter(uid = uid)
    # from django.forms.models import model_to_dict
    # UserDic = model_to_dict(theUser.first())
    # print(type(UserDic))
    # print(UserDic)
    # print(type(UserDic['photo']))

    return HttpResponse(serializers.serialize('json', theUser))
    # return JsonResponse(UserDic)
    



@check_login
def getUserInfo(request):
    # GET
    uid = request.GET.get('uid')
    userS = user.objects.filter(uid = uid)
    # strInfo = serializers.serialize("json", userS)
    # # print(type(jsonInfo))
    # # print(jsonInfo)
    # import json
    # listInfo = json.loads(strInfo)
    # listInfo[0]["pk"]
    return HttpResponse(serializers.serialize("json", userS))



# @csrf_exempt
# def register(request):

#     info = {
#         'uid': '',
#         'username': ''
#     }
#     ret = {
#         'error': True
#     }

#     try:
#         uid = request.POST['uid']
#         password = request.POST['pwd']
#         username = request.POST['user']
#         userInner = User.objects.create_user(username = uid, password = password)
#         # userInner.save()
#         user = myUser.objects.create(uid = userInner, username = username)
#         user.save()

#         ret['error'] = True
#         info['uid'] = uid
#         info['username'] = username
#         ret['info'] = info
#     except IntegrityError:
#         # uid不唯一
#         pass
#     return JsonResponse(ret)


# # @csrf_exempt
# def illegal(request):
#     t = request.POST['parm0']
#     if(request.session.get('is_login')):

#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})

@check_login
def logout(request):
    request.session.flush()
    # logoutAuth(request)
    return JsonResponse({'success': True})

# @csrf_exempt
# def getToken(request):
#     return JsonResponse({'token': str(get_token(request=request))})