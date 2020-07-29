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
        "host": env.str("MAIN_MYSQL_HOST", "localhost"),
        "port": env.int("MAIN_MYSQL_PORT", 3306),
        "user": env.str("MAIN_MYSQL_USER", "root"),
        "password": env.str("MAIN_MYSQL_PWD", ""),
        "db": env.str('MAIN_MYSQL_DB', "medusa_dev"),
        "charset": 'UTF8MB4'
    }
)
define(
    "redis",
    default={
        "host": env.str("MAIN_REDIS_HOST", "127.0.0.1"),
        "port": env.int("MAIN_REDIS_PORT", 6379),
        # "password": env.str("MAIN_REDIS_PWD", ""),
        "db": env.str('MAIN_REDIS_DB', "6")
    }
)
define(
    "session_prefix",
    type=str,
    default=env.str("SESSION_PREFIX", "MEDUSA.")
)
define(
    "expire_time",
    type=int,
    default=env.int("EXPIRE_TIME", 60 * 60 * 8)
)


options.parse_command_line()
print("========= Medusa Backend Framework ==========")
print(f"#### port: {options.port}")
print(f"#### env: {options.env}")
print(f"#### debug: {options.autoreload}")
