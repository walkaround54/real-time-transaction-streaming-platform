# Architecture

## Overview

The Enterprise Real-Time Transaction Streaming Platform is designed to simulate how banks, fintechs, payment companies, and large technology companies build real-time streaming systems.

The platform generates financial transaction events, streams them through Kafka, processes them with Flink, stores state using RocksDB, emits processed events and alerts back to Kafka, and exposes operational metrics through Prometheus and Grafana.

## Final Architecture

```mermaid
flowchart TD

    Dev[Developer<br/>Git / Local Code / Java / Python / Dockerfiles]

    Docker[Docker<br/>Containerise applications<br/>Python Producer<br/>Flink Java Job<br/>Supporting services]

    subgraph K8s[Kubernetes Cluster]

        Producer[Python Transaction Generator Pod<br/>Simulates live transaction events]

        KafkaRaw[Apache Kafka<br/>transactions_raw topic<br/>Event ingestion, buffering, replay]

        subgraph Flink[Apache Flink Cluster<br/>JobManager + TaskManagers]
            FlinkJava[Flink Java Jobs<br/>Fraud rules<br/>Stateful processing<br/>Event-time windows<br/>Alerts]
            FlinkSQL[Flink SQL Jobs<br/>Simple aggregations<br/>KPI metrics]
        end

        RocksDB[RocksDB State Backend<br/>Customer running spend<br/>Transaction count<br/>Failed transaction count<br/>Previous event history]

        Alerts[Kafka Topic<br/>transactions_alerts<br/>Fraud alerts]
        KPI[Kafka Topic<br/>transactions_kpi<br/>Dashboard metrics]
        Error[Kafka Topic<br/>transactions_error<br/>Invalid or malformed records]
        Processed[Kafka Topic<br/>transactions_processed<br/>Cleaned and enriched transactions]

        Metrics[Metrics Endpoints<br/>Kafka metrics<br/>Flink metrics<br/>Kubernetes metrics<br/>Producer metrics]

        Prometheus[Prometheus<br/>Scrapes and stores time-series metrics]

        Grafana[Grafana<br/>Dashboards for Kafka, Flink, Kubernetes and business KPIs]
    end

    Dev --> Docker
    Docker --> Producer
    Producer --> KafkaRaw
    KafkaRaw --> FlinkJava
    KafkaRaw --> FlinkSQL
    FlinkJava --> RocksDB
    RocksDB --> FlinkJava
    FlinkJava --> Processed
    FlinkJava --> Alerts
    FlinkJava --> Error
    FlinkSQL --> KPI
    Metrics --> Prometheus
    Prometheus --> Grafana
```

## Architecture Summary

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

## Component Responsibilities

| Component | Responsibility |
|----------|----------------|
| Python Producer | Generate realistic simulated financial transaction events |
| Docker | Package applications and supporting services |
| Kafka | Ingest, buffer, retain and replay transaction events |
| Flink Java | Perform production-style stateful stream processing and fraud detection |
| Flink SQL | Produce simple real-time analytics and KPI aggregations |
| RocksDB | Store local state for customer-level fraud rules |
| Prometheus | Collect operational and application metrics |
| Grafana | Visualise infrastructure and business metrics |
| Docker Compose | Run the full platform locally |
| Kubernetes | Run the platform in a production-like environment |
| Helm | Install and manage Kubernetes applications |
| Strimzi | Manage Kafka on Kubernetes |
| Flink Kubernetes Operator | Manage Flink jobs on Kubernetes |

## Data Flow

```mermaid
flowchart LR

    A[Transaction Event] --> B[Python Producer]
    B --> C[Kafka: transactions_raw]
    C --> D[Flink Validation]
    D --> E[transactions_processed]
    D --> F[transactions_error]
    C --> G[Flink Fraud Engine]
    G --> H[RocksDB State]
    H --> G
    G --> I[transactions_alerts]
    C --> J[Flink SQL]
    J --> K[transactions_kpi]
```

## Local Architecture

The local environment will use Docker Compose.

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

## Kubernetes Architecture

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

## Operator-Based Architecture

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

## Design Principles

- Build incrementally.
- Introduce each technology only when needed.
- Prefer working systems over isolated learning.
- Keep each phase testable.
- Preserve replayability through Kafka.
- Use stateful processing only where business logic requires memory.
- Observe both system metrics and business metrics.