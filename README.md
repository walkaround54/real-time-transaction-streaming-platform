# Enterprise Real-Time Transaction Streaming Platform

> An enterprise-grade learning project that simulates financial transactions, streams them through Apache Kafka, processes them with Apache Flink, detects fraud using stateful processing, and deploys using Docker and Kubernetes.

## Features

- Real-time transaction simulator (Python)
- Apache Kafka event streaming
- Apache Flink (Java + SQL)
- RocksDB stateful processing
- Fraud detection engine
- Prometheus & Grafana observability
- Docker Compose local environment
- Kubernetes + Helm deployment

## Technology Stack

| Area | Technology |
|------|------------|
| Producer | Python |
| Streaming | Apache Kafka |
| Processing | Apache Flink |
| State | RocksDB |
| Containers | Docker |
| Orchestration | Kubernetes |
| Monitoring | Prometheus, Grafana |

## Repository Structure

```text
README.md
CONTRIBUTING.md
VERSIONING.md
CHANGELOG.md
AGENTS.md
docs/
producer/
flink-jobs/
kafka/
docker-compose/
kubernetes/
observability/
```

## Documentation

- CONTRIBUTING.md – Development workflow
- VERSIONING.md – Release strategy
- CHANGELOG.md – Release history
- AGENTS.md – Instructions for AI coding agents
- docs/ – Architecture and implementation guides

## Roadmap

1. Python Producer
2. Docker
3. Kafka
4. Flink
5. RocksDB
6. Fraud Engine
7. Observability
8. Kubernetes

See the `docs/` folder for detailed design and implementation guides.