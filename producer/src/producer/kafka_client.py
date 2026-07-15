from confluent_kafka import Producer

class KafkaPublisher:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.topic = topic
        self.producer = Producer({
            "bootstrap.servers": bootstrap_servers,
            "acks": "all",
            "enable.idempotence": True, # more useful for when I replicate cluster

            "batch.num.messages": 10, # for Java Producer, user batch.size
            "linger.ms": 5,
        })

    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            print(
                f"Delivery failed for topic={msg.topic()} "
                f"partition={msg.partition()} offset={msg.offset()}: {err}"
            )

    def publish(self, value:str, key: str | None = None) -> None:
        self.producer.produce(
            topic = self.topic,
            value = value,
            key = key,
            callback = self.delivery_report
        )
        self.producer.poll(0)

    def flush(self) -> None:
        self.producer.flush()