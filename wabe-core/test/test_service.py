from app.service.orchestrator import Orchestrator
from app.service.event_config import KAFKA_BROKER, TOPICS
from confluent_kafka.admin import AdminClient

def test_kafka_init():
    orchestrator = Orchestrator()

    admin_client = AdminClient({"bootstrap.servers": KAFKA_BROKER})

    actual_topics = admin_client.list_topics(timeout = 5).topics

    for t in TOPICS:
        print(t)
        assert(t in actual_topics)

