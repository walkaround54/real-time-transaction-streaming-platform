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

## Documentation Update Trigger and Preservation Rules

When the user asks to update `STATUS.md`, `PROJECT_CONTEXT.md`, or `CHANGELOG.md`:
- Preserve all existing content unless a change is explicitly requested.
- Update only the sections related to the current task.
- Do not remove historical context from `STATUS.md`, `PROJECT_CONTEXT.md`, or `CHANGELOG.md`.
- Prefer append-only updates for `CHANGELOG.md`.
- If a change would delete or substantially rewrite existing documentation, pause and ask first.
- Never rewrite an entire document unless explicitly requested.

### `PROJECT_CONTEXT.md`

- Update `Current Project Status` when the current phase is complete or has clearly advanced.
- Append to `Current Architecture` when a new completed component changes the system shape.
- Append to `Completed Features` when a feature or capability is finished.
- Remove completed items from `Upcoming Milestones` only after they are fully delivered.
- Keep the broader project narrative, learning philosophy, and historical context intact.

### `STATUS.md`

- Update `Current Phase` when the project moves forward.
- Update `Current Work` to reflect the active task.
- Update `Phase X Task Completion Status` as tasks are completed.
- Append previously completed phases to `Previous Phases Task Completion` if they are not already listed.
- Do not change "# Project Structure (Auto-generated)" section; leave that to `scripts/update_project_tree.py`.

### `CHANGELOG.md`

- Treat the changelog as append-only.
- Use `VERSIONING.md` as the source of truth for release versions.
- Create one changelog entry per actual release, not per commit.
- Use the corresponding milestone version from `VERSIONING.md` as the release heading.
- Keep older entries intact.
- Use concise release notes that summarize what changed, why it mattered, and any notable follow-up work.
- If the current work is not yet a release, do not create a new changelog version entry prematurely.

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
