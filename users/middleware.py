from django.core.urlresolvers import reverse
from utils.wrappers import *
# 记录退出时的url
class RecordUrlMiddleware(object):
    #
    def process_response(self, request, response):
        # 定义不记录的url列表
        exclue_urls = [
            reverse('users:login'),
            reverse('users:register'),
            reverse('users:login_handle'),
            reverse('users:deal_register'),
            reverse('users:info'),
            reverse('users:site'),
            reverse('users:order'),
            reverse('users:login_out'),
            '/favicon.ico',
        ]

        # localhost:8000/abc/123/?a=100


        # 判断用户请求的url是否在排除列表
        if request.path not in exclue_urls and response.status_code == 200:
            # 记录url
            set_cookies(response, 'pre_url', request.get_full_path())
        #
        return response




