"""
    根据 yapi 自动生成接口参数, 路由等基础信息, 已有的接口不会重复生成
    或许之后还能考虑接口改动然后进行文档的自动更新？
    doc - https://hellosean1025.github.io/yapi/openapi.html
    INTERFACE_GET_PATH = '/api/interface/get'
    INTERFACE_LIST_PATH = '/api/interface/list'
    INTERFACE_LIST_MENY_PATH = '/api/interface/list_menu'
    CAT_MENU_PATH = '/api/interface/getCatMenu'
"""
import requests


class AutoGenApiFromYapi(object):

    def __init__(self, host: str, project_token: str) -> None:
        self.host = host
        self.project_token = project_token

    def _get_project_info(self):
        """获取项目信息
        """
        url = self.host + '/api/project/get'
        params = {'token': self.project_token}
        resp = requests.get(url, params=params).json()
        print(resp)


AutoGenApiFromYapi(host='http://yapi.insight.ecc.huobiapps.com/', project_token='4494e3f04287007da1f3c76eedd794273637a2f50d831b7924bfad083b2f7a29')._get_project_info()