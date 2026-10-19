# ICA CRM (icacrmweb)

Multi-tenant SaaS CRM for insurance/sales agencies, live at https://crm.icaweb.in (marketing site: icaweb.in). Owner: Sameer, ICA (Innovation, Consulting & Automation).

Built exclusively for **Indian insurance agencies**. A white-label fork, **APLM CRM** (crm.aplmsales.com, separate repo `icassameer/aplm`), runs for a client with its own branding and RC limit (100/month on ENTERPRISE). When fixing a shared feature, note whether the APLM fork needs the same change.

## Stack and layout
- `client/src/`: React 18, Vite 7, wouter routing, TanStack Query. Pages are in `client/src/pages/`.
- `server/routes.ts`: Express 5, and almost the whole API in one large file. `server/index.ts` handles app setup, CORS, the error handler and the daily cron. `server/storage.ts` holds the DB access layer.
- `shared/schema.ts`: Drizzle ORM tables and enums (PostgreSQL 16). Read this first for the data model.
- Integrations: Razorpay (subscriptions and add-on credits via webhooks), OpenAI, Sarvam, Anthropic, Resend email, and an external RC (vehicle registration) lookup API.
- Don't create `*.bak*` copies of files (they're gitignored). Use git commits or branches instead.

## Domain rules
- Tenancy is by `agency_code` (format `ICA-XXXXXX`, **contains a hyphen**). Users link to agencies by `agency_code`; there is no `agency_id`. Any validation of agency codes must allow `-`.
- Roles: `MASTER_ADMIN` (platform owner), `AGENCY_ADMIN`, `TEAM_LEADER`, `TELE_CALLER`.
- Plans: `BASIC`, `PRO`, `ENTERPRISE`. RC lookups are limited to 0, 50 and 200 per month respectively.
- Subscription state lives on the **agency** (`subscription_status`, `subscription_expiry`, `is_active`), not on the user. Extending it means: count from the current expiry if it's in the future, else from now; set ACTIVE; write an `audit_logs` row with action `SUBSCRIPTION_EXTENDED`. This mirrors `POST /api/subscription/extend`.
- Lead statuses: `NEW`, `CONTACTED`, `FOLLOW_UP`, `CONVERTED`, `NOT_INTERESTED`, `RENEWAL`. A lead moves from CONVERTED to RENEWAL automatically after 10 months.
- Auth: a 24-hour JWT plus a per-user `sessionToken`, so each user has one active session. Protect routes with `authMiddleware`, `roleMiddleware(...)` and `checkPlan(...)` from `server/routes.ts`. Every new endpoint that returns agency data needs auth and must be scoped to `req.user.agencyCode` (MASTER_ADMIN excepted).
- Significant admin actions write to `audit_logs`.

## Commands
- `npm run dev`: dev server (port 5000).
- `npm run build`: builds the client into `dist/public` and the server into `dist/index.cjs`.
- `npx tsc --noEmit`: type-check. There are old errors in `server/replit_integrations/*`; ignore them, but files you touch must be clean.
- There is no automated test suite. Verify by building and exercising the changed endpoint or page.

## Deploy and environments
- Production runs on one VPS behind Cloudflare and nginx, as PM2 process `ica-crm` (fork mode, port 5000).
- **Deploy only from the server:** `cd /var/www/ica-crm && ./deploy.sh`. It pulls `master`, builds, restarts, health-checks and rolls back automatically on failure. `./deploy.sh --no-pull` deploys the current working tree. `ecosystem.config.cjs` describes a cluster setup that is NOT what runs.
- **Cloud / web sessions** (claude.ai/code) have no access to the server, database or logs. Work on a branch and open a PR to `master`. The owner merges it and runs `./deploy.sh` on the server.
- **Server sessions** (VS Code on the VPS) may run the build, query the DB and deploy, but confirm with the owner before deploying or changing production data.

## Security rules
- Never commit or write secrets anywhere: `.env` values, tokens, passwords, DB URLs. Refer to env vars by name only.
- GitHub access from the server uses per-repo SSH deploy keys (host aliases `github-icacrm`, `github-aplm`). Never put tokens in remote URLs.
- Don't leave downloadable archives in the project root. `/api/download-project` serves `ica-crm-project.zip` without auth.

## Docs
- `docs/claude-project-knowledge.md`: project overview, operations log and open follow-ups. Update it, newest first, after significant changes or incidents.
- `ICA_CRM_SOP_v9_8_5.docx`: the standard operating procedure for how the CRM is used.
- `README.md`: general readme.
