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
    type=dict,
    default={
        "host": env.str("MYSQL_HOST", "127.0.0.1"),
        "port": env.int("MYSQL_PORT", 3306),
        "user": env.str("user", "root"),
        "password": env.str("password", ""),
        "db": "test_db"
    }
)


options.parse_command_line()
print("========= Medusa Backend Framework ==========")
print(f"## port: {options.port} ##")
print(f"## env: {options.env} ##")
print(f"## debug: {options.autoreload} ##")