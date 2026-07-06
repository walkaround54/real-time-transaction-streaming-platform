# Deployment

## Stage 1

Run locally.

Components:

- Python Producer
- Kafka
- Flink
- Prometheus
- Grafana

## Stage 2

Containerise with Docker.

Deliverables:

- Dockerfile (Producer)
- Dockerfile (Flink)
- Docker Compose

## Stage 3

Deploy to Kubernetes.

Namespaces:

```text
streaming
monitoring
```

Deploy:

- Producer
- Kafka
- Flink
- Prometheus
- Grafana

## Stage 4

Manage deployments using Helm.

Helm charts:

- Prometheus
- Grafana
- Strimzi
- Flink Kubernetes Operator

## Future Production Improvements

- Horizontal scaling
- High availability
- Persistent volumes
- Secrets management
- Rolling upgrades
- GitHub Actions CI/CD