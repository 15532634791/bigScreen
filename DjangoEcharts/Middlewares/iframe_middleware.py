from django.conf import settings
from django.http import HttpRequest, HttpResponse


class XFrameOptionsMiddleware(object):
    """
    如果您的 Django web 服务需要在其他网页上的 iframe 中展示，
    需要在响应头部中设置 X-Frame-Options 标志。X-Frame-Options
    可用于控制 iframe 的加载行为，可以设置为：

    DENY: 禁止加载 iframe
    SAMEORIGIN: 只允许同源网站的 iframe 加载
    ALLOW-FROM url: 允许指定 URL 的 iframe 加载

    在 Django 中设置 X-Frame-Options 标志可以通过中间件实现。
    创建一个新的 middleware，将 X-Frame-Options 标志添加到响应的响应头部中

    在 settings.py 中，可以将 X_FRAME_OPTIONS 设置为 DENY 或 SAMEORIGIN，
    示例代码如下：

        MIDDLEWARE = [
            # .
            # .
            'path.to.XFrameOptionsMiddleware',
        ]

        X_FRAME_OPTIONS = 'SAMEORIGIN'
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.x_frame_options = getattr(settings, 'X_FRAME_OPTIONS', 'SAMEORIGIN')

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        response['X-Frame-Options'] = self.x_frame_options
        return response
