from app.model.example import ExampleModel
from app.handler import BaseHandler
from app.route import BaseApplication as router
from app.handler.auth import check_perm
from app.handler.const import EXAMPLE_READ


@router.route("/api/v1/example/get")
class ExampleHandler(BaseHandler):

    @check_perm(EXAMPLE_READ)
    def get(self):
        return self.write_json(data="Hello world")
