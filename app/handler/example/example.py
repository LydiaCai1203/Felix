from app.handler import BaseHandler
from app.route import BaseApplication as router


@router.route('/api/v1/example/get')
class ExampleHandler(BaseHandler):

    def get(self):
        return self.write_json(data='Hello world')