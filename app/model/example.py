from sqlalchemy import Column, Integer, String

from app.model import BaseModel


class ExampleModel(BaseModel):

    __tablename__ = 'example'
    __table_args__ = {
        'mysql_charset': 'utf8mb4',
        'mysql_engine': 'innodb',
        'comment': '样例'
    }

    id = Column(Integer, primary_key=True, comment='自增ID')
    name = Column(String(32), nullable=False, comment='姓名')