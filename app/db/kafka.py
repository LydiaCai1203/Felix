import time
import json
from typing import Dict, Optional, Callable, List, Any

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

from app.handler.utils import local_robot
from settings import KAFKA_LOCAL_TOPIC, KAFKA_LOCAL_GROUP_ID, KAFKA_BASE_CONFIG


class Kafka(object):
    """ Kafka 连接工具类
    """

    def __init__(self, base_config: Dict[str, Any], topics: List[str]) -> None:
        self.consumer = KafkaConsumer(**base_config)
        self.consumer.subscribe(topics=topics)

    def consume(self, method_mapping: Dict[str, Callable]):
        try:
            for msg in self.consumer:
                try:
                    decoded_msg = self._deal_msg(msg)
                    # 数据过滤部分按需修改
                    for table_name_mod, method in method_mapping.items():
                        table_name, mod = table_name_mod.split(",")
                        if decoded_msg["table"] != table_name or (
                            mod != "NONE" and mod in decoded_msg["type"] != mod
                        ):
                            continue

                        try:
                            method(decoded_msg["data"][0])
                        except Exception as e:
                            __import__("traceback").print_exc()
                            local_robot.send_msg(e)
                except Exception as e:
                    __import__("traceback").print_exc()
                    local_robot.send_msg(e)
        except Exception as e:
            __import__("traceback").print_exc()
            local_robot.send_msg(e)

    def _deal_msg(self, msg: ConsumerRecord) -> Optional[dict]:
        try:
            msg = json.loads(msg.value.decode())
            return msg
        except:
            __import__("traceback").print_exc()
            return None

    def run(self, method_mapping: Dict[str, Callable]):
        """启动监听
        """
        while True:
            try:
                self.consume(method_mapping)
            except:
                __import__("traceback").print_exc()
                self.stop()
            time.sleep(10)

    def stop(self):
        self.consumer.close()


# 使用方式，按需修改
# def deal_sth(): pass
# KAFKA_CONF = {
#     'bootstrap_servers': KAFKA_BASE_CONFIG['localhost']['bootstrap_servers'],
#     'auto_offset_reset': 'latest',
#     'enable_auto_commit': True,
#     'group_id': KAFKA_GROUP_ID
# }
# table_mapping = {f'TEST_TABLE_NAME,INSERT': deal_sth}
# Kafka(base_config=KAFKA_CONF, topics=[KAFKA_TOPIC]).run(table_mapping)
