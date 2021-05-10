# from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

@csrf_exempt
def login(request):
    uid = request.POST['uid']
    password = request.POST['pwd']

    info = {
        'uid': '',
        'username': ''
    }
    ret = {
        'error': True,
        'info': None
    }
    
    user = authenticate(request, username = uid, password = password)
    if user is not None:
        login(request ,user)
        ret['error'] = False
        info['uid'] = user.get_username()
        info['username'] = user.myUser.username
        ret['info'] = info

        return JsonResponse(ret)
    else:
        return JsonResponse(ret)
    




