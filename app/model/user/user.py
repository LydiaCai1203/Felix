from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.sql.schema import Index

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
    status = Column(TINYINT, nullable=False, default=0, comment='状态 0: 启用 1: 删除')
    created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')


class PermModel(BaseModel):

    __tablename__ = "perm"
    __table_args__ = {
        "mysql_charset": "utf8mb4",
        "mysql_engine": "innodb",
        "comment": "权限"
    }

    id = Column(Integer, primary_key=True, comment="自增ID")
    key = Column(String(16), nullable=False, unique=True, comment="perm key")
    name = Column(String(32), nullable=False, comment="展示名")
    created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')


class UserPermModel(BaseModel):

    __tablename__ = "user_perm"
    __table_args__ = (
        UniqueConstraint(
            'user_id',
            'perm_id',
            name='idx_user_id_perm_id',
        ),
        {
            "mysql_charset": "utf8mb4",
            "mysql_engine": "innodb",
            "comment": "用户权限关系表",
        }
    )

    id = Column(Integer, primary_key=True, comment="自增ID")
    user_id = Column(Integer, nullable=False, comment="user_id")
    perm_id = Column(Integer, nullable=False, comment="perm_id")
    status = Column(TINYINT, nullable=False, default=0, comment='状态 0: 启用 1: 删除')
    created = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
    updated = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"), comment='更新时间')