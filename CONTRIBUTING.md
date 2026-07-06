# CONTRIBUTING

## Branch Strategy

Protected branches:

- `main`
- `develop`

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

## Workflow

1. Create branch from `develop`
2. Commit using Conventional Commits
3. Keep PRs focused on one logical change
4. Update documentation when behaviour changes
5. Merge into `develop`
6. Release via `release/*` branches

## Conventional Commits

`feat:` `fix:` `docs:` `refactor:` `test:` `build:` `ci:` `chore:` `perf:` `style:`