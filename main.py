"""
    Tornado Web 应用程序通常组成：一个或多个 RequestHandler 子类，一个 Application 对象
    会将所有的 request 都路由到对应的 Handler 上。那么为什么还存在多个 Applications 对应一
    个 Server 的情况，两种结构各自的优缺点又是什么。
"""
from tornado.ioloop import IOLoop
from tornado.web import HTTPServer
from tornado.options import options, define
from tornado import autoreload

from app.route import BaseApplication
from app.handler.example.example import ExampleHandler
from settings import *

router = BaseApplication()


if __name__ == "__main__":

    if options.autoreload: autoreload.start()

    server = HTTPServer(router)
    server.listen(options.port)
    IOLoop.current().start()