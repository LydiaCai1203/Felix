"""
    根据 yapi 文档自动生成接口的参数校验部分
"""
import requests
from requests import api
from requests.api import head


class AutoGenApiFromYapi(object):

    def __init__(self, host: str, project_token: str) -> None:
        self.host = host
        self.project_token = project_token

    def _get_project_info(self) -> dict:
        """获取项目基础信息
        """
        url = self.host + '/api/project/get'
        params = {'token': self.project_token}
        resp = requests.get(url, params=params).json()
        return (
            {
                'id': resp['data']['_id'],
                'basepath': resp['data']['basepath'],
                'name': resp['data']['name']
            }
            if '成功' in resp['errmsg'] else
            {}
        )

    def _get_interface_list_info(self, project_id: int) -> list:
        """获取接口列表信息
        """
        url = self.host + '/api/interface/list'
        headers = {'Content-Type': 'application/json'}
        params = {'project_id': project_id, 'token': self.project_token}
        resp = requests.get(url, headers=headers, params=params).json()
        return (
            [
                {
                    'id': i['_id'],
                    'method': i['method'],
                    'title': i['title'],
                    'path': i['path'],
                } for i in resp['data']['list']
            ]
            if '成功' in resp['errmsg'] else
            []
        )

    def _get_interface_info(self, api_id: int) -> dict:
        """获取单个接口信息
        """
        url = self.host + '/api/interface/get'
        headers = {'Content-Type': 'application/json'}
        params = {'id': api_id, 'token': self.project_token}
        resp = requests.get(url, headers=headers, params=params).json()
        return resp['data'] if '成功' in resp['errmsg'] else []

    def render_project(self):
        """生成项目目录信息以及基本的接口信息整合
        """
        pass

    def render_interface(self):
        """生成基础的接口结构和参数接口
        """
        pass

    def render_router(self):
        """生成路由信息
        """
        pass

    def render(self):
        pass


if __name__ == '__main__':
    # 让用户自己指定生成的文件目录
    host = 'http://yapi.insight.ecc.huobiapps.com'
    project_token = '4494e3f04287007da1f3c76eedd794273637a2f50d831b7924bfad083b2f7a29'
    data = AutoGenApiFromYapi(host=host, project_token=project_token)._get_interface_info(api_id=2168)
