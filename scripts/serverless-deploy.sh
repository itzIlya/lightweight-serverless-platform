#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_PATH="${BASH_SOURCE[0]}"
SCRIPT_DIR="$(cd "${SCRIPT_PATH%/*}" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

CONTROL_ENV="${REPO_ROOT}/.env.control-plane"
WORKER_ENV="${REPO_ROOT}/.env.worker"
CONTROL_COMPOSE="${REPO_ROOT}/docker-compose.control-plane.yml"
WORKER_COMPOSE="${REPO_ROOT}/docker-compose.worker.yml"

cd "${REPO_ROOT}"

die() {
  echo "error: $*" >&2
  exit 1
}

have() {
  command -v "$1" >/dev/null 2>&1
}

require_docker() {
  have docker || die "docker is not installed or not in PATH."
  docker compose version >/dev/null 2>&1 || die "docker compose is not available."
}

random_hex() {
  if have openssl; then
    openssl rand -hex "${1:-32}"
  else
    od -An -N "${1:-32}" -tx1 /dev/urandom | tr -d ' \n'
  fi
}

detect_host_ip() {
  local ip=""
  if have hostname; then
    ip="$(hostname -I 2>/dev/null | awk '{print $1}' || true)"
  fi
  if [[ -z "${ip}" ]] && have ip; then
    ip="$(ip route get 1.1.1.1 2>/dev/null | awk '{for (i=1; i<=NF; i++) if ($i == "src") {print $(i+1); exit}}' || true)"
  fi
  if [[ -z "${ip}" ]]; then
    ip="127.0.0.1"
  fi
  printf '%s\n' "${ip}"
}

prompt() {
  local label="$1"
  local default_value="${2:-}"
  local value
  if [[ -n "${default_value}" ]]; then
    read -r -p "${label} [${default_value}]: " value
    printf '%s\n' "${value:-${default_value}}"
  else
    read -r -p "${label}: " value
    printf '%s\n' "${value}"
  fi
}

prompt_secret() {
  local label="$1"
  local default_value="${2:-}"
  local value
  if [[ -n "${default_value}" ]]; then
    read -r -s -p "${label} [generated; press Enter to use it]: " value
    echo >&2
    printf '%s\n' "${value:-${default_value}}"
  else
    read -r -s -p "${label}: " value
    echo >&2
    printf '%s\n' "${value}"
  fi
}

confirm() {
  local label="$1"
  local default="${2:-n}"
  local suffix="[y/N]"
  local value
  if [[ "${default}" == "y" ]]; then
    suffix="[Y/n]"
  fi
  read -r -p "${label} ${suffix}: " value
  value="${value:-${default}}"
  [[ "${value}" == "y" || "${value}" == "Y" || "${value}" == "yes" || "${value}" == "YES" ]]
}

write_control_plane_env() {
  local host="$1"
  local secret_key="$2"
  local postgres_password="$3"
  local userservice_postgres_password="$4"
  local worker_secret="$5"
  local grafana_password="$6"

  cat >"${CONTROL_ENV}" <<EOF
DEBUG=0
SECRET_KEY=${secret_key}
ALLOWED_HOSTS=*

CONTROL_PLANE_HOST=${host}

CORS_ALLOWED_ORIGINS=http://${host}:5173,http://localhost:5173
CORS_ALLOW_ALL_ORIGINS=false
CORS_ALLOW_CREDENTIALS=false
CORS_PREFLIGHT_MAX_AGE=86400

POSTGRES_DB=serverless
POSTGRES_USER=serverless
POSTGRES_PASSWORD=${postgres_password}
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

USERSERVICE_POSTGRES_DB=userservice
USERSERVICE_POSTGRES_USER=userservice
USERSERVICE_POSTGRES_PASSWORD=${userservice_postgres_password}

REDIS_URL=redis://redis:6379/0
JOB_QUEUE_NAME=function-jobs
LOCAL_REGISTRY=${host}:5000
REGISTRY_IMAGE_REF_HOST=${host}:5000
REGISTRY_INTERNAL_BASE_URL=http://registry:5000
BACKEND_BASE_URL=http://backend:8000
ORCHESTRATOR_BASE_URL=http://orchestrator:8010
WORKER_SHARED_SECRET=${worker_secret}

USERSERVICE_JWT_ISSUER=serverless-userservice
USERSERVICE_JWT_AUDIENCE=serverless-platform

V2_BUILD_PILOT_ENABLED=true
V2_INVOCATION_PILOT_ENABLED=true
V2_BUILD_ROLLOUT_PERCENT=100
V2_INVOCATION_ROLLOUT_PERCENT=100
V2_BUILD_CANARY_FUNCTION_IDS=
V2_INVOCATION_CANARY_FUNCTION_IDS=
V2_CUTOVER_STAGE=all
V1_JOB_CREATION_ENABLED=false
V1_COORDINATION_ENDPOINTS_ENABLED=true

SYNC_INVOCATION_TIMEOUT_SECONDS=15
SYNC_INVOCATION_POLL_INTERVAL_SECONDS=0.1
SYNC_INVOCATION_MAX_RESULT_BYTES=262144
SYNC_INVOCATION_MAX_STDOUT_BYTES=65536
SYNC_INVOCATION_MAX_STDERR_BYTES=65536

WORKER_WARM_CONTAINERS_ENABLED=true
WORKER_WARM_IDLE_TTL_SECONDS=60
WORKER_WARM_MAX_CONTAINERS=2
WORKER_WARM_MAX_PER_FUNCTION_VERSION=1
WORKER_WARM_MAX_AGE_SECONDS=900
WORKER_WARM_MAX_USES=100

OBJECT_STORAGE_ENABLED=false
OBJECT_STORAGE_ENDPOINT_URL=https://example-s3-endpoint
OBJECT_STORAGE_ACCESS_KEY_ID=replace-me
OBJECT_STORAGE_SECRET_ACCESS_KEY=replace-me
OBJECT_STORAGE_BUCKET_NAME=replace-me
OBJECT_STORAGE_REGION_NAME=us-east-1
OBJECT_STORAGE_FORCE_PATH_STYLE=true
OBJECT_STORAGE_MEDIA_LOCATION=media

GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=${grafana_password}
EOF
}

write_worker_env() {
  local host="$1"
  local worker_name="$2"
  local worker_secret="$3"
  local metrics_port="$4"
  local max_concurrency="$5"
  local max_invocation_concurrency="$6"
  local max_build_concurrency="$7"
  local heartbeat_seconds="$8"

  cat >"${WORKER_ENV}" <<EOF
CONTROL_PLANE_HOST=${host}

WORKER_NAME=${worker_name}
WORKER_MAX_CONCURRENCY=${max_concurrency}
WORKER_MAX_INVOCATION_CONCURRENCY=${max_invocation_concurrency}
WORKER_MAX_BUILD_CONCURRENCY=${max_build_concurrency}
WORKER_HEARTBEAT_SECONDS=${heartbeat_seconds}
WORKER_METRICS_PORT=${metrics_port}

REDIS_URL=redis://${host}:6379/0
BACKEND_BASE_URL=http://${host}:8000
ORCHESTRATOR_BASE_URL=http://${host}:8010
LOCAL_REGISTRY=${host}:5000
WORKER_SHARED_SECRET=${worker_secret}

FUNCTION_CONTAINER_NETWORK=

WORKER_WARM_CONTAINERS_ENABLED=true
WORKER_WARM_IDLE_TTL_SECONDS=60
WORKER_WARM_MAX_CONTAINERS=2
WORKER_WARM_MAX_PER_FUNCTION_VERSION=1
WORKER_WARM_MAX_AGE_SECONDS=900
WORKER_WARM_MAX_USES=100
WORKER_WARM_RESIDENT_RUNNER_ENABLED=false
WORKER_WARM_RESIDENT_RUNNER_PORT=8765
WORKER_WARM_RESIDENT_RUNNER_STARTUP_TIMEOUT_SECONDS=5

WORKER_RUNNER_DIRECT_OUTPUT_UPLOAD_ENABLED=false
WORKER_RUNNER_OUTPUT_UPLOAD_TIMEOUT_SECONDS=10
WORKER_RUNNER_OUTPUT_UPLOAD_TOKEN_TTL_SECONDS=300
EOF
}

prepare_control_plane_env() {
  if [[ -f "${CONTROL_ENV}" ]] && confirm ".env.control-plane already exists. Use it as-is" "y"; then
    return
  fi

  local default_host
  default_host="$(detect_host_ip)"
  local host
  host="$(prompt "Control-plane host/IP reachable by workers" "${default_host}")"
  local secret_key
  secret_key="$(prompt_secret "Django SECRET_KEY" "$(random_hex 32)")"
  local postgres_password
  postgres_password="$(prompt_secret "Backend Postgres password" "$(random_hex 16)")"
  local userservice_postgres_password
  userservice_postgres_password="$(prompt_secret "Userservice Postgres password" "$(random_hex 16)")"
  local worker_secret
  worker_secret="$(prompt_secret "Shared worker secret" "$(random_hex 32)")"
  local grafana_password
  grafana_password="$(prompt_secret "Grafana admin password" "$(random_hex 12)")"

  write_control_plane_env \
    "${host}" \
    "${secret_key}" \
    "${postgres_password}" \
    "${userservice_postgres_password}" \
    "${worker_secret}" \
    "${grafana_password}"
}

prepare_worker_env() {
  if [[ -f "${WORKER_ENV}" ]] && confirm ".env.worker already exists. Use it as-is" "y"; then
    return
  fi

  local default_name
  default_name="worker-$(hostname -s 2>/dev/null || echo remote)"
  local host
  host="$(prompt "Control-plane host/IP" "")"
  [[ -n "${host}" ]] || die "control-plane host is required."
  local worker_name
  worker_name="$(prompt "Unique worker name" "${default_name}")"
  local worker_secret
  worker_secret="$(prompt_secret "Shared worker secret from the control plane" "")"
  [[ -n "${worker_secret}" ]] || die "shared worker secret is required."
  local metrics_port
  metrics_port="$(prompt "Worker metrics port" "9102")"
  local max_concurrency
  max_concurrency="$(prompt "Max total worker concurrency" "4")"
  local max_invocation_concurrency
  max_invocation_concurrency="$(prompt "Max invocation concurrency" "4")"
  local max_build_concurrency
  max_build_concurrency="$(prompt "Max build concurrency" "1")"
  local heartbeat_seconds
  heartbeat_seconds="$(prompt "Heartbeat seconds" "10")"

  write_worker_env \
    "${host}" \
    "${worker_name}" \
    "${worker_secret}" \
    "${metrics_port}" \
    "${max_concurrency}" \
    "${max_invocation_concurrency}" \
    "${max_build_concurrency}" \
    "${heartbeat_seconds}"

  cat <<EOF

Before the worker can pull function images, its Docker daemon must trust the
control-plane registry if you are using the default plain HTTP registry:

  sudo mkdir -p /etc/docker
  sudo tee /etc/docker/daemon.json >/dev/null <<JSON
  {"insecure-registries":["${host}:5000"]}
JSON
  sudo systemctl restart docker

EOF
}

compose_control() {
  docker compose --env-file "${CONTROL_ENV}" -f "${CONTROL_COMPOSE}" "$@"
}

compose_worker() {
  docker compose --env-file "${WORKER_ENV}" -f "${WORKER_COMPOSE}" "$@"
}

wait_for_exec() {
  local service="$1"
  shift
  local i
  for i in $(seq 1 60); do
    if "$@" exec -T "${service}" sh -lc "true" >/dev/null 2>&1; then
      return 0
    fi
    sleep 2
  done
  return 1
}

start_control_plane() {
  prepare_control_plane_env
  compose_control up -d --build
  wait_for_exec userservice compose_control || die "userservice container did not become ready for migrations."
  wait_for_exec backend compose_control || die "backend container did not become ready for migrations."
  compose_control exec -T userservice python manage.py migrate
  compose_control exec -T backend python manage.py migrate

  local host
  host="$(grep -E '^CONTROL_PLANE_HOST=' "${CONTROL_ENV}" | cut -d= -f2-)"
  cat <<EOF

Control plane is up.

Frontend:     http://${host}:5173
Backend API:  http://${host}:8000
Userservice:  http://${host}:8100
Orchestrator: http://${host}:8010
Registry:     ${host}:5000

To add a worker later, copy this repository to the worker machine and run:

  bash scripts/serverless-deploy.sh

Choose "worker" and use this control-plane host:

  ${host}

EOF
}

start_worker() {
  prepare_worker_env
  compose_worker up -d --build
  compose_worker ps
}

show_status() {
  if [[ -f "${CONTROL_ENV}" ]]; then
    echo
    echo "Control-plane services:"
    compose_control ps || true
  else
    echo
    echo "No .env.control-plane found."
  fi

  if [[ -f "${WORKER_ENV}" ]]; then
    echo
    echo "Worker services:"
    compose_worker ps || true
  else
    echo
    echo "No .env.worker found."
  fi
}

stop_worker_gracefully() {
  [[ -f "${WORKER_ENV}" ]] || die ".env.worker does not exist on this machine."
  compose_worker stop worker
  compose_worker ps
}

main_menu() {
  require_docker

  cat <<EOF
Serverless Platform distributed bootstrap

What do you want to run?
  1) control-plane
  2) worker
  3) status
  4) stop worker gracefully
EOF

  local choice
  read -r -p "Choose 1-4: " choice

  case "${choice}" in
    1|control-plane|control) start_control_plane ;;
    2|worker) start_worker ;;
    3|status) show_status ;;
    4|stop) stop_worker_gracefully ;;
    *) die "unknown choice: ${choice}" ;;
  esac
}

main_menu "$@"
