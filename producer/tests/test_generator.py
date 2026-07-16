from producer.generator import generate_one_transaction, publish_one_transaction
from unittest.mock import MagicMock, patch

def test_generate_one_transaction():
    transaction = generate_one_transaction(1)

    assert transaction.transaction_id == "TX00000001"
    assert transaction.customer_id.startswith("CUST")
    assert transaction.account_id.startswith("ACC")
    assert transaction.amount > 0

@patch("producer.generator.create_transaction")
def test_publish_one_transaction(mock_create_transaction):
    mock_transaction = MagicMock()
    mock_transaction.model_dump_json.return_value = '{"transaction_id":"TX00000001"}'
    mock_transaction.customer_id = "CUST00000001"
    mock_create_transaction.return_value = mock_transaction

    mock_publisher = MagicMock()
    transaction = publish_one_transaction(1, mock_publisher)

    mock_create_transaction.assert_called_once_with(1)
    mock_transaction.model_dump_json.assert_called_once()
    mock_publisher.publish.assert_called_once_with(
        value='{"transaction_id":"TX00000001"}',
        key="CUST00000001",       
    )

    assert transaction is mock_transaction
