import time
from src.transaction_factory import create_transaction

def main():
    sequence_number = 1
    while True:
        transaction = create_transaction(sequence_number)
        print(transaction.model_dump_json(indent=2))
        sequence_number += 1
        time.sleep(1)

if __name__ == "__main__":
    main()