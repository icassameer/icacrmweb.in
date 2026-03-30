# ICA CRM — Enterprise Lead Management System
> Innovation, Consulting & Automation | Support: +91 99679 69850 | support@icaweb.in

---

## 📋 PROJECT BLUEPRINT
*This is the single source of truth. Share this file at the start of any new session to resume work instantly.*

---

## 🔗 Quick Reference

| Item | Detail |
|------|--------|
| **Live URL** | https://crm.icaweb.in |
| **Marketing Site** | https://icaweb.in |
| **GitHub** | https://github.com/icassameer/icacrmweb.in |
| **Branch** | `master` |
| **Server IP** | 203.174.22.119 |
| **Server Name** | crmicawebin (HostBet) |
| **SSH** | `ssh root@203.174.22.119` (port 22) |
| **Root Password** | Icacrm@321 |
| **Working Dir** | /var/www/ica-crm |
| **Website Dir** | /var/www/icaweb-in |
| **OS** | Ubuntu 24.04 LTS |
| **Plan** | Micro — 2 vCPU, 4GB RAM, 40GB NVMe |
| **Support Portal** | https://clients.hostbet.in/ |
| **VS Code SSH** | Remote-SSH extension → Host: ICA-CRM → 203.174.22.119 |

---

## 🗄️ Database

| Item | Detail |
|------|--------|
| **Engine** | PostgreSQL 16 |
| **Database** | ica_crm |
| **User** | postgres |
| **Password** | Admin@1234 |
| **URL** | postgresql://postgres:Admin@1234@localhost:5432/ica_crm |
| **ORM** | Drizzle ORM |

---

## ⚙️ Server .env

```
SESSION_SECRET=IcaCrm@SecretKey2024@Sameer@321@ICA@CRM@SECURE
DATABASE_URL=postgresql://postgres:Admin@1234@localhost:5432/ica_crm
OPENAI_API_KEY=<real key added>
ANTHROPIC_API_KEY=<real key added — Claude Haiku + Sonnet>
NODE_ENV=production
ALLOWED_ORIGINS=https://crm.icaweb.in,https://icaweb.in,https://www.icaweb.in
RESEND_API_KEY=<active — domain icaweb.in verified>
FROM_EMAIL=support@icaweb.in
FROM_NAME=ICA Team
RC_API_KEY=<pending — Surepass>
RAZORPAY_KEY_ID=<live key>
RAZORPAY_KEY_SECRET=<live secret>
ADDON_WEBHOOK_SECRET=<addon webhook secret from Razorpay>
```

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 + Vite + TailwindCSS + Shadcn UI |
| Backend | Express.js 5 + TypeScript |
| Database | PostgreSQL 16 + Drizzle ORM |
| AI Transcription | OpenAI Whisper + GPT-4o (AI Proceeding) |
| AI Suite | Anthropic Claude — Haiku (scoring/remarks) + Sonnet (chatbot) |
| Email | Resend API — domain icaweb.in (Verified) |
| Payments | Razorpay (live) — UPI, Cards, NetBanking, Wallets, EMI |
| Process Manager | PM2 fork mode (1 instance) |
| Web Server | Nginx + SSL (Let's Encrypt) |
| Security | helmet.js + CORS + rate-limit + Zod validation |

---

## 👥 Roles & Access

| Role | Access |
|------|--------|
| MASTER_ADMIN | Full system — all agencies, users, plans, upgrade approvals, subscription management, payment history, activate subscriptions, send prospect emails |
| AGENCY_ADMIN | Own agency — leads, users, AI Proceeding, RC lookup, reports, plan upgrades, AI Tools (PRO+), addon credits, office location settings, commission settings |
| TEAM_LEADER | Add leads, bulk upload, assign leads to telecallers (select all on page), view team performance, AI Tools (PRO+), view team attendance & commissions |
| TELE_CALLER | Own assigned leads only — update status, remarks, WhatsApp, inline AI buttons (PRO+), punch in/out attendance, view own commissions |

> TEAM_LEADER is the **only** role that can assign leads to telecallers.

---

## 💰 Pricing Plans (FINAL — LOCKED)

| Feature | BASIC ₹2,500/mo | PRO ₹5,500/mo | ENTERPRISE ₹12,000/mo |
|---------|:-:|:-:|:-:|
| Leads | Custom (set by admin) | Custom (set by admin) | Custom (set by admin) |
| Users | Custom (set by admin) | Custom (set by admin) | Custom (set by admin) |
| AI Proceeding | ❌ | 15/month | 40/month |
| RC Lookup | ❌ | 50/month | 200/month |
| AI Tools (Remarks + Follow-up + Scoring) | ❌ | ✅ | ✅ |
| Inline AI on Lead Cards | ❌ | ✅ | ✅ |
| AI Chatbot | ❌ | ❌ | ✅ |
| Attendance & Commission | ✅ | ✅ | ✅ |
| WhatsApp | ✅ | ✅ | ✅ |
| Automated Emails | ✅ | ✅ | ✅ |
| Subscription | 30 days/payment | 30 days/payment | 30 days/payment |

### Add-on Packs (Live on icaweb.in)

| Pack | Credits | Price |
|------|---------|-------|
| RC Small | 10 RC Lookups | ₹99 |
| RC Large | 25 RC Lookups | ₹199 |
| AI Small | 5 AI Proceedings | ₹199 |
| AI Large | 15 AI Proceedings | ₹499 |

---

## ✅ COMPLETED FEATURES

| Feature | Status | Notes |
|---------|--------|-------|
| Multi-role auth (JWT) | ✅ | 4 roles |
| Lead management | ✅ | CRUD + bulk upload |
| WhatsApp click-to-chat | ✅ | |
| AI Proceeding | ✅ | GPT-4o + Whisper background processing |
| Multilingual transcription | ✅ | Hindi/Marathi/English |
| RC Lookup UI | ✅ | API key pending |
| Plan limits enforcement | ✅ | Leads, users, AI, RC per plan |
| Performance reports | ✅ | |
| Audit logs | ✅ | |
| DB-backed job processing | ✅ | PM2 fork safe |
| VPS deployment | ✅ | HostBet Micro |
| Nginx + SSL | ✅ | crm.icaweb.in + icaweb.in |
| Resend email integration | ✅ | All transactional emails |
| Marketing website | ✅ | icaweb.in |
| Privacy policy page | ✅ | icaweb.in/privacy-policy |
| Razorpay live payments | ✅ | Website + CRM |
| Edit agency limits | ✅ | MASTER_ADMIN per agency |
| Subscription expiry system | ✅ | 30-day cycle, auto-expire |
| Subscription renewal banner | ✅ | Shows in CRM at ≤7 days/expired/trial |
| Razorpay webhook auto-activate | ✅ | Payment → expiry +30 days |
| Manual extend (MASTER_ADMIN) | ✅ | POST /api/subscription/extend |
| Subscription emails | ✅ | Confirmation, reminder, expired |
| Daily subscription cron | ✅ | PM2 fork — single instance |
| Payment History page | ✅ | MASTER_ADMIN — paginated (20/page) |
| AI Smart Remark Suggestions | ✅ | Claude Haiku — PRO + ENTERPRISE |
| AI Follow-up Message Generator | ✅ | Claude Haiku — WhatsApp + Call script |
| AI Lead Scoring | ✅ | Claude Haiku — 1-100 score + Hot/Warm/Cold |
| AI CRM Chatbot | ✅ | Claude Sonnet — ENTERPRISE only |
| AI Tools page | ✅ | /ai-tools — all roles |
| Inline AI buttons on lead cards | ✅ | ✨ sparkle button — TELE_CALLER + TEAM_LEADER |
| Add-on packs checkout | ✅ | RC + AI top-ups on icaweb.in with Razorpay |
| Add-on credit balance in CRM | ✅ | Plan & Upgrade page with Buy more link |
| Activate subscription button | ✅ | Agencies page — no SQL needed |
| Smart telecaller scoring v2 | ✅ | 5-metric formula with confidence damping |
| Performance page redesign | ✅ | Hero card, 5 metric cards, radar chart |
| Agencies pagination | ✅ | 20/page — ready for 500+ agencies |
| Payments pagination | ✅ | 20/page — ready for 1000+ payments |
| ProcessingJobs 7-day cleanup | ✅ | Auto-cleanup in cron |
| Select all on page (leads) | ✅ | Team Leader bulk assign — current page checkbox |
| Send Prospect Email UI | ✅ | MASTER_ADMIN → Agencies → Send Prospect Email |
| Email templates audit | ✅ | Correct pricing, features, add-ons in all emails |
| Agency Business Profile | ✅ | Company profile + services stored per agency — injected into all 4 AI tools |
| AI Suggest Remark in Update dialog | ✅ | ✨ button in Update Lead popup — status-aware, one-click Use — PRO/ENT only |
| Bulk WhatsApp Messenger | ✅ | AI Tools page — AGENCY_ADMIN, 50 leads, AI polish, status filter, select all, one-by-one |
| In Progress stat card | ✅ | Replaces Contacted — shows all touched leads |
| Follow Up date sort | ✅ | Leads sorted by nearest follow-up date when Follow Up filter active |
| firstContactedAt timestamp | ✅ | New DB column — accurate speed-to-contact scoring |
| Mobile responsive all pages | ✅ | p-3 sm:p-6 pattern — desktop layout unchanged |
| PM2 fork mode | ✅ | Single instance — saves ~63MB RAM vs cluster |
| Website contact form | ✅ | POST /api/contact → email via Resend |
| Tawk.to live chat | ✅ | icaweb.in widget ID: 69c62f46bf40c71c359f3fc9 |
| APLM white-label CRM | ✅ | crm.aplmsales.com — separate DB, PM2, branding |
| **v9.4 DB Schema** | ✅ | attendance + commissions tables, service commission, office location |

---

## 🆕 v9.4 Features (DB Schema Done — UI In Progress)

### Telecaller Attendance
- GPS-based punch in/out via mobile browser
- Agency Admin sets office coordinates + allowed radius (meters)
- Telecaller blocked from punching in if outside radius
- Separate page per role: Telecaller (own) → TL (team) → Admin (all)

### Commission System
- Triggered on lead status = CONVERTED
- Commission amount set per service by Agency Admin
- Fallback to agency-level default if service has no commission set
- Separate Commission page with full history per role

### DB Changes (v9.4)
```sql
-- agencies table (new columns)
commission_per_lead     INTEGER DEFAULT 0       -- ₹ default per converted lead
office_latitude         TEXT                    -- Office GPS lat
office_longitude        TEXT                    -- Office GPS lng  
office_radius_meters    INTEGER DEFAULT 100     -- Punch-in allowed radius

-- services table (new column)
commission_amount       INTEGER DEFAULT 0       -- ₹ per converted lead for this service

-- New table: attendance
id, agency_code, user_id, date (YYYY-MM-DD)
punch_in_at, punch_in_lat, punch_in_lng
punch_out_at, punch_out_lat, punch_out_lng
status (PRESENT | HALF_DAY | ABSENT)

-- New table: commissions
id, agency_code, user_id, lead_id
amount, paid_status (PENDING | PAID)
converted_at, paid_at
```

### Commission Logic
```
Lead status → CONVERTED
      ↓
Check lead.service → find service.commission_amount
      ↓
If commission_amount > 0 → use it
If commission_amount = 0 → use agency.commission_per_lead
      ↓
Insert into commissions table
```

---

## 🚀 Agency Onboarding — Complete Flow (No SQL Required)

```
Step 1 — Create Agency
MASTER_ADMIN → Agencies → Create Agency
Enter name → agencyCode auto-generated → set plan + limits

Step 2 — Add Admin
Agencies page → Add Admin button
Enter: name, email, username, password
→ Welcome email sent automatically

Step 3 — Activate Subscription
Agencies page → Activate button (green)
Select plan + days (7/15/30/60/90) → Activate Subscription
→ Done instantly — no SQL needed!

Step 4 — Share Credentials
Send via WhatsApp:
- URL: https://crm.icaweb.in
- Username + Password
- Agency Code: ICA-XXXXXX

Step 5 — Agency Sets Up Team
AGENCY_ADMIN → Creates TEAM_LEADER + TELE_CALLER
AGENCY_ADMIN → Sets office location + commission per service
TEAM_LEADER → Adds leads → Assigns to telecallers
TELE_CALLER → Calls leads → Punches in/out → Uses AI tools
```

---

## 🤖 AI Suite

### API Endpoints
```
POST /api/ai/suggest-remark     → Smart remark (Haiku) — uses agency business profile
POST /api/ai/followup-message   → WhatsApp / call script (Haiku) — uses agency business profile
POST /api/ai/score-lead         → Lead score 1-100 (Haiku) — weights by agency focus area
POST /api/ai/chat               → CRM assistant with live data (Sonnet) — knows agency business
GET  /api/agency/profile        → Get own agency business profile (AGENCY_ADMIN)
PATCH /api/agency/profile       → Update own agency business profile (AGENCY_ADMIN)
```

---

## 🏢 Agency Business Profile

Each agency stores a business profile used by all AI tools.

| Field | Description |
|-------|-------------|
| Company Profile | Description of agency, location, target customers |
| Products / Services | Comma-separated insurance products sold |

---

## 📊 Telecaller Scoring Formula v2

```
Score = (Conversion Quality    × 35%)
      + (Speed to Contact      × 25%)
      + (Follow-Up Discipline  × 20%)
      + (Lead Coverage         × 15%)
      + (Closure Decisiveness  × 5%)

Confidence damping: < 5 leads → score blended toward neutral 40%
```

---

## 🔄 Subscription Lifecycle

```
Customer pays → Razorpay webhook → expiry + 30 days
Day 23 → 7-day reminder email
Day 29 → 1-day urgent reminder
Day 30 → expired → banner in CRM
cron → daysLeft ≤ 0 → EXPIRED → send expired email
Customer pays → webhook → +30 more days
```

---

## ⏱️ Daily Cron (PM2 Fork)

- Lives in `server/index.ts`
- Fires 10s after startup then every 24h
- No instance guard needed (fork mode = single instance)

```bash
pm2 logs ica-crm --lines 10
# [cron] Subscription cron registered on primary instance
# [cron] Subscription cron done — X agencies checked
# [cron] Job cleanup done — old completed/failed jobs removed
```

---

## 📧 Email Triggers (Resend)

| Email | Trigger | Function |
|-------|---------|----------|
| Welcome | New agency admin created | `sendWelcomeEmail` |
| Prospect Inquiry | MASTER_ADMIN → Agencies → Send Prospect Email | `sendProspectEmail` |
| Plan Upgrade | MASTER_ADMIN approves upgrade | `sendPlanUpgradeEmail` |
| Payment Confirmation | Webhook payment.captured | `sendPaymentSuccessEmail` |
| 7-day Reminder | Daily cron — daysLeft === 7 | `sendSubscriptionReminderEmail` |
| 1-day Reminder | Daily cron — daysLeft === 1 | `sendSubscriptionReminderEmail` |
| Plan Expired | Daily cron — daysLeft ≤ 0 | `sendSubscriptionExpiredEmail` |

---

## 🚀 Common Server Commands

```bash
ssh root@203.174.22.119
cd /var/www/ica-crm

pm2 status
pm2 logs ica-crm --lines 50

# Deploy
git pull origin master && npm run build && pm2 restart ica-crm

# If .env changed
pm2 restart ica-crm --update-env

# DB
psql -U postgres -h localhost -d ica_crm

# Check subscriptions
psql -U postgres -h localhost -d ica_crm -c \
  "SELECT name, plan, subscription_status, subscription_expiry FROM agencies;"

# Check addon credits
psql -U postgres -h localhost -d ica_crm -c \
  "SELECT name, agency_code, rc_addon_credits, ai_addon_credits FROM agencies;"

# Git tags / milestones
git tag -a vX.X -m "Description" && git push origin vX.X

# Rollback to a tag
git checkout vX.X && npm run build && pm2 restart ica-crm

# Return to latest
git checkout master && npm run build && pm2 restart ica-crm
```

---

## 📁 Key File Locations

| File | Path |
|------|------|
| Backend entry + cron | server/index.ts |
| Backend routes | server/routes.ts |
| Email functions | server/email.ts |
| DB schema | shared/schema.ts |
| Storage layer | server/storage.ts |
| Main app layout | client/src/App.tsx |
| Agencies page | client/src/pages/agencies.tsx |
| Leads page | client/src/pages/leads.tsx |
| AI Tools page | client/src/pages/ai-tools.tsx |
| Payment History page | client/src/pages/payment-history.tsx |
| Performance page | client/src/pages/performance.tsx |
| Agency Business Profile page | client/src/pages/agency-profile.tsx |
| Plan & Upgrade page | client/src/pages/upgrade-requests.tsx |
| Sidebar nav | client/src/components/app-sidebar.tsx |
| Subscription banner | client/src/components/SubscriptionBanner.tsx |
| Nginx (CRM) | /etc/nginx/sites-enabled/ica-crm |
| Marketing website | /var/www/icaweb-in/index.html |
| Privacy policy | /var/www/icaweb-in/privacy-policy.html |

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|---------|
| Site not loading | `pm2 restart ica-crm --update-env` |
| 502 Bad Gateway | `curl http://localhost:5000/api/auth/me` — if fails: `npm run build && pm2 restart ica-crm` |
| Build failed | `npm run build 2>&1 \| grep ERROR` |
| Subscription not activating | Check RAZORPAY_KEY_SECRET in .env |
| Emails not sending | Check RESEND_API_KEY in .env |
| AI returns 403 | Agency on BASIC plan |
| AI chatbot 403 | ENTERPRISE plan required |
| AI service error 500 | Check ANTHROPIC_API_KEY in .env |
| Addon credits not added | Check ADDON_WEBHOOK_SECRET in .env |
| SSL expired | `certbot renew && systemctl reload nginx` |
| Leads page blank | Hard refresh (Ctrl+Shift+R) — likely JS cache |
| Browser showing old UI | Hard refresh Ctrl+Shift+R or open Incognito |

---

## 🏷️ Git Tags / Milestones

| Tag | Date | Description |
|-----|------|-------------|
| `v9.4` | Mar 30, 2026 | DB schema — attendance, commissions, service commission, office location (UI in progress) |
| `v9.3` | Mar 28, 2026 | Mobile responsive all pages, PM2 fork, website contact form, Tawk.to, ICA Team sender |
| `v9.2` | Mar 25, 2026 | AI Suggest remark, Bulk WhatsApp, In Progress stat, Follow Up sort, firstContactedAt |
| `v9.1` | Mar 21, 2026 | Agency Business Profile |
| `v8.9` | Mar 21, 2026 | Prospect email UI, email audit, scoring v2, performance page, pagination, cron dedup |
| `v8.5` | Mar 21, 2026 | Smart telecaller scoring v2, Performance page redesign, PM2 cron dedup fix |
| `v8.4` | Mar 19, 2026 | Activate subscription button on Agencies page |
| `v8.2` | Mar 19, 2026 | Add-on packs backend + icaweb.in checkout |
| `v8.0` | Mar 18, 2026 | AI Suite — 4 features + Payment History |
| `v7.0` | Mar 18, 2026 | Daily subscription cron |
| `v6.0` | Mar 17, 2026 | Subscription system + Razorpay webhook |

---

## ⏳ PENDING TASKS

| Task | Priority |
|------|----------|
| v9.4 — Attendance UI (punch in/out page per role) | 🔴 High |
| v9.4 — Commission UI (settings + history page per role) | 🔴 High |
| v9.4 — Commission trigger on CONVERTED lead | 🔴 High |
| RC API key (Surepass) — ₹25k deposit | 🔴 High |
| APLM website — aplmsales.com (waiting for content) | 🟡 Medium |
| Auto-reply support@icaweb.in (ImprovMX) | 🟡 Medium |
| Verify aplmsales.com domain in Resend | 🟡 Medium |

---

## 🏢 White-Label: APLM CRM

| Item | Detail |
|------|--------|
| **CRM URL** | https://crm.aplmsales.com ✅ LIVE |
| **GitHub** | https://github.com/icassameer/aplm |
| **Working Dir** | /var/www/aplm-crm |
| **PM2** | id 8, port 5001, fork mode |
| **Database** | aplm_crm (separate) |
| **Agency Admin** | Ram_mane (Parshuram Mane) |
| **Deploy** | `cd /var/www/aplm-crm && git pull origin master && npm run build && pm2 restart aplm-crm` |

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v9.4 | Mar 30, 2026 | DB schema for attendance (GPS punch in/out) + commissions (per service/converted lead) + office location on agencies + commissionAmount on services. UI pending. |
| v9.3 | Mar 28, 2026 | Mobile responsive all pages, PM2 single instance fork, website contact form email, Tawk.to live chat, ICA Team sender name, icaweb.in URL fixes. APLM white-label CRM launched. |
| v9.2 | Mar 25, 2026 | AI Suggest remark in Update dialog, Bulk WhatsApp in AI Tools, In Progress stat card, Follow Up sort, firstContactedAt scoring. |
| v9.1 | Mar 21, 2026 | Agency Business Profile — injected into all 4 AI tools. |
| v9.0 | Mar 21, 2026 | Full SOP documentation of all features up to v8.9. |
| v8.9 | Mar 21, 2026 | Send Prospect Email UI, email audit fixes, scoring v2, performance page, pagination, cron dedup. |
| v8.0 | Mar 18, 2026 | AI Suite — Smart Remarks, Follow-up, Lead Scoring, CRM Chatbot. Payment History. |
| v7.0 | Mar 18, 2026 | Daily subscription cron. |
| v6.0 | Mar 17, 2026 | Subscription expiry system, 30-day billing, Razorpay webhook. |
| v1.0 | Jan 2026 | Initial release — lead management, 4 roles, JWT auth. |

---

*Last updated: March 30, 2026 | v9.4 | Sameer | ICA — Innovation, Consulting & Automation*
