"""
    handler 工具
"""
from sqlalchemy.sql import asc, desc
from sqlalchemy.orm.query import Query


class GeneralIntfTools:

    def gen_order_conds(self, order_fields: str, order_ways: str) -> list:
        """ 生成排序条件

            Args:
                order_fields: str -- 排序字段，英文逗号分隔
                order_ways: str -- 排序方式，英文逗号分隔 eg. asc or desc
        """
        order_fields = order_fields.split(',')
        order_ways = order_ways.split(',')
        order_conds = []
        for order_field, order_way in zip(order_fields, order_ways):
            func = asc if order_way == 'asc' else desc
            order_conds.append(func(order_field))
        return order_conds

    def add_pagination_conds(self, expr: Query, page_size: int, page_num: int) -> Query:
        """ 获取分页条件

            Args:
                expr: Query -- orm sql statements
                page_size: int -- 页大小
                page_num: int -- 页码
        """
        return (
            expr.offset((page_num - 1) * page_size)
            .limit(page_size)
        )
