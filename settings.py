"""
    配置文件
"""
from tornado.options import define, options
from environs import Env


env = Env()
env.read_env()

# 连接配置
define("autoreload", type=bool, default=env.bool("AUTORELOAD", True))
define("env", type=str, default=env.str("ENV", "DEV"))
define("port", type=int, default=env.int("PORT", 8009))
define("session_prefix", type=str, default=env.str("SESSION_PREFIX", "Felix."))
define("expire_time", type=int, default=env.int("EXPIRE_TIME", 60 * 60 * 8))

# db
MYSQL_CONF = {
    "localhost": {
        "host": env.str("MAIN_MYSQL_HOST", "127.0.0.1"),
        "port": env.int("MAIN_MYSQL_PORT", 3306),
        "user": env.str("MAIN_MYSQL_USER", "root"),
        "password": env.str("MAIN_MYSQL_PWD", "root123"),
        "db": env.str("MAIN_MYSQL_DB", "felix_dev"),
        "charset": "UTF8MB4",
    }
}

REDIS_CONF = {
    "localhost": {
        "host": env.str("MAIN_REDIS_HOST", "127.0.0.1"),
        "port": env.int("MAIN_REDIS_PORT", 6379),
        # "password": env.str("MAIN_REDIS_PWD", ""),
        "db": env.int("MAIN_REDIS_DB", 6),
    }
}

# KAFKA
KAFKA_BASE_CONFIG = {
    "localhost": {"bootstrap_servers": [env.str("KAFKA_LOCAL_HOST", "")]}
}
KAFKA_LOCAL_TOPIC = env.str("KAFKA_LOCAL_TOPIC", "")
KAFKA_LOCAL_GROUP_ID = env.str("KAFKA_LOCAL_GROUP_ID", "")


# ES
ES_BASE_CONF = {
    "localhost": {
        "user": env.str("ES_LOCAL_USER", ""),
        "password": env.str("ES_LOCAL_PWD", ""),
        "host": [env.str("ES_LOCAL_HOST", "")],
    }
}
LOCAL_ES_INDEX = env.str("ES_LOCAL_INDEX", "")


# dingding - 群机器人发送消息
ROBOT_DING_CONF = {"send_msg_url": "https://oapi.dingtalk.com/robot/send"}
ROBOT_GROUP = {
    "local_robot": {
        "access_token": env.str("LOCAL_DING_ROBOT_ACCESS_TOKEN", ""),
        "security_way": env.str("LOCAL_DING_ROBOT_SECURITY_WAY", ""),
        "access_token": env.str("LOCAL_DING_ROBOT_SECRET_KEY", ""),
    }
}

# dingding - 工作通知发送信息
WORK_NOTICE_DING_CONF = {
    "agent_id": env.int("DING_AGENT_ID", 0),
    "app_key": env.str("DING_APP_KEY", ""),
    "app_secret": env.str("DING_APP_SECRET", ""),
    "get_token_url": "https://oapi.dingtalk.com/gettoken",
    "send_msg_url": "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2",
    "get_send_ret_url": "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult",
    "get_send_process_url": "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendprogress",
    "get_recall_url": "https://oapi.dingtalk.com/topapi/message/corpconversation/recall",
}


options.parse_command_line()
print("========= Felix Backend Framework Base Tornado ==========")
iron = """


88888888888          88  88               
88                   88  CC               
88                   88                   
88aaaaa   ,adPPYba,  88  88  8b,     ,d8  
88bbbbb  a8P_____88  88  88   `Y8, ,8P"   
88       8PPP8P8P8P  88  88     )888(     
88       "8b,   ,aa  88  88   ,d8" "8b,   
88        `"Ybbd8""  88  88  8P"     `Y8  


"""
print(iron)
print(f"#### port: {options.port} ####")
print(f"#### env: {options.env} ####")
print(f"#### debug: {options.autoreload} ####")
