"""
    配置文件
"""
from tornado.options import define, options
from environs import Env


env = Env()
env.read_env()

# 连接配置
define(
    "autoreload",
    type=bool,
    default=env.bool("AUTORELOAD", True)
)
define(
    "env",
    type=str,
    default=env.str("ENV", "DEV")
)
define(
    "port",
    type=int,
    default=env.int("PORT", 8009)
)
define(
    "mysql",
    default={
        "host": env.str("MAIN_MYSQL_HOST", "127.0.0.1"),
        "port": env.int("MAIN_MYSQL_PORT", 3306),
        "user": env.str("MAIN_MYSQL_USER", "root"),
        "password": env.str("MAIN_MYSQL_PWD", "root123"),
        "db": env.str('MAIN_MYSQL_DB', "felix_dev"),
        "charset": 'UTF8MB4'
    }
)
define(
    "redis",
    default={
        "host": env.str("MAIN_REDIS_HOST", "127.0.0.1"),
        "port": env.int("MAIN_REDIS_PORT", 6379),
        # "password": env.str("MAIN_REDIS_PWD", ""),
        "db": env.int('MAIN_REDIS_DB', 6)
    }
)
define(
    "session_prefix",
    type=str,
    default=env.str("SESSION_PREFIX", "Felix.")
)
define(
    "expire_time",
    type=int,
    default=env.int("EXPIRE_TIME", 60 * 60 * 8)
)


options.parse_command_line()
print("========= Felix Backend Framework Base Tornado ==========")
iron = """


88888888888          88  88               
88                   88  CC               
88                   88                   
88aaaaa   ,adPPYba,  88  88  8b,     ,d8  
88bbbbb  a8P_____88  88  88   `Y8, ,8P'   
88       8PPP8P8P8P  88  88     )888(     
88       "8b,   ,aa  88  88   ,d8" "8b,   
88        `"Ybbd8"'  88  88  8P'     `Y8  


"""
print(iron)
print(f"#### port: {options.port} ####")
print(f"#### env: {options.env} ####")
print(f"#### debug: {options.autoreload} ####")
