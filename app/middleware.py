import time
from django.http import HttpResponseForbidden

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # process before view
        print(f'[middleware] path:{request.path}')
        response = self.get_response(request)
        # after process
        print(f'[middleware] after status:{response.status_code}')
        return response
    

class TimerMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response
    
    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time()- start
        print(f'[middleware] request takes time {duration:.2f} seconds')
        return response
        
        
class BlockedIpAddress:
    Blocked_IP = []
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self,request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.Blocked_IP:
            return HttpResponseForbidden("you ip is blocked")

        return self.get_response(request)
    

# class Log:
#     def __init__(self,get_response):
#         self.get_response = get_response
    
#     def __call__(self, request):
#         print(f'[middleware] path:{request.path}')
#         response = self.get_response(request)
#         print(f'[middleware] code:{response.status_code}')
#         return response
    
# class timer:
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         start = time.time()
#         response = self.get_response(request)
#         duration = time.time()-start
#         print(f'[middleware] take time:{duration:.2f} seconds')
#         return response
    
# class ipaddress:
#     BLOCKED_IPS = ['127.0.0.1']
#     def __init__(self,get_response):
#         self.get_response = get_response

#     def __call__(self,request):
#         ip = request.META.get('REMOTE_ADDR')
#         if ip in self.BLOCKED_IPS:
#             return HttpResponseForbidden('your ip is blocked')
#         return self.get_response(request)