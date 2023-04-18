import csv
import json
import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.ERROR)


class Producer:
    def __init__(self, host, topic):
        self.kafka_host = host
        self.kafka_topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_host, value_serializer=lambda v: json.dumps(v).encode(),
        )

    def publish_to_kafka(self, message):
        try:
            self.producer.send(self.kafka_topic, message)
            self.producer.flush()

        except KafkaError as ex:

            logging.error(f"Exception {ex}")
        else:
            logging.info(f"Published message {message} into topic {self.kafka_topic}")


if __name__ == "__main__":
    import sys

    print(sys.argv)
    producer = Producer(sys.argv[1], sys.argv[2])
    producer.publish_to_kafka("hello")


    with open('archive/analyst_ratings_processed.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader, None)
        print("header" + str(header))
        for row in reader:
            producer.publish_to_kafka(row)
