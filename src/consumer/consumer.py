from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)


class Consumer:

    def __init__(self, host, topic):
        self.kafka_host = host
        self.kafka_topic = topic
        self.consumer = KafkaConsumer(
            self.kafka_topic,
            bootstrap_servers=self.kafka_host,
        )

    def consume_from_kafka(self):
        for message in self.consumer:
            logging.info(message.value)


if __name__ == "__main__":
    import sys
    print(sys.argv)
    consumer = Consumer(sys.argv[1], sys.argv[2])

    while True:
        consumer.consume_from_kafka()
