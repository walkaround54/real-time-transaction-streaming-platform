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
| Processing | Apache Flink 2.2.1, Java DataStream API first, Flink SQL later |
| State | RocksDB |
| Containers | Docker |
| Orchestration | Kubernetes |
| Monitoring | Prometheus, Grafana |

## Documentation

- `STATUS.md` - Current project status, active phase, blockers, and the live auto-generated project tree
- `PROJECT_CONTEXT.md` - Project purpose, learning philosophy, architecture overview, and completed/upcoming milestones
- `AGENTS.md` - Working conventions for AI coding agents and documentation update rules
- `CONTRIBUTING.md` - Development workflow
- `VERSIONING.md` - Release strategy
- `CHANGELOG.md` - Release history
- `docs/` - Architecture and implementation guides

If you want the latest project snapshot, start with `STATUS.md`. If you want the broader narrative and design direction, read `PROJECT_CONTEXT.md`.

## Roadmap

1. Python Producer
2. Docker
3. Kafka
4. Flink
5. RocksDB
6. Fraud Engine
7. Observability
8. Kubernetes
