# Project Context

## Project

**Enterprise Real-Time Transaction Streaming Platform**

A hands-on data engineering project that incrementally builds a production-style real-time transaction streaming platform using Python, Apache Kafka, Apache Flink, Docker, Kubernetes, Prometheus and Grafana.

The objective is to learn modern data engineering by designing, implementing and operating a realistic event-driven system using production software engineering practices.

---

## Learning Philosophy

This project is intentionally educational.

The primary objective is understanding modern data engineering practices rather than completing features quickly.

When introducing new technologies:

- Build concepts incrementally.
- Encourage reasoning before implementation.
- Prefer questions over direct answers.
- Review and improve user-written code.
- Explain why production engineers make certain design decisions.
- Avoid providing full solutions before the user has attempted the task.

Treat each phase as a learning milestone rather than a coding exercise.

# Current Project Status

Current Version

v0.3.0

Current Milestone

Phase 4 - Apache Kafka cluster

Current Feature

Kafka publishing from the Python producer into `transactions_raw` has been implemented and verified locally

---

# Project Philosophy

Build the platform incrementally.

```text
Build simple
        ->
Generate realistic data
        ->
Containerise
        ->
Stream events
        ->
Process events
        ->
Maintain state
        ->
Detect fraud
        ->
Observe the platform
        ->
Deploy like production
```

Guiding principles:

- Build one feature at a time.
- Avoid premature optimisation.
- Prefer production-quality engineering over quick prototypes.
- Introduce new technologies only when they naturally fit the roadmap.
- Keep code simple, readable and testable.
- Keep responsibilities separated.

---

# Engineering Standards

Development workflow

- GitHub Flow
- Feature branches (`feature/<name>`)
- Pull Request before merging into `main`
- Squash merge
- Conventional Commits
- Semantic Versioning

Documentation

Whenever architecture or behaviour changes:

- Update PROJECT_CONTEXT.md
- Update STATUS.md
- Update CHANGELOG.md

---

# Current Architecture

```text
Transaction Generator
        |
        v
Transaction Factory
        |
        v
Transaction Model
        |
        v
Kafka Producer
        |
        v
Kafka Topic (`transactions_raw`)
```

Current application consists of a single Python producer that continuously generates realistic financial transaction events and publishes them to Kafka.

The producer is packaged using a standard Python src layout and a verified Docker runtime image:

```text
producer/
├── pyproject.toml
├── Dockerfile
├── src/
│   └── producer/
│       ├── __init__.py
│       ├── generator.py
│       ├── logging_config.py
│       ├── models.py
│       ├── settings.py
│       └── transaction_factory.py
└── tests/
    ├── test_generator.py
    └── test_transaction_factory.py
```

The runtime Docker image contains only the producer application code and its runtime dependencies, not the test suite.

Kafka is now available locally through Docker Compose in KRaft mode, with a one-shot topic setup service that creates `transactions_raw` during startup. The Python producer has been verified against this broker and topic setup using a Kafka console consumer.

---

Refer to STATUS.md for existing Project Tree structure.

---

# Completed Features

Repository

- Repository structure
- Git workflow
- Documentation
- Versioning conventions

Producer

- Pydantic transaction model
- Transaction factory
- Continuous transaction generator
- Merchant reference dataset
- Merchant-specific transaction amount bands
- Customer/account relationship
- Sequential transaction IDs
- Country-to-currency mapping
- Currency conversion
- Application settings
- Structured logging
- Unit tests
- Kafka publishing to `transactions_raw`
- Local delivery verification with a Kafka console consumer

Packaging / Build

- pyproject.toml-based Python packaging
- Runtime-only Docker approach for the producer
- Service-local build context convention
- Dockerized producer image verified with `docker run`
- Kafka broker running successfully in KRaft mode
- Topic provisioning for `transactions_raw` verified via Compose startup
- Producer container verified on the shared Compose network

---

# Current Producer Design

Transaction Generation

- Generates transactions continuously.
- Transaction IDs are sequential.
- Format: `TX00000001`

Customer

- Simulated population of 10,000 customers.
- One customer owns one account.

Merchant

- Merchant dataclass.
- 27 realistic merchants.
- Merchant category remains consistent.
- Merchant amount ranges stored in SGD.

Currency

- SGD is the base currency.
- Local transaction amount derived using configurable currency multipliers.

Configuration

- Generator settings centralised in `settings.py`.

Logging

- Python logging module.
- Structured console logging.
- Module-specific loggers.
- Kafka publish logging for generated transactions

Testing

- Pytest.
- Factory and generator unit tests.
- Kafka publisher wrapper unit tests

Packaging

- pyproject.toml is the source of truth for producer packaging metadata and dependencies.
- The package follows a src layout.
- Imports should use the package name, for example producer.generator.

---

# Upcoming Milestones

Phase 3

- Kafka Producer

Phase 4

- Apache Kafka cluster

Phase 5

- Apache Flink

Phase 6

- Stateful stream processing with RocksDB

Phase 7

- Fraud detection

Phase 8

- Observability

- Prometheus
- Grafana

Phase 9

- Kubernetes deployment

---

# Guidance for Future AI Assistants

Assume the current architecture unless there is a compelling engineering reason to change it.

Priorities

1. Keep the code simple.
2. Build one feature at a time.
3. Maintain realistic transaction behaviour.
4. Preserve separation of concerns.
5. Prefer production-quality code over quick prototypes.
6. Avoid redesigning completed components unless explicitly requested.
7. Follow the existing project roadmap.
8. Prefer incremental improvements over large refactors.

When chat memory becomes full, be prepared to regenerate:

- PROJECT_CONTEXT.md
- STATUS.md
- CHANGELOG.md

to allow the project to continue in a new conversation with minimal loss of context.
