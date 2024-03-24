# from django.utils.deprecation import MiddlewareMixin
# from django.shortcuts import redirect
# class DemoMiddelware(MiddlewareMixin):
#     def process_request(self,req):
#         if req.path_info=='/login/':
#             return
#
#         #1.获取登录信息发送session
#         user_info=req.session.get("user_info")
#         if user_info:
#             #自定义方便获取数据
#             req.unicom_userid=user_info['id']
#             req.unicom_username=user_info['username']
#             return
#         return redirect('/login/')
#
#
#     def process_response(self,req,response):
#
#         return response