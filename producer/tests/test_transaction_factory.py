from producer.transaction_factory import create_transaction

def test_create_transaction_returns_valid_transaction():
    transaction = create_transaction(1)

    assert transaction.transaction_id == "TX00000001"
    assert transaction.customer_id.startswith("CUST")
    assert transaction.account_id.startswith("ACC")
    assert transaction.merchant_id.startswith("MRC")
    assert transaction.amount > 0
    assert transaction.currency in ["SGD", "MYR", "THB", "IDR", "USD"]