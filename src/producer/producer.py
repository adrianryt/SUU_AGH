import csv
import json
import logging
from dataclasses import dataclass

from kafka import KafkaProducer
from kafka.errors import KafkaError

logging.basicConfig(level=logging.ERROR)

from datetime import datetime

@dataclass
class Row:
    ts: str
    device: str
    co: str
    humidity: str
    light: str
    lpg: str
    motion: str
    smoke: str
    temp: str


class Producer:
    def __init__(self, host):
        self.kafka_host = host
        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_host, value_serializer=lambda v: json.dumps(v).encode(),
        )

    def publish_to_kafka(self, message, topic):
        try:
            self.producer.send(topic, message)
            self.producer.flush()

        except KafkaError as ex:

            logging.error(f"Exception {ex}")
        else:
            logging.info(f"Published message {message} into topic {topic}")


if __name__ == "__main__":
    import sys

    producer = Producer(sys.argv[1])
    max_idx = int(sys.argv[2])
    idx = int(sys.argv[3])

    while True:
        with open('archive/iot_telemetry_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader, None)

            data_start = datetime(2020, 7, 12, 2, 1, 30)

            i = 0
            start = datetime.now()
            for r in reader:
                i += 1
                if i % max_idx != idx:
                    continue

                row = Row(*r)
                timestamp = datetime.fromtimestamp(float(row.ts))
                data_delta = timestamp - data_start

                while True:
                    if (datetime.now() - start) * 100 > data_delta:
                        break

                if row.light != "false":
                    topic = "light"
                else:
                    topic = "dark"

                producer.publish_to_kafka(r, topic)

                if float(row.temp) > 23.5:
                    topic = "warm"
                else:
                    topic = "cold"

                producer.publish_to_kafka(r, topic)
