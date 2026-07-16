from unittest.mock import MagicMock, patch

from producer.kafka_client import KafkaPublisher


@patch("producer.kafka_client.Producer")
def test_publish_sends_message_to_kafka(mock_producer_class):
    mock_producer = MagicMock()
    mock_producer_class.return_value = mock_producer

    publisher = KafkaPublisher(
        bootstrap_servers="broker:29092",
        topic="transactions_raw",
    )

    publisher.publish(
        value='{"transaction_id":"TX00000001"}',
        key="CUST00000001",
    )

    mock_producer.produce.assert_called_once_with(
        topic="transactions_raw",
        value='{"transaction_id":"TX00000001"}',
        key="CUST00000001",
        callback=KafkaPublisher.delivery_report, 
    )
    mock_producer.poll.assert_called_once_with(0)


@patch("producer.kafka_client.Producer")
def test_flush_calls_kafka_flush(mock_producer_class):
    mock_producer = MagicMock()
    mock_producer_class.return_value = mock_producer

    publisher = KafkaPublisher(
        bootstrap_servers="broker:29092",
        topic="transactions_raw",
    )

    publisher.flush()

    mock_producer.flush.assert_called_once()