# Technologies

## Main Technology Stack

| Area | Technology | Purpose |
|------|------------|---------|
| Programming | Python | Simulate transaction events |
| Programming | Java | Build production-style Flink streaming jobs |
| Containerisation | Docker | Package applications |
| Local Orchestration | Docker Compose | Run the platform locally before Kubernetes |
| Messaging | Apache Kafka | Ingest and buffer transaction events |
| Stream Processing | Apache Flink Java | Fraud detection and stateful business logic |
| Stream Processing | Flink SQL | Real-time analytics and KPI aggregations |
| State Management | RocksDB | Store Flink state locally and efficiently |
| Observability | Prometheus | Collect metrics |
| Dashboarding | Grafana | Visualise system and business metrics |
| Deployment | Kubernetes | Run services in a production-like environment |
| Package Management | Helm | Deploy Kubernetes applications |
| Kafka Operator | Strimzi | Manage Kafka on Kubernetes |
| Flink Operator | Flink Kubernetes Operator | Manage Flink jobs on Kubernetes |

## Python

Python is used to build the transaction generator.

The generator should create realistic JSON transaction events with fields such as:

- transaction_id
- customer_id
- account_id
- merchant_id
- merchant_category
- amount
- currency
- country
- channel
- status
- event_time

The producer should eventually send these events to Kafka.

## Docker

Docker is used to package applications and supporting services.

Use Docker for:

- Python transaction producer
- Flink jobs
- Local development services
- Repeatable runtime environments

## Docker Compose

Docker Compose is used before Kubernetes to run the full local platform.

Expected services:

- Kafka
- Kafka UI
- Flink JobManager
- Flink TaskManager
- Python transaction producer
- Prometheus
- Grafana

## Apache Kafka

Kafka is the messaging backbone.

It provides:

- Event ingestion
- Buffering
- Replay
- Topic-based decoupling
- Producer and consumer patterns
- Consumer groups
- Partitioning
- Offset management
- Retention

## Apache Flink Java

Flink Java is used for production-style stream processing.

Use it for:

- DataStream processing
- Stateful fraud detection
- Event-time processing
- Windows
- Checkpointing
- Side outputs
- Kafka source and sink integration

## Flink SQL

Flink SQL is used for simpler analytics and reporting-style streaming queries.

Use it for:

- Transaction volume per minute
- Total transaction amount per minute
- Average transaction size
- Top merchant categories
- Failed transaction rate
- Alert count per minute

## RocksDB

RocksDB is used as the Flink state backend for fraud detection logic that needs memory across events.

Example state:

- Rolling customer spend
- Customer transaction count
- Failed transaction count
- Previous transaction country
- Last transaction timestamp
- Historical average transaction amount

## Prometheus

Prometheus collects time-series metrics from platform components.

Monitor:

- Kafka metrics
- Flink metrics
- Kubernetes metrics
- Producer application metrics

## Grafana

Grafana visualises platform and business metrics.

Dashboards should include:

- Kafka consumer lag
- Flink throughput
- Flink latency
- Checkpoint duration
- Failed checkpoints
- CPU and memory
- Fraud alert count
- Transaction volume

## Kubernetes

Kubernetes is used for production-style deployment.

Key concepts:

- Pod
- Deployment
- Service
- ConfigMap
- Secret
- Namespace
- PersistentVolume
- PersistentVolumeClaim

## Helm

Helm is used to install and manage Kubernetes applications.

Use Helm for:

- Prometheus
- Grafana
- Kafka operator
- Flink operator

## Strimzi

Strimzi is used to deploy and manage Kafka on Kubernetes.

Learn:

- Kafka custom resource
- KafkaTopic custom resource
- KafkaUser custom resource

## Flink Kubernetes Operator

The Flink Kubernetes Operator is used to manage Flink jobs on Kubernetes.

Learn:

- FlinkDeployment
- JobManager specification
- TaskManager specification
- Savepoints
- Job upgrades