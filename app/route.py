# 路由配置
from functools import wraps

# from tornado.routing import Router
from tornado.web import Application


RESOURCES = {}


class BaseApplication(Application):

    def __init__(
        self, 
        handlers=None, 
        default_host=None, 
        transforms=None, 
        **settings
    ):
        super().__init__(
            handlers=handlers, 
            default_host=default_host, 
            transforms=transforms, 
            **settings
        )

    def find_handler(self, request, **kwargs):
        """将 path 对应到 request_handler 上
        """
        return self.get_handler_delegate(
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
