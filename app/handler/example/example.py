from app.handler import BaseHandler
<<<<<<< HEAD
from app.route import BaseApplication as app


@app.route('/api/v1/example/get')
=======
from app.route import BaseRouter as router


@router.route('/api/v1/example/get')
>>>>>>> dev
class ExampleHandler(BaseHandler):

    def get(self):
        return self.write_json(data='Hello world')