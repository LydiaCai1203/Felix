import traceback

from webargs import fields
from webargs.tornadoparser import use_args
from pbkdf2 import crypt

from app.handler import BaseHandler
from app.route import BaseApplication as router
from app.handler.error import BadRequestError
from app.model.user.user import UserModel
from app.db import Session

@router.route("/api/v1/users/register")
class UserRegisterHandler(BaseHandler):

    @use_args(
        {
            "account": fields.Str(required=True),
            "nickname": fields.Str(required=True),
            "email": fields.Str(required=True),
            "password": fields.Str(required=True)
        },
        location="json"
    )
    def post(self, post_args: dict):
        """register
        """
        pwdhash = crypt(post_args["password"])
        post_args.update(password=pwdhash)
        try:
            user = UserModel(**post_args)
            self.sess.add(user)
            self.sess.commit()
        except:
            traceback.print_exc()
            self.sess.rollback()
            return self.write_error(status_code=500, msg="register failed")
        return self.write_json(msg="register successfully")
