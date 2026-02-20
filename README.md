# Golf Coach

Initial scaffold for a golf swing analysis platform.

## Quick Start

1. One-time local Docker setup (without Docker Desktop):

```bash
brew install docker docker-compose colima
colima start
```

2. Start local infrastructure:

```bash
make infra-up
```

3. Start backend API:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
cp .env.example .env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Verify API health:

```bash
curl http://localhost:8000/healthz
```

If Docker is not running in a new shell/session:

```bash
colima start
```

## Infra Services

- Postgres: `localhost:5432`
- Redis: `localhost:6379`
- MinIO API: `localhost:9000`
- MinIO Console: `http://localhost:9001`

## Docs

See `docs/README.md` for product and technical planning docs.
