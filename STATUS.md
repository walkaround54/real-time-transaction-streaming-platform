# STATUS.md

Current Version

v0.4.0

Current Branch

feature/kafka-cluster

### Current Phase

Phase 5 - Flink processing

### Current Work

Add the Kafka source for `transactions_raw` to the first Apache Flink 2.2.1 Java DataStream job

# Phase 5 Task Completion Status

1. Scaffold the first Flink Java job project - completed
2. Add Kafka source for `transactions_raw`
3. Parse transaction JSON events
4. Assign event time and watermarks using `event_time`
5. Key the stream by `customer_id`
6. Add a one-minute tumbling event-time aggregation for first-job validation
7. Publish aggregated output to `transactions_processed`
8. Add local verification for the Flink processing flow

# Previous Phases Task Completion

### Phase 1 Tasks:

1. Repository setup
2. GitHub Flow
3. Documentation
4. Transaction model
5. Transaction factory
6. Continuous transaction generator
7. Application settings
8. Logging
9. Unit tests
10. `pyproject.toml`-based packaging

### Phase 2 Tasks:

1. Finalise the producer Dockerfile
2. Verify the producer runs inside Docker
3. Keep tests outside the runtime image

### Phase 3 Tasks:

1. Define the Kafka producer integration
2. Send simulated transactions to `transactions_raw`
3. Add basic local verification for message delivery
4. Start Kafka in KRaft mode with Docker Compose
5. Create `transactions_raw` via a one-shot topic setup service
6. Verify the broker and topic setup startup successfully
7. Verify the producer publishes to `transactions_raw`

### Phase 4 Tasks:

1. Document event time and processing time for transaction events in `docs/flink.md`
2. Define the initial one-minute validation window for transaction metrics in `docs/flink.md`
3. Define the watermark tolerance and late-event policy in `docs/flink.md`
4. Practise consumer groups, offsets and replay with `transactions_raw`
5. Document checkpointing, delivery guarantees and backpressure across `docs/kafka.md` and `docs/flink.md`
6. Define the first Flink input, output, keying and aggregation contract in `docs/flink.md`
7. Split Phase 4 concept notes by system responsibility: Kafka details in `docs/kafka.md`, Flink details in `docs/flink.md`
8. Clarify that realistic fraud detection will later require customer profiles, longer historical baselines and anomalous transaction generation

Target Release

v0.5.0 - First Flink Java DataStream processing job

Blockers

None.

# Project Structure (Auto-generated)

<!-- PROJECT_TREE_START -->
```text
real-time-transaction-streaming-platform
├── .agents
├── .github
├── compose
│   ├── flink.yml
│   └── kafka.yml
├── docs
│   ├── architecture.md
│   ├── deployment.md
│   ├── end_to_end_architecture.png
│   ├── flink.md
│   ├── fraud-engine.md
│   ├── kafka.md
│   ├── observability.md
│   ├── roadmap.md
│   └── technologies.md
├── flink-jobs
│   └── transaction-processor
│       ├── src
│       │   └── main
│       │       └── java
│       │           └── com
│       │               └── transactionstreaming
│       │                   └── flink
│       │                       └── TransactionProcessorJob.java
│       ├── target
│       │   ├── classes
│       │   │   └── com
│       │   │       └── transactionstreaming
│       │   │           └── flink
│       │   │               └── TransactionProcessorJob.class
│       │   ├── generated-sources
│       │   │   └── annotations
│       │   ├── maven-archiver
│       │   │   └── pom.properties
│       │   ├── maven-status
│       │   │   └── maven-compiler-plugin
│       │   │       └── compile
│       │   │           └── default-compile
│       │   │               ├── createdFiles.lst
│       │   │               └── inputFiles.lst
│       │   ├── original-transaction-processor-0.5.0-SNAPSHOT.jar
│       │   └── transaction-processor-0.5.0-SNAPSHOT.jar
│       └── pom.xml
├── kafka
├── kubernetes
├── observability
├── producer
│   ├── src
│   │   └── producer
│   │       ├── __init__.py
│   │       ├── generator.py
│   │       ├── kafka_client.py
│   │       ├── logging_config.py
│   │       ├── models.py
│   │       ├── settings.py
│   │       └── transaction_factory.py
│   ├── tests
│   │   ├── test_generator.py
│   │   ├── test_kafka_client.py
│   │   └── test_transaction_factory.py
│   ├── .dockerignore
│   ├── Dockerfile
│   └── pyproject.toml
├── scripts
│   ├── __init__.py
│   ├── test_python_services.py
│   └── update_project_tree.py
├── .gitignore
├── AGENTS.md
├── all_info.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── kafka-logs.txt
├── PROJECT_CONTEXT.md
├── README.md
├── STATUS.md
└── VERSIONING.md
```

<!-- PROJECT_TREE_END -->
