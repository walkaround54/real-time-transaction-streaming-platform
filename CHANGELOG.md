# Changelog

All notable changes to this project will be documented in this file.

The changelog is append-only. New releases or meaningful milestones should be added as new entries without rewriting prior history.

## [v0.2.0] - 2026-07-09

### Added

- Dockerized the Python transaction producer into a runtime image.
- Verified the producer container runs successfully with `docker run`.
- Kept the runtime image focused on application code and runtime dependencies only.

## [v0.1.0] - 2026-07-06

### Added

- Python transaction generator with realistic customer, merchant, and currency simulation.
- Pydantic transaction model with structured logging and unit tests.
