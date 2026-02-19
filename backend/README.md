# Backend Quick Start

This backend runs as native Python processes, while infrastructure dependencies run via Docker Compose.

## Prerequisites

- Python 3.12+
- Docker + Docker Compose

## 1) Start Infra Services

From repository root:

```bash
make infra-up
make infra-ps
```

Services started:

- PostgreSQL on `localhost:5432`
- Redis on `localhost:6379`
- MinIO API on `localhost:9000`
- MinIO console on `localhost:9001`

## 2) Set Up Python Environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

## 3) Configure Local Environment

```bash
cp .env.example .env
```

## 4) Run API Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Health check:

```bash
curl http://localhost:8000/healthz
```

Expected response:

```json
{"status":"ok"}
```

## Infra Helpers

From repository root:

```bash
make infra-logs
make infra-down
```
