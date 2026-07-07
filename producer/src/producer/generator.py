import time
import logging

from producer.transaction_factory import create_transaction
from producer.settings import TRANSACTIONS_PER_SECOND
from producer.logging_config import setup_logging

logger = logging.getLogger(__name__)

def generate_one_transaction(sequence_number: int):
    transaction = create_transaction(sequence_number)
    logger.info("Generated transaction %s", transaction.model_dump_json())
    return transaction

def main():
    setup_logging()

    sequence_number = 1

    while True:
        generate_one_transaction(sequence_number)
        sequence_number += 1
        time.sleep(1 / TRANSACTIONS_PER_SECOND)

if __name__ == "__main__":
    main()