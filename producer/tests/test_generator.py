from producer.src.generator import generate_one_transaction

def test_generate_one_transaction():
    transaction = generate_one_transaction(1)

    assert transaction.transaction_id == "TX00000001"
    assert transaction.customer_id.startswith("CUST")
    assert transaction.account_id.startswith("ACC")
    assert transaction.amount > 0