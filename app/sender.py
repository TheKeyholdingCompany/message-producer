from kafka import KafkaProducer
import json

kafka_host="192.168.10.221"
kafka_port="29092"

# def get_event():
#     dictionary= {
#         'millie':'15',
#         'lassi':'15',
#         'dila':'15'
#     }
#     return(dictionary)

def send_event(dictionary):
    print("sending message")
    json_string = json.dumps(dictionary).encode('utf-8')
    print("A")
    producer.send('testing',json_string)
    print("B")
    producer.flush()
    print("Finish sending data")

def main(data):
    dictionary = data
    send_event(dictionary)

producer = KafkaProducer(bootstrap_servers=f'{kafka_host}:{kafka_port}')

