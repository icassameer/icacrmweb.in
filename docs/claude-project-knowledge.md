# ICA CRM (icacrmweb): Project Knowledge

Last updated: 2026-10-19. This file mirrors Claude Code's workspace memory on the VPS. It contains no secrets.

## Product
- ICA CRM is a multi-tenant SaaS CRM for agencies, live at https://crm.icaweb.in. The marketing site is https://icaweb.in, and pricing is at icaweb.in/#pricing.
- Owner/operator: Sameer, ICA (Innovation, Consulting & Automation). GitHub repo: icassameer/icacrmweb.in, branch `master`.

## Stack
- Frontend: React 18, Vite 7, wouter, TanStack Query (`client/src`).
- Backend: Express 5. The main API file is `server/routes.ts`, and the cron lives in `server/index.ts`.
- Data: Drizzle ORM on PostgreSQL 16, database `ica_crm`. The schema is in `shared/schema.ts`.
- Integrations: Razorpay (subscriptions and add-on payments via webhooks), OpenAI, Sarvam, Anthropic, Resend email, and an external RC vehicle-registration lookup API.

## Domain model
- **Tenancy:** everything is keyed by `agency_code`, which looks like `ICA-XXXXXX` and contains a hyphen. Users link to agencies by `agency_code`; there is no `agency_id`.
- **Roles:** MASTER_ADMIN (platform owner), AGENCY_ADMIN, TEAM_LEADER, TELE_CALLER.
- **Plans:** BASIC, PRO and ENTERPRISE. RC lookups are limited to 0, 50 and 200 per month respectively.
- **Subscription status:** TRIAL, ACTIVE, EXPIRED or SUSPENDED. It is stored on the agency in `subscription_status`, `subscription_expiry` and `is_active`.
- **Lead statuses:** NEW, CONTACTED, FOLLOW_UP, CONVERTED, NOT_INTERESTED, RENEWAL. A lead moves from CONVERTED to RENEWAL automatically after 10 months.
- **Modules:** leads, users and approvals, dashboard, attendance, meetings, commissions, payments, reports, services, RC lookup and records, upgrade requests, add-on credits, audit logs, notifications, subscription.
- **Auth:** a 24-hour JWT plus a per-user session token, so each user has one active session. Endpoints are guarded by role and by plan.

## Hosting and deploy
- One VPS at 203.174.22.119, app folder `/var/www/ica-crm`. nginx handles TLS and proxies to PM2 process `ica-crm` on port 5000.
- The same server also runs `aplm-crm` (port 5001), `ica-pulse-api` (FastAPI) and PostgreSQL.
- To deploy: back up `dist/`, run `npm run build`, then `pm2 restart ica-crm`.
- `deploy.sh` is out of date. It pulls `main` instead of `master`, and it uses cluster mode, which doesn't match how the app runs now.
- The SSL certificates expire around 2026-12-03.

## Operations log
| Date | Event |
|---|---|
| 2026-10-19 | Fixed `/api/addons/balance`. Its validation rejected hyphenated agency codes, so the add-on balance never loaded. It now accepts them, requires login, and only returns the user's own agency. Deployed, committed and pushed. |
| 2026-10-19 | Server now pushes to GitHub with an SSH deploy key. The plain-text token was removed from the git config, and the 11 unpushed commits are now on GitHub. |
| 2026-10-19 | Deployed the Subscription Expired screen change: the Agency Code box always shows, with "N/A" when there is no code. |
| 2026-10-19 | Extended the subscription for agency ICA-N9ZYQZ (admin user Sam) by 365 days. Status is ACTIVE until 2027-10-19 and an audit log entry was written. It had been expired since 2026-07-27. |
| 2026-10-19 | Health check: site, APIs, database and cron all OK. This is the only agency in the database, and the last lead activity was on 2026-05-21. |

## Open follow-ups
- [ ] Revoke the old GitHub personal access token on GitHub. The server now uses an SSH deploy key instead.
- [ ] Return 400 instead of logging an error for bot-noise requests: malformed URLs, CORS rejections and bad JSON.
- [ ] Update `deploy.sh` to use `master` and the fork-mode PM2 setup.
- [ ] Confirm that SSL auto-renewal is set up before 2026-12-03.
