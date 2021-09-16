import time
import hmac
import hashlib
import base64
from typing import Tuple

import requests

from app.handler.utils import RobotMsgService
from settings import ROBOT_DING_CONF, ROBOT_GROUP
from app.handler.consts import ( 
    ROBOT_SECURITY_SIGN,
    ROBOT_DEFAULT_HEADER
)


class RobotMsgService(object):

    def __init__(self, access_token: str, security_way: str, secret_key: str=None):
        """初始化

        Args:
            access_token: str - 钉钉机器人的 access_token
            security_way: str - 钉钉机器人通信的安全模式("sign" or "keyword")
            secret_key: str - 与 secret_way 对应，为签名的密钥
        """
        super().__init__()
        self.access_token = access_token
        self.secret_key = secret_key
        self.security_way = security_way
        self.send_msg_url = ROBOT_DING_CONF["send_msg_url"]
        self.post_header = ROBOT_DEFAULT_HEADER
    
    def __cal_sign(self) -> Tuple[int, str]:
        """计算签名(Robot 的安全设置为加签时需要计算)
        
        Returns:
            Tuples[int, str] -- (timestamp, sign)
        """
        timestamp = int(round(time.time(), 3) * 1000)
        secret_enc = self.secret_key.encode() if self.secret_key else b""
        string_to_sign = "{}\n{}".format(timestamp, self.secret_key)
        string_to_sign_enc = string_to_sign.encode()
        hmac_code = hmac.new(
            secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
        ).digest()
        sign = base64.b64encode(hmac_code).decode("utf-8")
        return timestamp, sign
    
    def send_msg(self, msg_body: dict) -> dict:
        """发送消息

        Args:
            msg_body: dict -- 钉钉发送消息通知的请求体, 请求格式详见 readme.md
        
        Returns:
            dict -- 消息结果
        """
        params = {
            "access_token": self.access_token
        }
        if self.security_way == ROBOT_SECURITY_SIGN:
            timestamp, sign = self.__cal_sign()
            params.update({
                "timestamp": str(timestamp),
                "sign": sign
            })
        
        try:
            resp = requests.post(
                url=self.send_msg_url,
                params=params,
                json=msg_body,
                headers=self.post_header,
                timeout=3,
            ).json()
        except Exception as e:
            resp = {"err_code": 500, "err_msg": str(e)}
        return resp


local_robot = RobotMsgService(**ROBOT_GROUP["local_robot"])