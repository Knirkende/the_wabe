from app.service.event_config import setup_topics, get_consumer,POLL_TIMEOUT
from confluent_kafka import Consumer, KafkaError
import signal
import threading

class Orchestrator():

    consumer: Consumer
    running: bool = True

    def __init__(self):
        self.ready = threading.Event()

        signal.signal(signal.SIGINT, self._signal_handler) # keyboard interrupt
        signal.signal(signal.SIGTERM, self._signal_handler) # k8s sigterm on graceful shutdown
        #signal.signal(signal.SIGKILL, self._signal_handler) #TODO consider if murder should be handled gracefully

        setup_topics()
        self.consumer = get_consumer()
        
        self.ready.set()
    
    def do_consume(self):
        try:
            while self.running:
                msg = self.consumer.poll(timeout = POLL_TIMEOUT)

                if msg is None or msg.error() and msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                if msg.error():
                    #TODO handle and log
                    print(f"Oh noes, Kafka error: {msg.error()}")
                    break
                
                # TODO actually do stuff with message
                print(f"Received message: {msg.key().decode('utf-8')} : {msg.value().decode('utf-8')} from {msg.topic()}")
        finally:
            #TODO log properly
            print("Closing consumer")
            self.ready.clear()
            self.consumer.close()
            print("Done")          

    def _signal_handler(self, sig, frame):
        self.running = False