# Flink

## Purpose

Apache Flink is the real-time stream processing engine of the platform.

## Project Version And API Choice

- Project Flink version: Apache Flink 2.2.1.
- Primary implementation API: Java DataStream API.
- First learning focus: Kafka source and sink, JSON parsing, event time, watermarks, keyed streams, windows and checkpointing.
- Flink SQL will be introduced later for analytics and KPI-style streams after the first Java DataStream job is working.
- PyFlink is intentionally out of scope for now so the project can focus on Flink's production-oriented Java APIs first.

## Responsibilities

- Consume `transactions_raw`
- Validate and enrich events
- Maintain customer state with RocksDB
- Execute fraud detection rules
- Produce processed transactions, alerts and KPI streams

## DataStream API

The Java DataStream API is the primary API for the first Flink implementation.

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

- Rolling spend
- Transaction count
- Failed transaction count
- Previous country
- Historical average amount

## Flink SQL

Flink SQL is planned as a later addition for declarative analytics once the Java DataStream processing path is understood.

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

## Streaming Concepts

Use this section to record the Flink-side streaming concepts needed before building the first Flink job.

### Event Time

- `event_time` is the time when the simulated transaction occurred.
- Flink should use the transaction model's `event_time` field as the event-time timestamp.
- `event_time` is generated in UTC by the Python producer.
- Event time should drive transaction windows because it represents business time, not system processing time.

### Processing Time

- Processing time is the time when Flink processes an event.
- Processing time can be useful for operational monitoring, debugging delay, and identifying pipeline bottlenecks.
- The first Flink job should not use processing time for business metrics because delayed events would be assigned to the wrong time window.
- Processing-time metrics may be added later for observability.

### Event Time vs Processing Time

- Event time answers: "When did the transaction happen?"
- Processing time answers: "When did Flink handle the transaction?"
- A delayed transaction should still be counted in the window matching its `event_time`.
- The first Flink job should use event time for windowed transaction metrics.

### Watermarks

- A watermark represents Flink's progress through event time.
- It tells Flink that events older than the watermark are unlikely to arrive.
- Watermarks allow event-time windows to close even when events do not arrive perfectly in order.
- Chosen watermark tolerance for this project: 30 seconds
- This tolerance was chosen because the current producer and Kafka broker run locally, so large delays are not expected, but 30 seconds is useful for learning out-of-order event handling.

### Late Events

- An event is late when it arrives after the watermark has passed the end of the window the event belongs to.
- For the first Flink job, late events should not update the main aggregation after the window has closed.
- Chosen late-event policy: drop late events from the main output, but count or log them for visibility.
- Future improvement: route late events to a side output or a dedicated error/audit topic.

### Allowed Lateness

- Allowed lateness is extra time Flink keeps a window available after the watermark has passed the window end.
- Watermark tolerance controls how conservatively event time advances.
- Allowed lateness controls whether already-closed windows can still be updated by late events.
- Chosen allowed lateness for the first Flink job: 0 seconds.
- This is acceptable for the first version because the local producer should not generate heavily delayed events, and a simple policy makes the first job easier to reason about.

### Windows

- A window groups events by time so Flink can calculate metrics over a bounded interval.
- Tumbling windows are fixed-size, non-overlapping windows.
- Sliding windows are fixed-size windows that overlap.
- Session windows group events separated by periods of inactivity.
- Chosen window type for the first Flink job: tumbling event-time window.
- Chosen window duration: 1 minute.
- This 1-minute window is intentionally short so the first local Flink job produces visible results quickly.
- The 1-minute window is not the final fraud detection horizon because real customers may not transact many times within one minute.
- Later fraud detection should compare short-term behaviour against longer customer history, such as 1-day, 7-day, or 30-day baselines.

### Keying

- `keyBy` groups related events so state and window calculations are scoped to each key.
- Chosen key for the first Flink job: `customer_id`.
- This matches the Kafka producer key, which also uses `customer_id`.
- Kafka preserves ordering within a partition, and Flink keying lets the job calculate customer-level metrics consistently.

## First Flink Job Contract

Use this section to define exactly what the first Flink job should do before implementation.

### Input

- Input topic: `transactions_raw`
- Input format: JSON transaction events
- Required fields: `transaction_id`, `customer_id`, `account_id`, `merchant_id`, `merchant_category`, `amount`, `currency`, `country`, `channel`, `status`, `event_time`
- Event-time field: `event_time`
- Kafka consumer group ID: `flink-transactions-processor`

### Processing

- Key: `customer_id`
- Window type: tumbling event-time window
- Window duration: 1 minute
- Window purpose: first-job validation and fast local feedback, not final fraud scoring
- Watermark tolerance: 30 seconds
- Allowed lateness: 0 seconds
- Late-event policy: do not update the main aggregation; count or log late events
- Aggregations:
  - transaction count
  - total transaction amount
  - average transaction amount
  - failed transaction count

### Output

- Output topic: `transactions_processed`
- Output format: JSON
- Output grain: per customer per one-minute window
- Output fields: `customer_id`, `window_start`, `window_end`, `transaction_count`, `total_amount`, `average_amount`, `failed_transaction_count`

### Example Output Event

```json
{
  "customer_id": "CUST00005784",
  "window_start": "2026-07-15T09:53:00Z",
  "window_end": "2026-07-15T09:54:00Z",
  "transaction_count": 4,
  "total_amount": 1234.56,
  "average_amount": 308.64,
  "failed_transaction_count": 1
}
```

## Checkpointing

- Checkpointing lets Flink periodically save processing progress and state.
- For Kafka sources, checkpoints help Flink recover from the correct Kafka offsets after a restart.
- For stateful jobs, checkpoints also preserve keyed state such as customer-level rolling metrics.
- The first Flink job should target reliable recovery from Kafka with checkpointing enabled.
- End-to-end exactly-once processing will require compatible Kafka source and sink configuration in addition to checkpoints.

## Customer History And Fraud Context

- The first Flink job only calculates simple per-window transaction metrics.
- Realistic fraud detection needs historical customer context in addition to short windows.
- Future customer profile state may include usual countries, usual channels, usual merchant categories, average transaction amount, daily average spend, weekly average spend, failed transaction rate, and previous transaction time.
- Short windows are useful for velocity checks, such as rapid repeated transactions or repeated failures.
- Longer windows and historical profiles are useful for anomaly checks, such as spend that is unusually high compared with the customer's normal behaviour.
- RocksDB will later be used to maintain customer-level state for these profiles.

## Backpressure

- Backpressure happens when downstream processing cannot keep up with incoming records.
- In this project, backpressure may appear if the Flink job processes slower than the Python producer writes to Kafka.
- Kafka will retain the backlog while consumer lag grows.
- Consumer lag and Flink throughput should be observed later when the Flink job is running.

## Failure And Recovery

- If the Flink job restarts, it should resume from checkpointed Kafka offsets when checkpoints are available.
- Without checkpoints, the job may resume based on committed Kafka offsets or the configured offset reset policy.
- For the first version, the acceptable recovery target is to avoid losing Kafka input records and to make replay possible during development.

## Implementation Notes For Later

- Java package/module location: `flink-jobs`
- Flink version: 2.2.1
- Primary API: Java DataStream API
- Kafka connector version: use the Kafka connector compatible with Flink 2.2.x
- Kafka source connector needed: yes, for `transactions_raw`
- Kafka sink connector needed: yes, for `transactions_processed`
- JSON serialization/deserialization approach:
- Local Docker Compose requirements:
- Tests or verification commands:


## Future Enhancements

- Checkpointing
- Savepoints
- Exactly-once processing
- Event-time watermarks
- Schema Registry integration
