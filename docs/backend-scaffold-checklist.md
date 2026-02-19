# Backend Scaffold Checklist (FastAPI + Native App/Worker + Dockerized Infra)

Use this checklist as the execution plan for the first backend vertical slice.

## Scope

- API and worker run natively in a Python virtual environment.
- Infra services run in Docker Compose:
  - PostgreSQL
  - Redis
  - MinIO (optional for local S3-compatible storage)
- First shipped functionality:
  - create analysis job
  - process metadata-only quality checks (`fps`, `resolution`, `duration`)
  - fetch analysis status and gate result

## 0. Repo Bootstrap

- [x] Create backend folder structure:
  - [x] `backend/app/api/v1/`
  - [x] `backend/app/core/`
  - [x] `backend/app/db/`
  - [x] `backend/app/models/`
  - [x] `backend/app/schemas/`
  - [x] `backend/app/services/`
  - [x] `backend/app/workers/`
  - [x] `backend/alembic/`
- [x] Add `pyproject.toml` (or `requirements.txt`) with pinned dependencies.
- [x] Add `.env.example` with local defaults.

## 1. Docker Compose Infra

- [x] Add `docker-compose.yml` with:
  - [x] `postgres` (port 5432)
  - [x] `redis` (port 6379)
  - [x] `minio` (ports 9000/9001, optional but recommended)
- [x] Add healthchecks for each service.
- [x] Add named volumes for persistence.
- [x] Add helper commands in `Makefile`:
  - [x] `make infra-up`
  - [x] `make infra-down`
  - [x] `make infra-logs`

## 2. FastAPI App Skeleton

- [x] Create FastAPI app entrypoint (`backend/app/main.py`).
- [x] Add `/healthz` endpoint.
- [ ] Add API router namespace `/v1`.
- [ ] Add request ID middleware and structured logging.
- [ ] Add config loader from env (`pydantic-settings`).

## 3. Database and Migrations

- [ ] Configure SQLAlchemy engine/session.
- [ ] Configure Alembic migration environment.
- [ ] Create initial tables:
  - [ ] `videos`
  - [ ] `analyses`
  - [ ] `analysis_checks`
  - [ ] `analysis_quality_gate_results`
- [ ] Run and verify first migration locally.

## 4. Queue and Worker Skeleton

- [ ] Configure Redis queue client (RQ or Celery).
- [ ] Add worker process entrypoint.
- [ ] Implement `process_analysis_job(analysis_id)` stub.
- [ ] Add retry policy and failure status handling.
- [ ] Ensure worker updates analysis status:
  - [ ] `queued`
  - [ ] `processing`
  - [ ] `complete`
  - [ ] `failed`

## 5. API Endpoints (V0)

- [ ] `POST /v1/analyses`
  - [ ] validate payload
  - [ ] create analysis row
  - [ ] enqueue job
  - [ ] return `analysis_id`, `status`
- [ ] `GET /v1/analyses/{analysis_id}`
  - [ ] return status
  - [ ] return gate output when available
  - [ ] return model/rule version fields

## 6. Metadata-Only Quality Gate (First Working Slice)

- [ ] Implement media probe utility (`ffprobe` preferred).
- [ ] Compute hard checks:
  - [ ] `fps >= 60`
  - [ ] `resolution >= 1280x720`
  - [ ] `1.2s <= duration <= 6.0s`
- [ ] Persist per-check raw values and pass/fail.
- [ ] Generate error codes:
  - [ ] `ERR_FPS_TOO_LOW`
  - [ ] `ERR_RESOLUTION_TOO_LOW`
  - [ ] `ERR_DURATION_OUT_OF_RANGE`
- [ ] Map each error code to a recapture tip.
- [ ] Return full gate payload matching `docs/capture-quality-gate-spec.md`.

## 7. Local Developer Workflow

- [ ] Add startup docs to `backend/README.md`.
- [ ] Add commands:
  - [ ] start API server
  - [ ] start worker
  - [ ] run migrations
  - [ ] run tests
- [ ] Add one integration test:
  - [ ] create analysis
  - [ ] process job
  - [ ] fetch completed result

## 8. Observability Baseline

- [ ] Log analysis lifecycle events with `analysis_id`.
- [ ] Log individual check outputs and thresholds.
- [ ] Add basic metrics counters:
  - [ ] analyses created
  - [ ] analyses completed
  - [ ] analyses failed
  - [ ] gate pass/fail totals

## 9. Definition of Done (Backend Slice 1)

- [ ] Fresh clone can run infra with one command.
- [ ] API and worker can run locally without Docker.
- [ ] `POST /v1/analyses` queues a job successfully.
- [ ] Worker computes metadata checks and stores results.
- [ ] `GET /v1/analyses/{id}` returns deterministic gate output.
- [ ] At least one end-to-end integration test passes.

## Suggested Execution Order

1. Docker Compose infra
2. FastAPI skeleton + health endpoint
3. DB models + migrations
4. Queue/worker
5. Endpoints
6. Metadata-only gate
7. Test + docs + cleanup
