""" 
    鉴权相关的工具函数放在此处，open-api 的签名校验也可以放在此处
"""

from app.handler.error import ForbideenError


def check_perm(perm_name: str):

    def decorator(func):
        def inner(req_handler, *args, **kwargs):
            redis_session = (
                req_handler.server_session
                .open_session(req_handler.request)
            )
            user_info = redis_session.user_info
            perms = user_info.get("perms", [])

            if perm_name not in perms:
                raise ForbideenError(log_message="无接口权限")

            return func(*args, **kwargs)
        return inner
    return decorator


