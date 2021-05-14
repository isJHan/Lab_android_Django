from django.http.response import JsonResponse

def check_login(fn):
    def wrapper(request, *args, **kwargs):
        if(request.session.get('is_login', False)):
            return fn(request, *args, **kwargs)
        else:
            return JsonResponse({'error': True}) # 未认证
    
    return wrapper