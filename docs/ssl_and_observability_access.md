# SSL And Observability Access

Generated: 2026-09-02

## Current Public Endpoints

- Application: `https://fleetingcircus.ir/`
- Backend health: `https://fleetingcircus.ir/health/`
- Backend API docs: `https://fleetingcircus.ir/backend/docs/`
- Userservice API docs: `https://fleetingcircus.ir/userservice/docs/`
- Grafana: `https://fleetingcircus.ir/grafana/`

## Certificate

The control-plane deployment uses a Let's Encrypt certificate for:

- `fleetingcircus.ir`
- `www.fleetingcircus.ir`

The certificate was issued with Certbot's webroot challenge. Nginx serves challenge files from:

```text
/home/ubuntu/serverless-platform-current/nginx/certbot/www
```

Certificate files are stored on the control-plane server under:

```text
/home/ubuntu/serverless-platform-current/nginx/certbot/conf
```

The active certificate path inside the Nginx container is:

```text
/etc/letsencrypt/live/fleetingcircus.ir/fullchain.pem
/etc/letsencrypt/live/fleetingcircus.ir/privkey.pem
```

The issued certificate expires on `2026-11-30`.

## Renewal

The control-plane server has this renewal script:

```text
/home/ubuntu/serverless-platform-current/scripts/renew_ssl.sh
```

It runs Certbot in a container and reloads the Nginx container afterward.

Cron entry:

```cron
17 3 * * * /home/ubuntu/serverless-platform-current/scripts/renew_ssl.sh >> /home/ubuntu/serverless-platform-current/nginx/certbot/renew.log 2>&1
```

## Nginx Configs

The repo keeps two Nginx configs:

- `nginx/default.http.conf`: HTTP/dev/bootstrap config.
- `nginx/default.ssl.conf`: production HTTPS config.

For local development, `nginx/default.conf` should stay HTTP-friendly.

On the deployed control-plane server, `nginx/default.ssl.conf` is copied to:

```text
/home/ubuntu/serverless-platform-current/nginx/default.conf
```

## Observability

Grafana is publicly reachable through Nginx:

```text
https://fleetingcircus.ir/grafana/
```

The `/grafana/` path is protected by Nginx basic auth. Grafana also allows anonymous Viewer access behind that Nginx gate so dashboard panels can load without Grafana session/cookie problems under the `/grafana/` subpath.

Prometheus, Loki, cAdvisor and exporters are not published directly to host ports. They are reachable only inside the Docker network. Grafana uses the provisioned datasources:

- `Prometheus`
- `Loki`

Prometheus currently scrapes:

- Backend
- Userservice
- Orchestrator
- Redis exporter
- Backend Postgres exporter
- Userservice Postgres exporter
- cAdvisor
- Worker metrics at `10.42.1.56:9102`
- Worker metrics at `10.42.1.149:9102`

Loki currently collects Docker logs from the control-plane host through Grafana
Alloy. That includes backend, userservice, orchestrator, finalizer, projector,
reconciler and cleanup service logs. It does not yet collect logs from worker
containers running on separate worker VMs. To add those logs, run an Alloy
agent on each worker VM and point it at the central Loki endpoint over the
private network.

An empty "Recent Detailed Platform Errors" panel means no matching error lines
were found in the selected time range. Use the "Recent Platform Logs" panel to
confirm that Loki is receiving ordinary service logs.

Grafana credentials are stored on the control-plane server in:

```text
/home/ubuntu/serverless-platform-current/.env.control-plane
```

Relevant variables:

```env
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=...
```

The same username/password is used for the Nginx basic-auth prompt in front of `/grafana/`.

To read them from your machine:

```powershell
ssh -i .\local-ssh-keys\codex_deploy_ed25519 ubuntu@37.32.36.255 "cd /home/ubuntu/serverless-platform-current && grep '^GRAFANA_ADMIN_' .env.control-plane"
```

## Verification Commands

Check HTTPS from the server:

```bash
curl -vkI https://fleetingcircus.ir/health/
```

Check Grafana route:

```bash
curl -kI https://fleetingcircus.ir/grafana/login
```

Check Prometheus targets from the control-plane server:

```bash
cd /home/ubuntu/serverless-platform-current
docker compose -f docker-compose.control-plane.yml exec -T prometheus wget -qO- http://localhost:9090/api/v1/targets
```

As of setup time, Prometheus reported all configured scrape targets as `up`.

Check the dashboard data path through Grafana itself:

```bash
cd /home/ubuntu/serverless-platform-current
docker compose -f docker-compose.control-plane.yml exec -T grafana wget \
  --header='Content-Type: application/json' \
  --post-data='{"queries":[{"refId":"A","datasource":{"type":"prometheus","uid":"Prometheus"},"expr":"up{job=\"backend\"}","instant":true,"format":"time_series"}],"from":"now-15m","to":"now"}' \
  -qO- http://localhost:3000/api/ds/query
```

## Notes

The local Windows Schannel client reported a TLS client-credential error while testing HTTPS from PowerShell/curl. The server-side TLS check succeeded, the host listens on port `443`, and the certificate chain is served by Nginx. If this happens locally, test from a browser or from the server with `curl -vkI`.
