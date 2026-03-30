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
| AGENCY_ADMIN | Own agency — leads, users, AI Proceeding, RC lookup, reports, plan upgrades, AI Tools (PRO+), addon credits, office location settings, commission settings, attendance |
| TEAM_LEADER | Add leads, bulk upload, assign leads to telecallers, view team performance, AI Tools (PRO+), view team attendance & commissions |
| TELE_CALLER | Own assigned leads only — update status, remarks, WhatsApp, inline AI (PRO+), punch in/out attendance, view own commissions |

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
| VPS deployment | ✅ | HostBet Micro |
| Nginx + SSL | ✅ | crm.icaweb.in + icaweb.in |
| Resend email integration | ✅ | All transactional emails |
| Marketing website | ✅ | icaweb.in |
| Razorpay live payments | ✅ | Website + CRM |
| Subscription expiry system | ✅ | 30-day cycle, auto-expire |
| Subscription renewal banner | ✅ | Shows in CRM at ≤7 days/expired/trial |
| Razorpay webhook auto-activate | ✅ | Payment → expiry +30 days |
| Daily subscription cron | ✅ | PM2 fork — single instance |
| Payment History page | ✅ | MASTER_ADMIN — paginated (20/page) |
| AI Smart Remark Suggestions | ✅ | Claude Haiku — PRO + ENTERPRISE |
| AI Follow-up Message Generator | ✅ | Claude Haiku — WhatsApp + Call script |
| AI Lead Scoring | ✅ | Claude Haiku — 1-100 score + Hot/Warm/Cold |
| AI CRM Chatbot | ✅ | Claude Sonnet — ENTERPRISE only |
| Add-on packs checkout | ✅ | RC + AI top-ups on icaweb.in with Razorpay |
| Agency Business Profile | ✅ | Injected into all 4 AI tools |
| AI Suggest Remark in Update dialog | ✅ | PRO/ENT only |
| Bulk WhatsApp Messenger | ✅ | AI Tools — AGENCY_ADMIN, 50 leads |
| Mobile responsive all pages | ✅ | p-3 sm:p-6 pattern |
| PM2 fork mode | ✅ | Single instance — saves ~63MB RAM |
| Website contact form | ✅ | POST /api/contact → email via Resend |
| Tawk.to live chat | ✅ | icaweb.in widget ID: 69c62f46bf40c71c359f3fc9 |
| APLM white-label CRM | ✅ | crm.aplmsales.com — separate DB, PM2, branding |
| **Telecaller Attendance** | ✅ | GPS punch in/out, radius check, office location settings |
| **Commission System** | ✅ | Per service or agency default, triggered on CONVERTED |
| **Service Commission** | ✅ | Per-service commission amount in Services page |
| **Office Location Settings** | ✅ | Agency Admin sets GPS + radius on Attendance page |

---

## 🆕 v9.4 Features (COMPLETE)

### Telecaller Attendance
- GPS-based punch in/out via mobile browser
- Agency Admin sets office GPS + radius on Attendance page
- "Use My Current Location" button for easy setup
- Telecaller blocked from punch-in if outside radius
- Warning shown if office location not set
- Separate view per role: Telecaller (own) → TL (team) → Admin (all)
- Team Today stats: Present / Punched Out / Still Working

### Commission System
- Triggered automatically when lead status → CONVERTED
- Per-service commission set on Services page
- Agency default commission set on Commission page
- Commission logic: service amount → fallback to agency default
- Full history table per role
- Agency Admin can mark commissions as PAID
- Summary cards: Total Earned / Pending / Paid Out

### New API Endpoints (v9.4)
```
POST  /api/attendance/punch-in         → GPS punch in (radius check)
POST  /api/attendance/punch-out        → GPS punch out
GET   /api/attendance/today            → Today's record
GET   /api/attendance                  → List (role-based)
PATCH /api/agency/office-location      → Set office GPS + radius + default commission
GET   /api/agency/commission-settings  → Get agency commission + location settings
GET   /api/commissions                 → List (role-based)
PATCH /api/commissions/:id/paid        → Mark commission paid (AGENCY_ADMIN)
PATCH /api/services/:id                → Update service commission amount
```

### Commission Logic
```
Lead → CONVERTED
  → Check lead.service → find service.commission_amount
  → If > 0: use service commission
  → If = 0: use agency.commission_per_lead
  → Insert into commissions table (paidStatus: PENDING)
```

### New DB Tables
```sql
attendance  — id, agency_code, user_id, date, punch_in_at, punch_in_lat,
              punch_in_lng, punch_out_at, punch_out_lat, punch_out_lng, status
commissions — id, agency_code, user_id, lead_id, amount, paid_status,
              converted_at, paid_at
```

### New DB Columns
```sql
agencies.commission_per_lead     — Default ₹ per converted lead
agencies.office_latitude         — Office GPS latitude
agencies.office_longitude        — Office GPS longitude
agencies.office_radius_meters    — Punch-in allowed radius (default 100m)
services.commission_amount       — ₹ per converted lead for this service
```

---

## 🚀 Agency Onboarding — Complete Flow

```
Step 1 — Create Agency (MASTER_ADMIN → Agencies → Create Agency)
Step 2 — Add Admin (Agencies → Add Admin button)
Step 3 — Activate Subscription (Agencies → Activate button)
Step 4 — Share Credentials via WhatsApp
Step 5 — Agency Sets Up Team (TL + Telecallers)
Step 6 — Agency Admin sets office location (Attendance page)
Step 7 — Agency Admin sets commission per service (Services page)
Step 8 — Telecallers start punching in/out daily
```

---

## 🏢 White-Label: APLM CRM

| Item | Detail |
|------|--------|
| **CRM URL** | https://crm.aplmsales.com ✅ LIVE |
| **GitHub** | https://github.com/icassameer/aplm |
| **Working Dir** | /var/www/aplm-crm |
| **PM2** | id 8, port 5001, fork mode |
| **Database** | aplm_crm (separate) |
| **Agency Admin** | Ram_mane (Parshuram Mane) — APLM-001 |
| **Deploy** | `cd /var/www/aplm-crm && git pull origin master && npm run build && pm2 restart aplm-crm` |

---

## 🚀 Common Server Commands

```bash
ssh root@203.174.22.119
cd /var/www/ica-crm

pm2 status
pm2 logs ica-crm --lines 50

# Deploy ICA CRM
git pull origin master && npm run build && pm2 restart ica-crm

# Deploy APLM CRM (after ICA CRM is tested)
cd /var/www/aplm-crm && git pull origin master && npm run build && pm2 restart aplm-crm

# If .env changed
pm2 restart ica-crm --update-env

# DB
psql -U postgres -h localhost -d ica_crm

# Check attendance
psql -U postgres -h localhost -d ica_crm -c "SELECT * FROM attendance ORDER BY created_at DESC LIMIT 10;"

# Check commissions
psql -U postgres -h localhost -d ica_crm -c "SELECT * FROM commissions ORDER BY created_at DESC LIMIT 10;"

# Git tags
git tag -a vX.X -m "Description" && git push origin vX.X
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
| Login page | client/src/pages/login.tsx |
| Attendance page | client/src/pages/attendance.tsx |
| Commission page | client/src/pages/commission.tsx |
| Services page | client/src/pages/services.tsx |
| Leads page | client/src/pages/leads.tsx |
| AI Tools page | client/src/pages/ai-tools.tsx |
| Performance page | client/src/pages/performance.tsx |
| Sidebar nav | client/src/components/app-sidebar.tsx |
| Nginx (CRM) | /etc/nginx/sites-enabled/ica-crm |
| Marketing website | /var/www/icaweb-in/index.html |

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|---------|
| Site not loading | `pm2 restart ica-crm --update-env` |
| 502 Bad Gateway | `curl http://localhost:5000/api/auth/me` — rebuild if fails |
| Build failed | `npm run build 2>&1 \| grep ERROR` |
| Punch-in blocked | Check office location set by Agency Admin |
| GPS not working | Allow location in browser settings |
| Commission not created | Check lead has assignedTo + service set |
| Browser showing old UI | Hard refresh Ctrl+Shift+R or Incognito |
| SSL expired | `certbot renew && systemctl reload nginx` |

---

## 🏷️ Git Tags / Milestones

| Tag | Date | Description |
|-----|------|-------------|
| `v9.4` | Mar 30, 2026 | Attendance GPS punch in/out, commission system, service commission, office location settings — fully complete |
| `v9.3` | Mar 28, 2026 | Mobile responsive, PM2 fork, website contact form, Tawk.to, APLM white-label launched |
| `v9.2` | Mar 25, 2026 | AI Suggest remark, Bulk WhatsApp, In Progress stat, Follow Up sort |
| `v9.1` | Mar 21, 2026 | Agency Business Profile |
| `v8.9` | Mar 21, 2026 | Prospect email UI, email audit, scoring v2, performance page |
| `v8.0` | Mar 18, 2026 | AI Suite — 4 features + Payment History |
| `v7.0` | Mar 18, 2026 | Daily subscription cron |
| `v6.0` | Mar 17, 2026 | Subscription system + Razorpay webhook |

---

## ⏳ PENDING TASKS

| Task | Priority |
|------|----------|
| Deploy v9.4 to APLM CRM | 🔴 High |
| RC API key (Surepass) — ₹25k deposit | 🔴 High |
| Build aplmsales.com website (waiting for content) | 🟡 Medium |
| Auto-reply support@icaweb.in (ImprovMX) | 🟡 Medium |
| Verify aplmsales.com domain in Resend | 🟡 Medium |

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v9.4 | Mar 30, 2026 | Telecaller GPS attendance (punch in/out, office location settings, radius check). Commission system (per service or agency default, triggered on CONVERTED, mark as paid). Service commission amount field. Office Location Settings card on Attendance page with Use My Current Location button. All 3 roles have Attendance + Commission in sidebar. |
| v9.3 | Mar 28, 2026 | Mobile responsive all pages, PM2 fork mode, website contact form, Tawk.to live chat, ICA Team sender, APLM white-label CRM launched at crm.aplmsales.com. |
| v9.2 | Mar 25, 2026 | AI Suggest remark in Update dialog, Bulk WhatsApp, In Progress stat card, Follow Up sort, firstContactedAt. |
| v9.1 | Mar 21, 2026 | Agency Business Profile — injected into all 4 AI tools. |
| v8.0 | Mar 18, 2026 | AI Suite — Smart Remarks, Follow-up, Lead Scoring, CRM Chatbot. |
| v7.0 | Mar 18, 2026 | Daily subscription cron. |
| v6.0 | Mar 17, 2026 | Subscription expiry system, 30-day billing, Razorpay webhook. |
| v1.0 | Jan 2026 | Initial release — lead management, 4 roles, JWT auth. |

---

*Last updated: March 30, 2026 | v9.4 | Sameer | ICA — Innovation, Consulting & Automation*
