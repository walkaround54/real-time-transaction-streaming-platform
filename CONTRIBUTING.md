# CONTRIBUTING

## Branch Strategy

Protected branches:

- `main`

Work only on short-lived branches.

```text
feature/<scope>-<description>
bugfix/<scope>-<description>
hotfix/<scope>-<description>
release/v<major>.<minor>.<patch>
```

Examples:

- feature/producer-transaction-generator
- feature/kafka-local-compose
- feature/flink-fraud-engine

# Service Structure Convention

Every deployable component within this repository is treated as an independent service. Each service is responsible for its own source code, dependencies, testing, and container image.

---

## Repository Structure

```text
real-time-transaction-streaming-platform/
├── producer/
├── consumer/
├── flink-jobs/
├── kafka/
├── observability/
├── kubernetes/
├── docker-compose/
├── docs/
└── scripts/
```

Each top-level service should be independently buildable and testable.

---

# Python Services

Python services should follow the `src` layout.

```text
producer/
├── Dockerfile
├── .dockerignore
├── pyproject.toml
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

Dockerfiles for Python services specifically should assume the build context is the service directory.

Typical pattern:

WORKDIR /app/producer
COPY . /app/producer/
RUN pip install --no-cache-dir .
CMD ["python", "-m", "producer.generator"]


## Import Convention

Always import using the package name.

```python
from producer.generator import generate_transactions
from producer.models import Transaction
```

Avoid importing using:

```python
from src.generator import ...
from producer.src.generator import ...
```

The package name should always represent the application.

## Docker

Each deployable service owns its own Dockerfile and image.

## Build Context

Build each service from its own service directory.

Examples:

```bash
docker build -t transaction-producer ./producer
docker build -t flink-job ./flink-jobs/my-job
```

Tests should run outside the runtime image unless the image is explicitly a test image.
The runtime container should include only what is required to run the service.

---

## Testing

Each service owns its own unit tests.

```text
tests/
```

Tests should import the package directly.

```python
from producer.generator import ...
```

The project-level `scripts/check.py` is responsible for executing tests across all Python services.

---

# Java / Flink Services

Java services should follow Maven conventions.

```text
flink-jobs/
├── Dockerfile
├── pom.xml
└── src/
    ├── main/
    │   └── java/
    └── test/
        └── java/
```

Do not attempt to force Java into the Python project layout.

---

# Infrastructure Services

Infrastructure components primarily contain configuration rather than application code.

## Kafka

```text
kafka/
├── docker-compose.kafka.yml (optional)
├── config/
└── README.md
```

## Observability

```text
observability/
├── prometheus/
├── grafana/
└── alertmanager/
```

## Kubernetes

```text
kubernetes/
├── producer/
├── consumer/
├── flink/
├── kafka/
└── observability/
```

Each folder contains Kubernetes manifests specific to that service.

---

# Docker Compose

Repository-level orchestration lives under:

```text
docker-compose/
```

Compose is responsible for:

- Building services
- Creating networks
- Creating volumes
- Starting services
- Connecting services together

Services should never depend on Compose to define their internal structure.

---

# General Principles

- One deployable application = one service folder.
- Every service owns its dependencies.
- Every service owns its tests.
- Every service owns its Dockerfile.
- Follow language-specific conventions internally.
- Keep services independently buildable, testable, and deployable.

## Workflow

1. Create branch from `main`
2. Commit using Conventional Commits
3. Keep PRs focused on one logical change
4. Update documentation when behaviour changes
5. Merge into `main`

## Conventional Commits

`feat:` `fix:` `docs:` `refactor:` `test:` `build:` `ci:` `chore:` `perf:` `style:`