# AGENTS

This file defines the engineering conventions for AI coding agents (ChatGPT, Codex, Claude Code, Cursor, Copilot, Gemini CLI, etc.).

## Repository Rules

- Preserve repository structure.
- Prefer incremental changes.
- Do not perform unrelated refactoring.
- Keep documentation synchronized with code.

## Git Rules

- Never commit directly to `main`.
- Use `develop` as the integration branch.
- Use feature branches.

## Branch Naming

```text
feature/<scope>-<description>
bugfix/<scope>-<description>
hotfix/<scope>-<description>
release/v<major>.<minor>.<patch>
```

## Commit Convention

Use Conventional Commits.

## Versioning

Follow Semantic Versioning.

## Documentation

Whenever architecture or functionality changes:
- Update README if user-facing.
- Update docs/ for technical details.
- Update CHANGELOG for releases.

## Design Philosophy

Build simple → Stream events → Add state → Detect fraud → Observe → Containerise → Deploy like production.