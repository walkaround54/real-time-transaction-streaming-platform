import time
import logging

from src.transaction_factory import create_transaction
from src.settings import TRANSACTIONS_PER_SECOND
from src.logging_config import setup_logging

logger = logging.getLogger(__name__)

def main():
    setup_logging()

    sequence_number = 1

    while True:
        transaction = create_transaction(sequence_number)
        logger.info(transaction.model_dump_json())
        sequence_number += 1
        time.sleep(1 / TRANSACTIONS_PER_SECOND)

if __name__ == "__main__":
    main()