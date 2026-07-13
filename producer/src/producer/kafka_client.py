from confluent_kafka import Producer

class KafkaPublisher:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.topic = topic
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers,
            "acks": "all",
            "enable.idempotence": True, # more useful for when I replicate cluster
        })

    def publish(self, value:str, key: str | None = None) -> None:
        self.producer.produce(
            topic = self.topic,
            value = value,
            key = key,
        )
        self.producer.poll(0)

    def flush(self) -> None:
        self.producer.flush()