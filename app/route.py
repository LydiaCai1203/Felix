# 路由配置
"""
    路由表是一个 URLSpec 对象/元组 组成的列表，第一个被匹配的规则就会被使用，
    如果正则表达式包含捕获组，这些组会被作为路径参数传递给处理函数的 HTTP 方法。 
    
    [url(r"/story/([0-9]+)", StoryHandler, dict(db=db), name="story")]
    path(包含路径参数的写法), 处理函数，第三个参数作为处理函数的参数参入，name 是 URLSpec 的名字。

    (r"/static/(.*)", web.StaticFileHandler, {"path": "/var/www"}) 配置静态服务
"""
from functools import wraps

# from tornado.routing import Router
from tornado.web import Application

RESOURCES = {}


class BaseApplication(Application):
    """
        负责全局配置，包括映射请求转发给处理程序的路由表。
    """

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

            get_handler_delegate 里面的 path_args 将会传到 handler 中
        """
        return self.get_handler_delegate(
            request, 
            RESOURCES[request.path],
        )

    @staticmethod
    def route(uri: str):
        """路由装饰器
        """
        def decorator(cls):
            RESOURCES.update({uri: cls})
            return cls
        return decorator
