# Changelog

All notable changes to this project will be documented in this file.

The changelog is append-only. New releases or meaningful milestones should be added as new entries without rewriting prior history.

## [v0.4.0] - 2026-07-16

### Added

- Documented Kafka-side streaming concepts for consumer groups, offsets, replay, producer guarantees and lag.
- Documented Flink-side streaming concepts for event time, processing time, watermarks, windows, late events, checkpointing and backpressure.
- Defined the first Flink processing contract for the upcoming `v0.5.0` job: read `transactions_raw`, key by `customer_id`, apply a one-minute validation window and write to `transactions_processed`.
- Added fraud-engine planning notes for customer historical profiles, longer baselines and explicit anomalous transaction generation.

### Verified

- Practised Kafka consumer groups, committed offsets and replay using Kafka CLI tools against `transactions_raw`.
- Confirmed producer unit tests pass after Kafka publisher callback test updates.

## [v0.3.0] - 2026-07-13

### Added

- Wired the Python producer to Kafka using `confluent-kafka`.
- Published simulated transaction events to `transactions_raw` with customer-based message keys.
- Added unit tests for the Kafka publisher wrapper and the generator publish flow.

### Verified

- Confirmed the producer container runs on the shared Compose network and can reach the Kafka broker.
- Confirmed messages are readable from `transactions_raw` with a Kafka console consumer.

## [v0.2.0] - 2026-07-09

### Added

- Dockerized the Python transaction producer into a runtime image.
- Verified the producer container runs successfully with `docker run`.
- Kept the runtime image focused on application code and runtime dependencies only.

## [v0.1.0] - 2026-07-06

### Added

- Python transaction generator with realistic customer, merchant, and currency simulation.
- Pydantic transaction model with structured logging and unit tests.
