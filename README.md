# Compose Casserole

Docker Compose stack: Nginx front door, Flask API, Redis. Healthchecks gate service start order; Nginx proxies `/api/*` to the API.

## Run

```bash
docker compose up --build
```

| Service | URL |
|---------|-----|
| Web | http://localhost:8088 |
| API health | http://localhost:5005/health |
| Via Nginx | http://localhost:8088/api/health |
| Counter | http://localhost:8088/api/counter |

## Layout

```
docker-compose.yml
web/          static page + nginx reverse-proxy config
api/          Flask app, Dockerfile, requirements
```

`depends_on: condition: service_healthy` waits for readiness, not just process start.

## License

MIT
