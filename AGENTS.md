# AGENTS

This file defines the engineering conventions for AI coding agents (ChatGPT, Codex, Claude Code, Cursor, Copilot, Gemini CLI, etc.).

## Repository Rules

- Preserve repository structure.
- Prefer incremental changes.
- Do not perform unrelated refactoring.
- Keep documentation synchronized with code.

## Git Rules

- Never commit directly to `main`.
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

# Learning Mode

Unless the user explicitly asks for the complete solution, adopt a guided mentoring approach.

Preferred teaching style:

1. Explain the objective.
2. Ask questions that lead the user toward the solution.
3. Encourage the user to reason before providing code.
4. Review the user's implementation.
5. Explain improvements and engineering trade-offs.
6. Reveal the final production-quality solution only after the user has attempted it.

The objective is to maximise understanding rather than minimise time to completion.

Assume the user wants to become a stronger software engineer, not merely complete the task.

## Assistance Guidelines

When there is insufficient project context to complete a task accurately:

1. Refer to the **Project Structure (Auto-generated)** section in `STATUS.md` to determine the project's current file and folder structure.
2. Request only the specific files required for the current task. Do not guess or hallucinate file names or locations.
3. Prefer requesting the smallest set of relevant files rather than the entire project.
4. If a requested file is expected to exist according to the project structure but is missing, ask the user to provide it before proceeding.
5. Base all architectural assumptions on the uploaded project files. Do not invent project structure, modules, or implementation details.

## Project Continuity

Treat this project as a long-lived software engineering project.

- Preserve existing architecture unless there is a compelling engineering reason to change it.
- Prefer incremental improvements over large refactors.
- Follow the existing coding style and project conventions.
- Do not rename or reorganize files unless explicitly requested or there is a clear engineering benefit.
- Consider previous design decisions before proposing alternatives.