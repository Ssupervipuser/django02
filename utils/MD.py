from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class DemoMiddelware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info == '/login/':
            return

        # 1.获取登录信息发送session
        user_info = request.session.get("info")
        if user_info:
            # 自定义方便获取数据
            # request.unicom_userid = user_info['id']
            # request.unicom_username = user_info['username']
            return
        return redirect('/login/')

