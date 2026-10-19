#!/bin/bash
# ─── ICA CRM — Production Deployment Script ──────────────────────────────────
# Usage (on the VPS):  ./deploy.sh            # pull latest master, build, restart
#                      ./deploy.sh --no-pull  # build + restart current working tree
#
# Matches how the app actually runs: PM2 process "ica-crm" (fork mode, port 5000,
# dist/index.cjs). Backs up dist/ first and rolls back automatically if the build
# fails or the app doesn't answer after restart.

set -euo pipefail

APP_DIR="/var/www/ica-crm"
PM2_NAME="ica-crm"
BRANCH="master"
HEALTH_URL="http://127.0.0.1:5000/"
BACKUP_DIR="$APP_DIR/.deploy-backup"

cd "$APP_DIR"
echo "🚀 ICA CRM deployment starting ($(date '+%F %T'))"

# ─── 1. Pull latest code ──────────────────────────────────────────────────────
if [[ "${1:-}" != "--no-pull" ]]; then
  if [[ -n "$(git status --porcelain --untracked-files=no)" ]]; then
    echo "❌ Uncommitted changes in tracked files — commit them or run with --no-pull."
    git status --short --untracked-files=no
    exit 1
  fi
  echo "📦 Pulling origin/$BRANCH..."
  OLD_LOCK=$(git rev-parse HEAD:package-lock.json)
  git pull --ff-only origin "$BRANCH"
  NEW_LOCK=$(git rev-parse HEAD:package-lock.json)

  # ─── 2. Install dependencies only if the lockfile changed ─────────────────
  if [[ "$OLD_LOCK" != "$NEW_LOCK" ]]; then
    echo "📚 package-lock.json changed — installing dependencies..."
    npm ci
  fi
fi

# ─── 3. Back up current build ─────────────────────────────────────────────────
rm -rf "$BACKUP_DIR" && cp -a dist "$BACKUP_DIR"
echo "💾 Previous build backed up to $BACKUP_DIR"

rollback() {
  echo "↩️  Rolling back to previous build..."
  rm -rf dist && cp -a "$BACKUP_DIR" dist
  pm2 restart "$PM2_NAME" >/dev/null
  echo "❌ Deployment failed — previous build restored."
  exit 1
}

# ─── 4. Build ─────────────────────────────────────────────────────────────────
echo "🔨 Building..."
npm run build || rollback

# ─── 5. Restart and health-check ──────────────────────────────────────────────
echo "🔄 Restarting $PM2_NAME..."
pm2 restart "$PM2_NAME" >/dev/null

for i in $(seq 1 20); do
  if [[ "$(curl -s -o /dev/null -w '%{http_code}' "$HEALTH_URL")" == "200" ]]; then
    echo "✅ Deployed $(git log -1 --format='%h %s') — app healthy after ${i}s"
    pm2 save >/dev/null
    exit 0
  fi
  sleep 1
done

echo "⚠️  App did not return 200 within 20s"
rollback
