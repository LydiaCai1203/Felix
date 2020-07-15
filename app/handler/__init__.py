# Base Handler
import traceback
from typing import Any

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    
    def initialize(self):
        """初始化
        
            如果不是所有的 RequestHandler 初始化都需要 middleware
            可以在 routes.py 中以参数的形式传入
            
            参考文档：
            https://tornado-zh.readthedocs.io/zh/latest/guide/structure.html
            < example >:
            (r"/api/v1/example", ExampleHandler, dict(middleware=BaseMiddleWare()))
        """
        pass

    def prepare(self):
        """在请求进入处理函数之前被调用，可能产生输出，会在调用 finish 之后在这里结束
        """
        return super().prepare()

    def on_finish(self):
        """响应返回给用户以后调用
        """
        return super().on_finish()

    def write_json(self, data: Any, **kwargs):
        """规范返回数据格式

            request_handler.write() 中如果传入 dict, tornado 会将该 dict 作为
            JSON 来写, 并在响应头中加上 Content-type:application/json。所以不必
            显示将 data 进行 JSONEncode。倘若 data 不能被 JSONDecoded，程序抛出
            异常，tornado 会调用 write_error()
        """
        STATUS_SUCCESS = 200
        return self.write({
            "code": kwargs.get("code", STATUS_SUCCESS),
            "data": data,
            "msg": kwargs.get("msg", ""),
        })

    def write_error(self, status_code: int, **kwargs):
        """添加通用异常处理

            write_error 调用 由处理程序中抛异常引起 或 应用程序主动调用
            exc_info 未必是 sys.exc_info，因此不能使用 format_exc,
            要使用 format_exception 代替
            参考文档：
            https://tornado-zh.readthedocs.io/zh/latest/guide/structure.html
            < #错误处理 >
        """
        STATUS_INTERNAL_ERROR = 500
        try:        
            if "exc_info" in kwargs:
                exc_type, exc_value, exc_traceback = kwargs["exc_info"]
                msg_list = traceback.format_exception(
                    exc_type, 
                    exc_value, 
                    exc_traceback
                )
                print(repr(msg_list))
                msg = str(exc_value)
            else:
                msg = kwargs.get("msg", "")
                self.set_status(status_code)
        except:
            msg = traceback.format_exc()
            self.set_status(STATUS_INTERNAL_ERROR)

        return self.write({
            "code": status_code,
            "msg": msg,
            "data": ""
        })
        
    def on_connection_close(self):
        """当客户端断开时被调用，应用程序该情况并中断后续处理

            清除和长连接相关的资源，只有当异步处理，连接被关闭才会调用。
            如果你需要在每个请求之后做处理，用 on_finish 
        """
        return super().on_connection_close()
