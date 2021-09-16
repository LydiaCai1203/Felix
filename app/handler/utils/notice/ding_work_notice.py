import json
import traceback
from typing import Dict, Union

import requests

from settings import WORK_NOTICE_DING_CONF as WN_CONF
from app.handler.consts import (
    WORK_NOTICE_SEND_SUCCESS_CODE,
    WORK_NOTICE_PROCESS_SUCCESS_CODE,
    WORK_NOTICE_PROCESS_FINISHED_STATUS,
    WORK_NOTICE_SEND_RET_SUCCESS_CODE,
    SUCCESS_REQUEST,
    INTERNAL_ERROR,
    BAD_REQUEST,
)


class WorkNoticeService(object):

    def __init__(self):
        """初始化
        """
        self.agent_id = WN_CONF['agent_id']
        self.app_key = WN_CONF['app_key']
        self.app_secret = WN_CONF['app_secret']
        self.get_token_url = WN_CONF['get_token_url']
        self.send_msg_url = WN_CONF['send_msg_url']
        self.get_send_ret_url = WN_CONF['get_send_ret_url']
        self.get_send_process_url = WN_CONF['get_send_process_url']
        self.get_recall_url = WN_CONF['get_recall_url']
        self.access_token = self.__get_token()
    
    def work_notice(self, post_body: dict):
        """发送工作通知消息

        Args:
            post_body: dict -- 发送工作消息通知请求体
        
        Returns:
            dict -- 消息发送结果
        """
        payload = {'access_token': self.access_token}
        post_body.update({'agent_id': self.agent_id})
        resp = requests.post(
            self.send_msg_url, 
            params=payload, 
            json=post_body
        ).json()

        if resp['errcode'] == WORK_NOTICE_SEND_SUCCESS_CODE:
            send_ret = self.__get_send_msg_ret(resp['task_id'])
        else:
            send_ret = resp['errmsg']
        
        code = self.__judge_notice_result(send_ret)

        send_ret_str = json.dumps(send_ret)
        return {
            'code': code,
            'data': send_ret_str if code == SUCCESS_REQUEST else '',
            'msg': '' if code == SUCCESS_REQUEST else send_ret_str
        }

    def __get_token(self) -> str:
        """获取企业凭证 access_token

        Returns:
            str -- access_token
        """
        payload = {
            'appkey': self.app_key, 
            'appsecret': self.app_secret
        }
        resp = requests.get(
            self.get_token_url, 
            params=payload
        ).json()
        return resp.get('access_token')

    def __get_send_msg_ret(self, task_id: int) -> Union[str, dict]:
        """获取消息发送的结果信息

        Args:
            task_id: int -- 钉钉返回的任务ID, 仅支持查询24小时内的任务ID
        
        Returns:
            str -- 消息发送的结果
        """
        body = {
            'agent_id': self.agent_id,
            'task_id': task_id
        }
        try:
            while True:
                resp = requests.post(
                    self.get_send_process_url,
                    params={'access_token': self.access_token},
                    data=body,
                ).json()

                if resp['errcode'] != WORK_NOTICE_PROCESS_SUCCESS_CODE:
                    return resp['errmsg']

                if (
                    resp['errcode'] == WORK_NOTICE_PROCESS_SUCCESS_CODE
                    and resp['progress']['status'] == WORK_NOTICE_PROCESS_FINISHED_STATUS
                ):
                    break

            # 发送结果
            resp = requests.post(
                self.get_send_ret_url,
                params={'access_token': self.access_token},
                data=body,
            ).json()

            return (
                resp['send_result']
                if resp['errcode'] == WORK_NOTICE_SEND_RET_SUCCESS_CODE else 
                resp['errmsg']
            )
        except:
            exec_str = traceback.format_exc()
            return exec_str

    def __judge_notice_result(self, send_ret: Union[str, dict]) -> int:
        """从结果信息里面判断此次消息有没有发送成功, 返回状态码

        Args:
            send_ret -- 成功失败的字符串信息

        Returns:
            int -- code 响应状态码
        """
        code = SUCCESS_REQUEST
        if isinstance(send_ret, dict):
            code = (
                BAD_REQUEST
                if any(
                    send_ret.get('failed_user_id_list'),
                    send_ret.get('forbidden_list'),
                    send_ret.get('forbidden_user_id_list'),
                    send_ret.get('invalid_dept_id_list'),
                    send_ret.get('invalid_user_id_list')
                ) else 
                INTERNAL_ERROR
            )
        return code


work_notice = WorkNoticeService()