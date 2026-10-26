# LinkScope

LinkScope is a URL-shortening and link-analytics platform. The initial MVP
will let a user create a short link, redirect visitors to the stored HTTP or
HTTPS destination, and record minimal click activity.

## Initial architecture

The project has two separate applications:

- `backend/`: FastAPI API, validation, short-code generation, redirects,
  click tracking, and database access.
- `frontend/`: Next.js user interface for the landing page, shortening form,
  link management, and analytics.
- PostgreSQL: persistent storage for links and click events.

The frontend does not contain URL-shortening business logic. It communicates
with the backend over HTTP.

## Initial MVP scope

The first implementation will include:

1. A health endpoint.
2. HTTP/HTTPS destination URL validation.
3. Secure random short-code generation with database-enforced uniqueness.
4. Link creation and listing.
5. Short-link redirection.
6. Minimal click-event recording.
7. Basic analytics based on real click events.

Authentication, custom aliases, QR codes, geographic analytics, and advanced
abuse prevention are intentionally deferred until the core workflow is
working and tested. Until authentication is implemented, this is a
development-stage MVP and does not provide private user accounts.

## Local database

The development database runs in Docker:

```bash
cp .env.example .env
docker compose up -d postgres
```

The `.env` file is local-only and must not be committed. The example password
is suitable only for local development.

## Planned local services

| Service | Address |
| --- | --- |
| Frontend | `http://localhost:3000` |
| Backend API | `http://localhost:8000` |
| FastAPI docs | `http://localhost:8000/docs` |
| PostgreSQL | `localhost:5432` |

## Development status

The repository foundation is complete. The next milestone is initializing the
FastAPI backend, configuring its dependencies, and adding a tested health
endpoint before implementing database-backed links.
