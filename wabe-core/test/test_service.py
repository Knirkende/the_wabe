from app.service.orchestrator import Orchestrator
from app.service.event_config import KAFKA_BROKER, TOPICS
from confluent_kafka.admin import AdminClient
from confluent_kafka import Producer
from test.unit_test_config import test_kafka_producer
import threading
import time

#TODO switch to test class, setup and teardown orchestrator.

def test_kafka_init():
    orchestrator = Orchestrator()

    admin_client = AdminClient({"bootstrap.servers": KAFKA_BROKER})

    actual_topics = admin_client.list_topics(timeout = 5).topics

    for t in TOPICS:
        assert(t in actual_topics)

def test_consumer(test_kafka_producer: Producer):
    orchestrator = Orchestrator()

    consumer_thread = threading.Thread(target = orchestrator.do_consume)
    consumer_thread.start()

    orchestrator.ready.wait()

    delivery_event = threading.Event()

    test_kafka_producer.produce(topic = 'wabe.system.event', key = 'stuff', value = 'value', callback = lambda err, msg: delivery_event.set())
    test_kafka_producer.flush()

    delivery_event.wait()

    time.sleep(30) #TODO Why does it take so long for consumer to consume

    orchestrator.running = False
    consumer_thread.join()