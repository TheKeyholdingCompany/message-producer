from kafka import KafkaProducer
import json

producer=None

def configure_producer(endpoint):
    global producer
    producer = KafkaProducer(bootstrap_servers=endpoint)


def send_event(dictionary, topic):
    print("Sending message")
    json_string = json.dumps(dictionary).encode('utf-8')
    producer.send(topic, json_string)
    producer.flush()
    print("Finish sending data")


def close_producer():
    producer.close()
