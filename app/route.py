# 路由配置
from functools import wraps

from tornado.routing import Router


RESOURCES = {}

class BaseRouter(Router):

    def __init__(self, app):
        self.app = app

    def find_handler(self, request, **kwargs):
        """将 path 对应到 request_handler 上
        """
        return self.app.get_handler_delegate(
            request, 
            RESOURCES[request.path]
        )

    @staticmethod
    def route(uri: str):
        """路由装饰器
        """
        def decorator(cls):
            RESOURCES.update({uri: cls})
            return cls
        return decorator