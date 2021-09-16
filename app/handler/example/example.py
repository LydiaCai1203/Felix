from tornado import log

from app.handler import BaseHandler
from app.route import BaseApplication as router
from app.handler.utils import check_perm
from app.handler.const import EXAMPLE_READ


@router.route("/api/v1/example/get")
class ExampleHandler(BaseHandler):

    @check_perm(EXAMPLE_READ)
    def get(self):
        log.access_log.info("access_log")
        log.app_log.info("app_log")
        return self.write_json(data="Hello world")
