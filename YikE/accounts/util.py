

# 从session中获取uid
def getUidFrom(request):
    return request.session.get('user')


# 获取返回字典
def getRetInfo(uid = '', username = '', error = True):
    return {'error': error, 'info':{
            'uid': uid,
            'username': username
    }}


