"""
    handler 工具
"""
from sqlalchemy.sql import asc, desc
from sqlalchemy.orm.query import Query


class GeneralIntfTools:

    def sql_order(self, expr: Query, is_desc: int, order_fields: str) -> Query:
        """ 获取排序 query expr

        Args:
            expr: Query - 查询语句
            is_desc: int - 排序类型，0-升序 1-降序
            order_fields: str - 排序字段，英文逗号分割
        """
        order_func = desc if is_desc else asc
        return expr.order_by(
            *[
                order_func(order_field) 
                for order_field in order_fields.split(",")
            ]
        )

    def sql_pagination(self, expr: Query, page_size: int, page_num: int) -> Query:
        """ 获取分页条件

        Args:
            expr: Query - 查询语句
            page_size: int - 页大小
            page_num: int - 页码
        """
        return (
            expr.offset((page_num - 1) * page_size)
            .limit(page_size)
        )
