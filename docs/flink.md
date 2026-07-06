# Flink

## Purpose

Apache Flink is the real-time stream processing engine of the platform.

## Responsibilities

- Consume `transactions_raw`
- Validate and enrich events
- Maintain customer state with RocksDB
- Execute fraud detection rules
- Produce processed transactions, alerts and KPI streams

## DataStream API

Key concepts:

- Source
- Sink
- Map
- Filter
- KeyBy
- Window
- ProcessFunction
- KeyedProcessFunction
- Side Outputs

## Stateful Processing

State stored per customer:

- Rolling spend (5 min)
- Transaction count
- Failed transaction count
- Previous country
- Historical average amount

## Flink SQL

Used for:

- Transaction volume/minute
- Total amount/minute
- Average transaction size
- Failed transaction rate
- Alert count/minute

## Outputs

- transactions_processed
- transactions_alerts
- transactions_kpi
- transactions_error

## Future Enhancements

- Checkpointing
- Savepoints
- Exactly-once processing
- Event-time watermarks
- Schema Registry integration