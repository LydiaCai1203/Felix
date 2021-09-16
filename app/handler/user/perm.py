import traceback

from sqlalchemy.log import echo_property

from webargs import fields
from webargs.tornadoparser import use_args
from sqlalchemy.sql import or_

from app.handler import BaseHandler
from app.handler.utils import GeneralIntfTools
from app.route import BaseApplication as router
from app.model.user.user import PermModel
from app.db import Session
from app.handler.const import PERM_STATUS_DELETED


@router.route("/api/v1/perms")
class PermsHandler(BaseHandler, GeneralIntfTools):

    @use_args(
        {
            "key": fields.Str(required=True, help='perm key'),
            "name": fields.Str(required=True, help='perm show name'),
        },
        location="json"
    )
    def post(self, post_args: dict):
        """ create perm
        """
        try:
            perm = PermModel(**post_args)
            self.sess.add(perm)
            self.sess.commit()
        except Exception:
            traceback.print_exc()
            self.sess.rollback()
            return self.write_error(status_code=500, msg="insert perm failed")
        return self.write_json(msg="insert perm successfully")

    @use_args(
        {
            "search_text": fields.Str(required=False, help='搜索字段'),

            "order_fields": fields.Str(required=False, missing='id', help='排序字段'),
            "is_desc": fields.Int(required=False, missing=1, help='排序方式'),
            "page_size": fields.Int(required=False, missing=10, help='页大小'),
            "page_num": fields.Int(required=False, missing=1, help='页码'),
        },
        location="query"
    )
    def get(self, get_args: dict):
        """ check perms
        """
        search_text = get_args.get("search_text", "")
        search_text = search_text.strip(" ")
        expr = (
            self.sess.query(PermModel)
            .filter(
                or_(
                    PermModel.key.like(f"{search_text}%"),
                    PermModel.name.like(f"{search_text}%")
                )
            )
        )

        total = expr.count()
        expr = self.sql_order(expr, get_args["is_desc"], get_args["order_fields"])
        expr = self.sql_pagination(expr, get_args["page_size"], get_args["page_num"])

        data = [
            {'id': i.id, 'key': i.key, 'perm': i.name}
            for i in expr.yield_per(100)
        ]

        return self.write_json(
            data={
                'total': total,
                'page_size': get_args["page_size"],
                'page_num': get_args["page_num"],
                'data': data
            }
        )


@router.route(r"/api/v1/perms/detail/(\d+)")
class PermsDetailHandler(BaseHandler):

    def delete(self, pid: str, *args):
        try:
            self.sess.query(PermModel.id).filter(PermModel.id == str(pid)).delete()
            self.sess.commit()
        except Exception:
            exc_msg = __import__('traceback').format_exc()
            self.sess.rollback()
            return self.write_error(status_code=500, msg=f'delete perm failed: {exc_msg}')
        else:
            return self.write_json(status=200, msg='delete perm successfully')

    @use_args(
        {
            "key": fields.Str(required=False, help='perm key'),
            "name": fields.Str(required=False, help='perm name'),
        },
        location="json"
    )
    def patch(self, pid: str, patch_args: dict):

        patch_body = dict()

        if 'key' in patch_args and patch_args['key']:
            patch_body.update({PermModel.key: patch_args['key']})
        if 'name' in patch_args and patch_args['name']:
            patch_body.update({PermModel.name: patch_args['name']})

        try:
            (
                self.sess.query(PermModel.id)
                .filter(PermModel.id == int(pid))
                .update(patch_body)
            )
            self.sess.commit()
        except Exception:
            exc_msg = __import__('traceback').format_exc()
            self.sess.rollback()
            return self.write_json(status=500, msg=f'patch perm failed: {exc_msg}')
        else:
            return self.write_json(status=200, msg='patch perm successfully')
