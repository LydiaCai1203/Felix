"""
Tornado Web 应用程序通常组成：一个或多个 RequestHandler 子类，一个 Application 对象
会将所有的 request 都路由到对应的 Handler 上。那么为什么还存在多个 Applications 对应一
个 Server 的情况，两种结构各自的优缺点又是什么。
"""
from tornado.ioloop import IOLoop
from tornado.web import Application, HTTPServer

from app.route import BaseRouter
from app.handler.example.example import ExampleHandler


router = BaseRouter(Application())

if __name__ == "__main__":
    server = HTTPServer(router)
    server.bind(8009)
    server.start(0)
    IOLoop.current().start()