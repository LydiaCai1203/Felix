from webargs import fields
from webargs.tornadoparser import use_args
from pbkdf2 import crypt

from app.handler import BaseHandler
from app.route import BaseApplication as router
from app.handler.error import BadRequestError
from app.model.user.user import UserModel


@router.route("/api/v1/users/login")
class UserLoginHandler(BaseHandler):

    @use_args(
        {
            "account": fields.Str(required=False),
            "email": fields.Str(required=False),
            "password": fields.Str(required=True)
        },
        location="json"
    )
    def post(self, post_args: dict):
        """login

        1. check password
        2. save session and return cookies
        """
        user = (
            self.sess.query(UserModel)
            .filter(UserModel.email == post_args["email"])
            .first()
        )
        assert user, "the email is not existed"

        pwdhash = user.password
        pwd_is_right = crypt(post_args["password"], pwdhash)
        assert pwd_is_right, "wrong password"

        # create session & save session & return session_id
        user_info = {
            "account": post_args["account"],
            "email": post_args["email"]
        }

        server_session = (
            self.server_session
            .save_session(self.request, user_info)
        )
        self.set_cookie("SESSION_ID", server_session.sid)
        return self.write_json(data="login successfully")


@router.route("/api/v1/users/logout")
class UserLogoutHandler(BaseHandler):

    def get(self):
        """logout

            del session_id in redis
        """
        self.server_session.clear_session()
        return self.write_json(data="logout successfully")
