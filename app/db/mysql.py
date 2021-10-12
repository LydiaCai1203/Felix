from urllib.parse import quote

from tornado.options import options
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.model.example import ExampleModel
from app.model.user import UserModel, PermModel, UserPermModel
from settings import MYSQL_CONF


def get_mysql_conn():
    """建立 MySQL 连接
    """
    mysql = MYSQL_CONF["localhost"]
    user = quote(mysql["user"])
    password = quote(mysql["password"])
    auth = f"{user}:{password}" if password else user

    uri = ("mysql+pymysql://{auth}@{host}:{port}/{db}" "?charset={charset}").format(
        auth=auth, **mysql
    )

    return create_engine(uri, pool_size=5, pool_recycle=3600)


def get_mysql_sess(binds: dict) -> Session:
    """生成会话
    """
    SessionClass = sessionmaker()
    SessionClass.configure(binds=binds)
    return SessionClass


# 获取 session 实例
mysql_conn = get_mysql_conn()
Session = get_mysql_sess(
    {
        ExampleModel: mysql_conn,
        UserModel: mysql_conn,
        PermModel: mysql_conn,
        UserPermModel: mysql_conn,
    }
)
