import time
import logging

from producer.transaction_factory import create_transaction
from producer.settings import TRANSACTIONS_PER_SECOND, KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
from producer.logging_config import setup_logging
from producer.kafka_client import KafkaPublisher

logger = logging.getLogger(__name__)

def generate_one_transaction(sequence_number: int):
    transaction = create_transaction(sequence_number)
    return transaction

def publish_one_transaction(sequence_number: int, publisher: KafkaPublisher):
    transaction = generate_one_transaction(sequence_number)
    transaction_as_json = transaction.model_dump_json()
    # transaction.model_dump() returns python dict
    # transaction.model_dump_json() returns json str
    logger.info("Generated transaction %s", transaction_as_json)
    publisher.publish(value=transaction_as_json, key=transaction.customer_id)
    return transaction

def main():
    setup_logging()

    publisher = KafkaPublisher(
        bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
        topic = KAFKA_TOPIC,
    )

    try:
        sequence_number = 1

        while True:
            publish_one_transaction(sequence_number, publisher)
            sequence_number += 1
            time.sleep(1 / TRANSACTIONS_PER_SECOND)
    finally:
        # flush all remaining transactions when generator stops
        publisher.flush()

if __name__ == "__main__":
    main()