from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka import Consumer

KAFKA_BROKER = "localhost:9092"
CONSUMER_GROUP_ID = "wabe"
TOPICS = [
    "wabe.client.query", # client queries from frontend
    "wabe.system.event"  # system generated events
    ]
POLL_TIMEOUT = 1 

def setup_topics(topic_names: list[str] = TOPICS, num_partitions: int = 1, replication_factor: int = 1):
    admin_client = AdminClient({"bootstrap.servers": KAFKA_BROKER})
    actual_topics = admin_client.list_topics(timeout = 5).topics

    topics = [NewTopic(x, num_partitions = num_partitions, replication_factor = replication_factor) 
              for x in topic_names if x not in actual_topics]
    if len(topics) > 0:
        future = admin_client.create_topics(topics)

        for topic, f in future.items():
            try:
                f.result()
                #TODO: set up logging and log this
            except Exception as e:
                #TODO log and handle
                raise e

def get_consumer(topic_names: list[str] = TOPICS):
    consumer = Consumer(
        {
            "bootstrap.servers": KAFKA_BROKER,
            "group.id": CONSUMER_GROUP_ID,
            "auto.offset.reset": "latest"
        }
    )
    consumer.subscribe(topic_names)
    return consumer