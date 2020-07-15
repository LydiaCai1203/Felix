"""
    自定义错误
"""
from tornado.web import HTTPError


class BadRequestError(HTTPError):
    def __init__(
        self, 
        status_code=400, 
        log_message="Bad Request", 
        *args, 
        **kwargs
    ):
        (
            super()
            .__init__(
                status_code=status_code, 
                log_message=log_message, 
                *args, 
                **kwargs
            )
        )

class ForbideenError(HTTPError):
    def __init__(
        self, 
        status_code=403, 
        log_message="Forbideen", 
        *args, 
        **kwargs
    ):
        (
            super()
            .__init__(
                status_code=status_code, 
                log_message=log_message, 
                *args, 
                **kwargs
            )
        )

class UnauthorizedError(HTTPError):
    def __init__(
        self, 
        status_code=401, 
        log_message="Unauthorized", 
        *args, 
        **kwargs
    ):
        (
            super()
            .__init__(
                status_code=status_code, 
                log_message=log_message, 
                *args, 
                **kwargs
            )
        )

class InternalError(HTTPError):
    def __init__(
        self, 
        status_code=500, 
        log_message="Internal Error", 
        *args, 
        **kwargs
    ):
        (
            super()
            .__init__(
                status_code=status_code, 
                log_message=log_message, 
                *args, 
                **kwargs
            )
        )