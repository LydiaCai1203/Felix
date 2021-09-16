import time
import json
from typing import Dict, Optional, Callable, List, Any

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

from app.handler.utils import local_robot


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
                    for table_name_mod, method in method_mapping.items():
                        table_name, mod = table_name_mod.split(",")
                        if (
                            decoded_msg["table"] != table_name
                            or (mod != "NONE" and mod in decoded_msg["type"] != mod)
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
