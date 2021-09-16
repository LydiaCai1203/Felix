# 钉钉机器人安全设置
# https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
ROBOT_SECURITY_SIGN = "sign"
ROBOT_SECURITY_IP = "ip"
ROBOT_SECURITY_KEYWORD = "keyword"
# 默认请求头
ROBOT_DEFAULT_HEADER = {"Content-Type": "application/json;charset=utf-8"}


# 钉钉工作通知
# 钉钉发送工作通知返回的 errcode: 0 可以成功获取 task_id 
WORK_NOTICE_SEND_SUCCESS_CODE = 0
# 钉钉发送工作通知的发送进度返回的 errcode: 0 可以成功获取消息发送的进度
WORK_NOTICE_PROCESS_SUCCESS_CODE = 0
# 钉钉发送工作通知的发送进度返回的 status：2 消息发送处理完毕
WORK_NOTICE_PROCESS_FINISHED_STATUS = 2
# 钉钉发送工作通知的发送结果返回的 errcode：0 可以成功获取消息发送的结果
WORK_NOTICE_SEND_RET_SUCCESS_CODE = 0
# 消息发送结果
WORK_NOTICE_SUCCESS = 1
WORK_NOTICE_FAILED = 2
# 返回状态码判断
SUCCESS_REQUEST = 200
BAD_REQUEST = 400
INTERNAL_ERROR = 500


# 常量部分
PERM_STATUS_DELETED = 1


