import logging
import os

from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)

import time
import random


class Consumer:
    def __init__(self, host, topics):
        self.kafka_host = host
        self.kafka_topic = topics
        print(self.kafka_topic)
        self.consumer = KafkaConsumer(
            bootstrap_servers=self.kafka_host,
            max_poll_records=int(os.getenv("max_poll_records", "500")),
            group_id=os.getenv("consumer_group", None)
        )
        self.consumer.subscribe(self.kafka_topic)

    def consume_from_kafka(self):
        result = next(self.consumer)
        logging.info(result)
        return result


if __name__ == "__main__":
    import sys
    consumer = Consumer(sys.argv[1], [topic for topic in sys.argv[2].split(",")])

    interval = os.getenv("poll_interval")

    print(interval)

    while True:
        consumer.consume_from_kafka()
        if interval:
            time.sleep(int(interval))
        else:
            time.sleep(random.randint(25, 75) / 100)
