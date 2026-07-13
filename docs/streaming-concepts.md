# Streaming Concepts

## Purpose

Phase 4 prepares the platform for Apache Flink by defining how transaction events behave in a streaming system. This phase does not introduce a Flink job or change the producer-to-Kafka flow.

The existing path remains:

```text
Python producer -> Kafka topic: transactions_raw
```

## Event Time And Processing Time

`event_time` in a transaction event is the time when the simulated transaction occurred. It is generated in UTC by the Python producer and will be the event-time field used by Flink.

Processing time is the time at which a Flink task receives and processes that event. Processing time can differ from event time because of network delay, Kafka backlog, retries, or downstream backpressure.

## Keying And Ordering

The producer uses `customer_id` as the Kafka message key. Kafka assigns records with the same key to the same topic partition, so their order is preserved within that partition.

This supports customer-level processing in a later Flink job with `keyBy(customerId)`. Kafka does not provide a single global order across all partitions.

## Initial Windowing Contract

The first Flink job will calculate these metrics from `transactions_raw` in one-minute tumbling event-time windows:

- transaction count
- total transaction amount
- average transaction amount
- failed transaction count

The initial job will publish its results to `transactions_processed` as defined in the roadmap. The exact output event schema will be designed before implementation.

## Watermarks And Late Events

A watermark estimates that the stream has progressed beyond a point in event time. It allows an event-time window to close even when events do not arrive in timestamp order.

The initial policy should allow a small out-of-order tolerance, such as 30 seconds. Events that arrive after the watermark must have an explicit outcome: drop and count them, or send them to a side output for inspection. The selected policy should be documented with the first Flink job.

## Consumer Groups, Offsets, And Replay

A consumer group stores its committed position for each Kafka partition. This lets a consumer restart from its last committed offset instead of reading the topic from the beginning.

Use a named test consumer group against `transactions_raw` to practise:

- observing committed offsets
- restarting from its committed position
- replaying records with a new group ID or an offset reset

## Delivery Guarantees And Checkpointing

The producer is configured with `acks=all` and idempotence. These settings reduce the chance of duplicate or lost producer writes, but they do not make the full producer-to-Flink-to-Kafka flow exactly once.

Flink checkpointing will later record consistent processing progress and state. End-to-end exactly-once processing requires compatible Kafka source and sink configuration in addition to checkpoints.

## Backpressure And Lag

When processing is slower than production, records remain in Kafka and consumer lag grows. Backpressure is the downstream pressure that slows work inside a streaming pipeline when an operator or sink cannot keep up.

Kafka decouples the producer from that slower consumer, but retention limits still determine how long the backlog remains available for processing or replay.

## Phase 4 Exit Criteria

- Event-time and processing-time behaviour is understood and documented.
- The first window, watermark tolerance, and late-event outcome are chosen.
- Consumer groups, offsets, and replay have been exercised on the local broker.
- The relationship between producer idempotence, checkpoints, and end-to-end delivery guarantees is clear.
- The first Flink job has a defined Kafka input, output, key, and aggregation contract.
