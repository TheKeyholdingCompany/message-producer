"""Kafka Broadcaster.

Usage:
    main.py send [--endpoint=<endpoint>] [--topic=<topic>] [--time-range=<time-range>]
    main.py listen [--endpoint=<endpoint>] [--topic=<topic>]
    main.py (-h | --help)
    main.py --version

Options:
    -h --help                  Show this screen.
    --version                  Show version.
    --endpoint=<endpoint>      Endpoint of the Kafka server [default: localhost:29092].
    --topic=<topic>            Topic to send the data [default: testing].
    --time-range=<time-range>  Time range to send the data [default: 1-3].

"""

#Imported functions
from event_maker import create_events
from sender import send_event, configure_producer, close_producer
from listener import listen as start_listening, configure_consumer
import time
from docopt import docopt
import random

arguments = docopt(__doc__, version='Naval Fate 2.0')

endpoint = arguments['--endpoint']
topic = arguments['--topic']
time_range = [int(n) for n in arguments['--time-range'].split("-")]


def listen():
    configure_consumer(endpoint, topic)
    start_listening()


def send():
    configure_producer(endpoint)

    events = create_events()
    for event in events:
        send_event(event, topic)
        time.sleep(random.randint(*time_range))

    close_producer()


if __name__ == '__main__':
    if arguments['send']:
        send()
    elif arguments['listen']:
        listen()
    else:
        print("Invalid option")
