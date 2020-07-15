from sqlalchemy import Column, Integer, String

from app.model import BaseModel


class UserModel(BaseModel):

    __tablename__ = "user"
    __table_args__ = {
        "mysql_charset": "utf8mb4",
        "mysql_engine": "innodb",
        "comment": "用户"
    }

    id = Column(Integer, primary_key=True, comment="自增ID")
    account = Column(String(16), nullable=False, comment="账户")
    nickname = Column(String(32), nullable=False, comment="展示名")
    email = Column(String(64), nullable=False, unique=True, comment="邮箱")
    password = Column(String(256), nullable=False, comment="密码")