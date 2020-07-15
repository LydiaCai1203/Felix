from app.handler import BaseHandler
from app.route import BaseApplication as router
from app.handler.error import BadRequestError


@router.route('/api/v1/example/get')
class ExampleHandler(BaseHandler):

    def get(self):
        # raise BadRequestError(reason='什么什么玩意儿')
        return self.write_json(data='Hello world')