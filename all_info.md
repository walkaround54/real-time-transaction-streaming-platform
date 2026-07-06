# Enterprise Real-Time Transaction Streaming Platform

## 1. Project Overview

### Objective

Build an enterprise-grade real-time transaction streaming platform that simulates financial transaction events, processes them in real time, detects suspicious behaviour, and exposes operational and processing metrics through a complete observability stack.

The project is designed to mirror how banks, fintechs, payment companies, and large technology companies build real-time streaming systems.

The focus is to learn by building.

---

## 2. Final Architecture

```text
                                    ┌──────────────────────────────┐
                                    │          Developer            │
                                    │ Git / Local Code / Java /     │
                                    │ Python / Dockerfiles          │
                                    └───────────────┬──────────────┘
                                                    │
                                                    ▼
                                    ┌──────────────────────────────┐
                                    │            Docker             │
                                    │ Containerise applications     │
                                    │ - Python Producer             │
                                    │ - Flink Java Job              │
                                    │ - Supporting services         │
                                    └───────────────┬──────────────┘
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                                Kubernetes Cluster                                   │
│                                                                                     │
│   ┌──────────────────────┐        ┌────────────────────────┐                       │
│   │ Python Transaction   │        │ Apache Kafka            │                       │
│   │ Generator Pod        │───────▶│ transactions_raw topic  │                       │
│   │                      │        │                        │                       │
│   │ Simulates live       │        │ Event ingestion, queue, │                       │
│   │ transaction events   │        │ buffering, replay       │                       │
│   └──────────────────────┘        └───────────┬────────────┘                       │
│                                                │                                    │
│                                                ▼                                    │
│                              ┌────────────────────────────────┐                    │
│                              │ Apache Flink Cluster            │                    │
│                              │ JobManager + TaskManagers       │                    │
│                              │                                │                    │
│                              │ Flink Java Jobs                 │                    │
│                              │ - Fraud rules                   │                    │
│                              │ - Stateful processing           │                    │
│                              │ - Event-time windows            │                    │
│                              │ - Alerts                        │                    │
│                              │                                │                    │
│                              │ Flink SQL Jobs                  │                    │
│                              │ - Simple aggregations           │                    │
│                              │ - KPI metrics                   │                    │
│                              └───────────────┬────────────────┘                    │
│                                              │                                     │
│                                              ▼                                     │
│                              ┌────────────────────────────────┐                    │
│                              │ RocksDB State Backend           │                    │
│                              │                                │                    │
│                              │ Stores Flink local state:       │                    │
│                              │ - Customer running spend        │                    │
│                              │ - Transaction count             │                    │
│                              │ - Failed transaction count      │                    │
│                              │ - Previous event history        │                    │
│                              └───────────────┬────────────────┘                    │
│                                              │                                     │
│                                              ▼                                     │
│        ┌──────────────────────────────┬──────────────────────────────┐             │
│        │                              │                              │             │
│        ▼                              ▼                              ▼             │
│ ┌───────────────────┐        ┌───────────────────┐        ┌───────────────────┐   │
│ │ Kafka Topic        │        │ Kafka Topic        │        │ Kafka Topic        │   │
│ │ transactions_alerts│        │ transactions_kpi   │        │ transactions_error │   │
│ │                   │        │                   │        │                   │   │
│ │ Fraud alerts       │        │ Dashboard metrics  │        │ Bad / invalid data │   │
│ └───────────────────┘        └───────────────────┘        └───────────────────┘   │
│                                                                                     │
│ ┌──────────────────────────────┐       ┌──────────────────────────────────────┐    │
│ │ Prometheus                   │◀──────│ Metrics Endpoints                    │    │
│ │                              │       │ - Kafka metrics                      │    │
│ │ Scrapes platform metrics     │       │ - Flink metrics                      │    │
│ │ and stores time-series data  │       │ - Kubernetes metrics                 │    │
│ └───────────────┬──────────────┘       │ - Producer application metrics       │    │
│                 │                      └──────────────────────────────────────┘    │
│                 ▼                                                                   │
│ ┌──────────────────────────────┐                                                   │
│ │ Grafana                      │                                                   │
│ │                              │                                                   │
│ │ Dashboards for:              │                                                   │
│ │ - Kafka consumer lag         │                                                   │
│ │ - Flink throughput           │                                                   │
│ │ - Flink latency              │                                                   │
│ │ - Checkpoint duration        │                                                   │
│ │ - Failed checkpoints         │                                                   │
│ │ - CPU and memory             │                                                   │
│ │ - Fraud alert count          │                                                   │
│ └──────────────────────────────┘                                                   │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Architecture Summary

```text
Python Transaction Generator
        ↓
Docker Container
        ↓
Kubernetes Pod
        ↓
Kafka Topic: transactions_raw
        ↓
Flink Java / Flink SQL
        ↓
RocksDB State Backend
        ↓
Kafka Output Topics
        ↓
Prometheus Metrics
        ↓
Grafana Dashboard
```

---

## 4. Main Technologies Used

| Area                | Technology                | Purpose                                         |
| ------------------- | ------------------------- | ----------------------------------------------- |
| Programming         | Python                    | Simulate transaction events                     |
| Programming         | Java                      | Build production-style Flink streaming jobs     |
| Containerisation    | Docker                    | Package applications                            |
| Local orchestration | Docker Compose            | Run the platform locally before Kubernetes      |
| Messaging           | Apache Kafka              | Ingest and buffer transaction events            |
| Stream processing   | Apache Flink Java         | Fraud detection and stateful business logic     |
| Stream processing   | Flink SQL                 | Simple real-time analytics and KPI aggregations |
| State management    | RocksDB                   | Store Flink state locally and efficiently       |
| Observability       | Prometheus                | Collect metrics                                 |
| Dashboarding        | Grafana                   | Visualise system and business metrics           |
| Deployment          | Kubernetes                | Run services in a production-like environment   |
| Package management  | Helm                      | Deploy Kubernetes applications                  |
| Kafka operator      | Strimzi                   | Manage Kafka on Kubernetes                      |
| Flink operator      | Flink Kubernetes Operator | Manage Flink jobs on Kubernetes                 |

---

## 5. Learning Philosophy

This project should be built incrementally.

Do not learn every tool separately before starting.

Instead, introduce each technology only when the project needs it.

The learning path is:

```text
Build simple
        ↓
Make it stream
        ↓
Process events
        ↓
Add state
        ↓
Detect fraud
        ↓
Monitor it
        ↓
Containerise it
        ↓
Deploy it like production
```

---

## 6. Phase 1 — Simulate Financial Transactions

### Goal

Create a realistic financial transaction simulator.

### Learn

* Python
* Faker
* JSON
* Basic Docker

### Build

Create a Python script that continuously generates simulated transaction events.

Example transaction event:

```json
{
  "transaction_id": "TX100001",
  "customer_id": "CUST001",
  "account_id": "ACC001",
  "merchant_id": "MRC001",
  "merchant_category": "Electronics",
  "amount": 350.50,
  "currency": "SGD",
  "country": "SG",
  "channel": "Online",
  "status": "SUCCESS",
  "event_time": "2026-07-06T10:20:15"
}
```

### Transaction Scenarios to Simulate

* Normal retail transaction
* High-value transaction
* Repeated failed transactions
* Multiple countries for same customer
* Multiple transactions within 60 seconds
* Sudden spending spike
* Suspicious merchant category

### Output

```text
Python Script
        ↓
Generated JSON transaction events
```

---

## 7. Phase 2 — Containerise the Transaction Generator

### Goal

Package the Python transaction generator using Docker.

### Learn

* Dockerfile
* Docker image
* Docker container
* Environment variables
* Container logs

### Build

Create a Docker image for the Python producer.

Example flow:

```text
Python Code
        ↓
Dockerfile
        ↓
Docker Image
        ↓
Running Container
```

### Output

A container that continuously generates transaction events.

---

## 8. Phase 3 — Build the Messaging Layer with Kafka

### Goal

Send simulated transactions into Kafka.

### Learn

* Kafka broker
* Topic
* Producer
* Consumer
* Consumer group
* Partition
* Offset
* Retention
* Replay

### Build

Create Kafka topic:

```text
transactions_raw
```

The flow becomes:

```text
Python Transaction Producer
        ↓
Kafka Topic: transactions_raw
        ↓
Test Consumer
```

### Skills Learned

* Event streaming
* Producer / consumer pattern
* Distributed messaging
* Kafka topic design

---

## 9. Phase 4 — Learn Streaming Concepts

Before building Flink jobs, understand the main streaming concepts.

### Learn

* Event time
* Processing time
* Watermarks
* Tumbling windows
* Sliding windows
* Session windows
* Late events
* Checkpointing
* Exactly-once processing
* Backpressure

These concepts are more important than the syntax of any single framework.

---

## 10. Phase 5 — Real-Time Processing with Flink Java

### Goal

Build the core stream processing engine.

### Learn

* Flink DataStream API
* Source
* Sink
* Map
* Filter
* KeyBy
* Window
* ProcessFunction
* KeyedProcessFunction
* Side outputs

### Build

Create a Flink Java job that reads from:

```text
transactions_raw
```

Calculate:

* Transaction count
* Total transaction amount
* Average transaction amount
* Failed transaction count

Write output to:

```text
transactions_processed
```

### Flow

```text
Kafka: transactions_raw
        ↓
Flink Java Job
        ↓
Kafka: transactions_processed
```

---

## 11. Phase 6 — Stateful Processing with RocksDB

### Goal

Use RocksDB to support stateful fraud detection.

### Why RocksDB Is Needed

Fraud detection requires memory across multiple events.

For example:

* How much has this customer spent in the last 5 minutes?
* How many failed transactions happened in the last 60 seconds?
* Did this customer transact in two different countries within a short period?
* Is this transaction much higher than the customer's usual amount?

Flink stores this kind of state using a state backend. RocksDB is commonly used when the state is too large to keep fully in memory.

### Learn

* Keyed state
* ValueState
* ListState
* MapState
* State TTL
* RocksDB state backend
* Checkpointing
* Recovery

### Build

Implement:

* Rolling 5-minute customer spend
* Transaction count per customer
* Failed transaction count
* Previous transaction country
* Last transaction timestamp

### Flow

```text
Kafka Event
        ↓
Flink Java Operator
        ↓
Read / Write Customer State
        ↓
RocksDB
        ↓
Fraud Rule Decision
```

---

## 12. Phase 7 — Fraud Detection Engine

### Goal

Implement real-time fraud detection rules.

### Fraud Rules

Create alerts when:

1. Customer spends more than SGD 10,000 within 5 minutes.
2. Customer makes more than 5 transactions within 60 seconds.
3. Customer has more than 3 failed transactions within 5 minutes.
4. Customer transacts from two countries within a short time.
5. Transaction amount is significantly higher than the customer's historical average.

### Output Topic

```text
transactions_alerts
```

### Alert Event Example

```json
{
  "alert_id": "ALERT100001",
  "customer_id": "CUST001",
  "transaction_id": "TX100001",
  "alert_type": "HIGH_VELOCITY_SPEND",
  "severity": "HIGH",
  "description": "Customer spent more than SGD 10,000 within 5 minutes",
  "event_time": "2026-07-06T10:25:15"
}
```

### Flow

```text
transactions_raw
        ↓
Flink Java Fraud Engine
        ↓
RocksDB State
        ↓
transactions_alerts
```

---

## 13. Phase 8 — Real-Time Analytics with Flink SQL

### Goal

Use Flink SQL for simple real-time reporting metrics.

### Learn

* Create table
* Kafka connector
* Window aggregation
* TUMBLE
* HOP
* GROUP BY
* Streaming SQL joins

### Build

Calculate:

* Transaction volume per minute
* Total transaction amount per minute
* Average transaction size
* Top merchant categories
* Failed transaction rate
* Alert count per minute

### Output Topic

```text
transactions_kpi
```

### Flow

```text
transactions_raw
        ↓
Flink SQL
        ↓
transactions_kpi
```

---

## 14. Phase 9 — Add Dead Letter Queue

### Goal

Handle invalid or malformed transaction events.

### Learn

* Data validation
* Error handling
* Bad record routing
* Dead Letter Queue

### Build

Create error topic:

```text
transactions_error
```

Events should be routed here if:

* Required fields are missing
* Amount is invalid
* Currency is missing
* Event time cannot be parsed
* JSON structure is invalid

### Flow

```text
transactions_raw
        ↓
Flink Validation Logic
        ↓
Valid Events → transactions_processed
Invalid Events → transactions_error
```

---

## 15. Phase 10 — Observability with Prometheus and Grafana

### Goal

Monitor both the platform and the business events.

### Learn Prometheus

* Metrics
* Scraping
* Targets
* Exporters
* Time-series data

### Learn Grafana

* Dashboard
* Panel
* Query
* Alert
* Time range

### Monitor Kafka

* Broker availability
* Topic throughput
* Consumer lag
* Under-replicated partitions

### Monitor Flink

* Records in per second
* Records out per second
* Processing latency
* Checkpoint duration
* Failed checkpoints
* Backpressure
* TaskManager CPU
* TaskManager memory

### Monitor Business Metrics

* Transactions per minute
* Total transaction amount
* Failed transaction count
* Fraud alert count
* Alerts by severity
* Alerts by rule type

### Flow

```text
Kafka / Flink / Kubernetes Metrics
        ↓
Prometheus
        ↓
Grafana Dashboard
```

---

## 16. Phase 11 — Run Everything Locally with Docker Compose

### Goal

Run the full system locally before moving to Kubernetes.

### Learn

* Docker Compose
* Service networking
* Container dependencies
* Volumes
* Ports
* Environment variables

### Docker Compose Services

* Kafka
* Kafka UI
* Flink JobManager
* Flink TaskManager
* Python transaction producer
* Prometheus
* Grafana

### Local Architecture

```text
Docker Compose

├── Kafka
├── Kafka UI
├── Flink JobManager
├── Flink TaskManager
├── Python Producer
├── Prometheus
└── Grafana
```

---

## 17. Phase 12 — Deploy to Kubernetes

### Goal

Move from local Docker Compose to a production-style Kubernetes deployment.

### Learn

* Pod
* Deployment
* Service
* ConfigMap
* Secret
* Namespace
* PersistentVolume
* PersistentVolumeClaim

### Deploy

* Python producer pod
* Kafka cluster
* Flink cluster
* Prometheus
* Grafana

### Kubernetes Architecture

```text
Kubernetes Cluster

├── Namespace: streaming
│   ├── Python Producer Deployment
│   ├── Kafka Cluster
│   ├── Flink JobManager
│   ├── Flink TaskManagers
│   └── Kafka Topics
│
└── Namespace: monitoring
    ├── Prometheus
    └── Grafana
```

---

## 18. Phase 13 — Deploy with Helm

### Goal

Use Helm to install and manage Kubernetes applications.

### Learn

* Helm chart
* Helm values
* Helm release
* Upgrade
* Rollback

### Use Helm For

* Prometheus
* Grafana
* Kafka operator
* Flink operator

---

## 19. Phase 14 — Use Kubernetes Operators

### Goal

Manage Kafka and Flink using Kubernetes-native operators.

### Strimzi

Use Strimzi to deploy and manage Kafka.

Learn:

* Kafka custom resource
* KafkaTopic custom resource
* KafkaUser custom resource

### Flink Kubernetes Operator

Use the Flink Kubernetes Operator to deploy and manage Flink jobs.

Learn:

* FlinkDeployment
* JobManager specification
* TaskManager specification
* Savepoints
* Job upgrades

### Operator-Based Architecture

```text
Kubernetes

├── Strimzi Operator
│   └── Kafka Cluster
│       ├── transactions_raw
│       ├── transactions_processed
│       ├── transactions_alerts
│       ├── transactions_kpi
│       └── transactions_error
│
└── Flink Kubernetes Operator
    └── Flink Fraud Detection Job
```

---

## 20. Final Kafka Topics

| Topic                  | Purpose                                     |
| ---------------------- | ------------------------------------------- |
| transactions_raw       | Raw transaction events from Python producer |
| transactions_processed | Cleaned and enriched transactions           |
| transactions_alerts    | Fraud and anomaly alerts                    |
| transactions_kpi       | Aggregated metrics for dashboarding         |
| transactions_error     | Invalid or malformed records                |

---

## 21. Final Project Deliverables

By the end of the project, the system should include:

1. Python transaction generator
2. Dockerised producer
3. Kafka ingestion layer
4. Flink Java fraud detection job
5. RocksDB-backed stateful processing
6. Flink SQL analytics job
7. Kafka alert and KPI topics
8. Dead Letter Queue
9. Prometheus monitoring
10. Grafana dashboard
11. Docker Compose local deployment
12. Kubernetes deployment
13. Helm-based installation
14. Strimzi-managed Kafka
15. Flink Kubernetes Operator deployment

---

## 22. Recommended Learning Order

```text
1. Python transaction generator
2. Docker
3. Kafka producer and consumer
4. Kafka topics, partitions, offsets
5. Streaming concepts
6. Flink Java DataStream API
7. Flink state
8. RocksDB
9. Fraud detection rules
10. Flink SQL
11. Dead Letter Queue
12. Prometheus
13. Grafana
14. Docker Compose
15. Kubernetes
16. Helm
17. Strimzi
18. Flink Kubernetes Operator
```

---

## 23. Stretch Goals

After the core system works, add:

* Schema Registry
* Avro or Protobuf serialization
* OpenTelemetry tracing
* CI/CD with GitHub Actions
* Integration tests
* Replay from Kafka offsets
* Exactly-once end-to-end processing
* Alert notification to email or Microsoft Teams
* Multiple transaction producers
* Load testing
* Chaos testing by killing Flink TaskManagers

---

## 24. Skills Gained

This project will help build skills in:

* Big data engineering
* Real-time stream processing
* Apache Kafka
* Apache Flink Java
* Flink SQL
* Stateful processing
* RocksDB
* Fraud detection logic
* Docker
* Kubernetes
* Helm
* Prometheus
* Grafana
* Production observability
* Event-driven architecture
* Distributed systems
