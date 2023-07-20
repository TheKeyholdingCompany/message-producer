from kafka import KafkaConsumer
import json

consumer = None


def configure_consumer(endpoint, topic):
    global consumer
    consumer = KafkaConsumer(topic,
                            bootstrap_servers=endpoint,
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')))


def listen():
    for message in consumer:
        data = message.value
        print(data)

    consumer.close()