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
| Security | helmet.js + CORS + rate-limit + Zod validation + Fail2Ban |

---

## 👥 Roles & Access

| Role | Access |
|------|--------|
| MASTER_ADMIN | Full system — all agencies, users, plans, upgrade approvals, subscription management, payment history, activate subscriptions, send prospect emails |
| AGENCY_ADMIN | Own agency — leads, users, AI Proceeding, RC lookup, reports, plan upgrades, AI Tools (PRO+), addon credits, office location settings, commission settings, attendance |
| TEAM_LEADER | Add leads, bulk upload, assign leads to telecallers, view team performance, AI Tools (PRO+), view team attendance & commissions |
| TELE_CALLER | Own assigned leads (default filter: NEW) — update status, remarks, Polish with AI, WhatsApp, inline AI (PRO+), punch in/out attendance, view own commissions |

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
| Inline AI + Polish with AI | ❌ | ✅ | ✅ |
| AI Chatbot | ❌ | ❌ | ✅ |
| Attendance & Commission | ✅ | ✅ | ✅ |
| WhatsApp | ✅ | ✅ | ✅ |
| Automated Emails | ✅ | ✅ | ✅ |
| Subscription | 30 days/payment | 30 days/payment | 30 days/payment |

---

## ✅ COMPLETED FEATURES

| Feature | Status | Notes |
|---------|--------|-------|
| Multi-role auth (JWT) | ✅ | 4 roles |
| Lead management | ✅ | CRUD + bulk upload |
| WhatsApp click-to-chat | ✅ | |
| AI Proceeding | ✅ | GPT-4o + Whisper |
| RC Lookup UI | ✅ | API key pending |
| Plan limits enforcement | ✅ | |
| Performance reports | ✅ | |
| Audit logs | ✅ | |
| Subscription expiry system | ✅ | 30-day cycle |
| Razorpay live payments | ✅ | |
| Daily subscription cron | ✅ | PM2 fork |
| AI Smart Remarks | ✅ | Claude Haiku — PRO+ |
| AI Follow-up Generator | ✅ | Claude Haiku — PRO+ |
| AI Lead Scoring | ✅ | Claude Haiku — PRO+ |
| AI CRM Chatbot | ✅ | Claude Sonnet — ENTERPRISE |
| Add-on packs | ✅ | RC + AI top-ups |
| Agency Business Profile | ✅ | Injected into all 4 AI tools |
| Bulk WhatsApp Messenger | ✅ | AGENCY_ADMIN, 50 leads |
| Mobile responsive all pages | ✅ | p-3 sm:p-6 pattern |
| PM2 fork mode | ✅ | Single instance |
| Website contact form | ✅ | POST /api/contact |
| Tawk.to live chat | ✅ | icaweb.in |
| APLM white-label CRM | ✅ | crm.aplmsales.com LIVE |
| Telecaller Attendance | ✅ | GPS punch in/out, radius check |
| Office Location Settings | ✅ | Admin sets GPS + radius |
| Commission System | ✅ | Auto-triggered on CONVERTED |
| Service Commission | ✅ | Per-service amount saved |
| Polish with AI | ✅ | Telecaller types remark → AI polishes |
| Remarks line-clamp | ✅ | Long remarks wrap to 2 lines |
| Telecaller default filter | ✅ | Leads page shows NEW by default |
| **Circuit pulse animation** | ✅ | Login page background animation |
| **Telecaller commission summary** | ✅ | Leads page — Agency Admin view |
| **Commission page grouped view** | ✅ | Telecaller-wise + Mark All Paid |
| **Improved welcome email** | ✅ | Credentials + role onboarding steps |
| **Login renewal card** | ✅ | Shows on expired subscription login |
| **Self-service renewal** | ✅ | icaweb.in agency code field + auto-activate |
| **Secure payment flow** | ✅ | Server-side order creation, amount fixed |
| **Payment History recording** | ✅ | website-renew recorded in DB |
| **Server security hardening** | ✅ | Fail2Ban + Nginx rate limit + ports blocked |

---

## 🆕 v9.5 — Feature Summary

### Login Page — Circuit Pulse Animation
- Canvas-based circuit board animation with electricity pulses
- Blue glowing pulses travel along circuit lines with trail effect
- Replaces particle animation — more premium engineering feel
- Desktop only (mobile shows clean login)

### Telecaller Commission Summary (Leads Page)
- Agency Admin sees commission summary below stat cards
- Shows: Telecaller | Total Converted | Commission On | Total Earned | Paid | Pending
- Data pulled from commissions + leads tables (real converted count)
- Auto-updates when commissions change

### Commission Page — Telecaller-wise Grouping
- Replaced per-lead rows with per-telecaller grouped view
- Mark All Paid button — marks all pending commissions for a telecaller at once
- Total row at bottom with agency-wide summary
- Telecaller view (non-admin) still shows individual records

### Improved Welcome Email
- Now includes login credentials (username + password in red box)
- Role-specific onboarding steps (5 steps for Admin, 4 for Telecaller)
- Login to ICA CRM Now button (CTA)
- Sent for ALL roles — Agency Admin, Team Leader, Telecaller
- Subject line varies by role

### Login Renewal Card
- When expired agency user tries to login — shows renewal card instead of toast error
- Red 🔴 Subscription Expired message
- Renew Subscription Now button → icaweb.in
- WhatsApp Sameer to Renew button
- Back to Login link

### Self-Service Renewal Flow (icaweb.in)
- Agency Code field added to payment form (existing customers)
- After payment → auto-calls `/api/payments/website-renew`
- Agency auto-activated (isActive=true, +30 days expiry) immediately
- Payment recorded in Payment History with PAID status
- Payment success email sent automatically
- Amount field is readonly — server controls price, cannot be tampered

### Secure Payment — Server-side Order Creation
- New endpoint: `POST /api/payments/website-order`
- icaweb.in calls backend to create Razorpay order with fixed plan price
- User cannot change amount on frontend — Razorpay opens with server amount
- BASIC=₹2,500 / PRO=₹5,500 / ENTERPRISE=₹12,000 — all enforced server-side

### Server Security Hardening
- Port 5000 + 5001 blocked from public (Nginx proxy still works)
- Fail2Ban installed — bans IP after 5 failed SSH attempts for 24 hours
- Nginx rate limiting: login=5r/min, API=30r/min
- Applied to both ICA CRM and APLM CRM

---

## 🚀 Agency Onboarding Flow

```
Step 1 — MASTER_ADMIN creates agency + admin (welcome email auto-sent with credentials)
Step 2 — Activate subscription
Step 3 — Agency Admin logs in → changes password → sets office location
Step 4 — Agency Admin sets commission per service (Services page)
Step 5 — Agency Admin sets default commission (Commission page)
Step 6 — Team Leader adds leads → assigns to telecallers
Step 7 — Telecallers punch in daily → call leads → update status
Step 8 — On CONVERTED → commission auto-created
Step 9 — Agency Admin marks commission as PAID when paying telecaller
Step 10 — On renewal → agency pays on icaweb.in with agency code → auto-activates
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
| **Agency Admin** | Ram_mane (Parshuram Mane) — APLM-001 — ENTERPRISE |
| **Deploy cmd** | `cd /var/www/aplm-crm && git pull origin master && npm run build && pm2 restart aplm-crm` |

### Syncing ICA → APLM (after changes)
```bash
cp /var/www/ica-crm/server/storage.ts /var/www/aplm-crm/server/storage.ts
cp /var/www/ica-crm/server/routes.ts /var/www/aplm-crm/server/routes.ts
cp /var/www/ica-crm/client/src/pages/leads.tsx /var/www/aplm-crm/client/src/pages/leads.tsx
cp /var/www/ica-crm/client/src/pages/commission.tsx /var/www/aplm-crm/client/src/pages/commission.tsx
# Fix APLM sidebar branding after copying app-sidebar.tsx
cd /var/www/aplm-crm && npm run build && pm2 restart aplm-crm
```

> **DO NOT copy:** login.tsx (APLM has own logo), app-sidebar.tsx (APLM has own branding)

---

## 🔒 Security Configuration

| Protection | ICA CRM | APLM CRM |
|-----------|---------|---------|
| SSL/HTTPS | ✅ | ✅ |
| Port 5000/5001 blocked | ✅ | ✅ |
| .env / .git blocked | ✅ | ✅ |
| Login rate limit (5/min) | ✅ | ✅ |
| API rate limit (30/min) | ✅ | ✅ |
| Fail2Ban SSH protection | ✅ | ✅ (same server) |
| X-Real-IP forwarding | ✅ | ✅ |

---

## 🚀 Common Server Commands

```bash
ssh root@203.174.22.119
cd /var/www/ica-crm

pm2 status
pm2 logs ica-crm --lines 50

# Deploy ICA CRM
git pull origin master && npm run build && pm2 restart ica-crm

# If .env changed
pm2 restart ica-crm --update-env

# DB checks
psql -U postgres -h localhost -d ica_crm
psql -U postgres -h localhost -d ica_crm -c "SELECT * FROM attendance ORDER BY created_at DESC LIMIT 10;"
psql -U postgres -h localhost -d ica_crm -c "SELECT * FROM commissions ORDER BY created_at DESC LIMIT 10;"
psql -U postgres -h localhost -d ica_crm -c "SELECT name, agency_code, is_active, subscription_expiry FROM agencies;"

# Git tags
git tag -a vX.X -m "Description" && git push origin vX.X
```

---

## 📁 Key File Locations

| File | Path |
|------|------|
| Backend entry + cron | server/index.ts |
| Backend routes | server/routes.ts |
| Storage layer | server/storage.ts |
| DB schema | shared/schema.ts |
| Email templates | server/email.ts |
| Login page | client/src/pages/login.tsx |
| Leads page | client/src/pages/leads.tsx |
| Attendance page | client/src/pages/attendance.tsx |
| Commission page | client/src/pages/commission.tsx |
| Services page | client/src/pages/services.tsx |
| Sidebar nav | client/src/components/app-sidebar.tsx |
| App routes | client/src/App.tsx |
| Nginx (CRM) | /etc/nginx/sites-enabled/ica-crm |
| Nginx (APLM) | /etc/nginx/sites-enabled/aplm-crm |
| Marketing website | /var/www/icaweb-in/index.html |
| Fail2Ban config | /etc/fail2ban/jail.local |

---

## 📧 Email Triggers

| Email | When Sent | Template |
|-------|-----------|---------|
| Welcome Email | User created (all roles) | Credentials + role onboarding steps + CTA button |
| Prospect Inquiry | MASTER_ADMIN sends manually | Plan comparison + pricing |
| Password Reset | Admin resets password | New temp password |
| Plan Upgrade | Plan upgraded | New plan features |
| Payment Link | Payment link sent | Amount + pay button |
| Payment Success | Razorpay payment confirmed | Receipt + dashboard link |
| Subscription Reminder | 7 days + 1 day before expiry | WhatsApp renew link |
| Subscription Expired | On expiry day | Red header + renew button |

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|---------|
| Site not loading | `pm2 restart ica-crm --update-env` |
| 502 Bad Gateway | `curl http://localhost:5000/api/auth/me` — rebuild if fails |
| Punch-in blocked | Check office location set by Agency Admin |
| GPS not working | Allow location in browser settings |
| Commission not created | Check lead has assignedTo + CONVERTED status |
| Commission 0 | Old leads — only new CONVERTED leads trigger commission |
| Browser showing old UI | Hard refresh Ctrl+Shift+R or Incognito |
| SSL expired | `certbot renew && systemctl reload nginx` |
| APLM sidebar shows ICA | Re-apply branding after copying app-sidebar.tsx |
| Agency not auto-activating after payment | Check website-renew endpoint logs — PM2 logs |
| Payment not in history | Check razorpay_order_id unique constraint |

---

## 🏷️ Git Tags / Milestones

| Tag | Date | Description |
|-----|------|-------------|
| `v9.5` | Apr 1, 2026 | Circuit pulse login animation, commission summary on leads page, commission page telecaller grouping, improved welcome email, login renewal card, self-service renewal, secure server-side payment, payment history recording, server security hardening |
| `v9.4` | Mar 30, 2026 | Attendance GPS, commission system, service commission, office location, Polish with AI, remarks wrap, telecaller default filter NEW |
| `v9.3` | Mar 28, 2026 | Mobile responsive, PM2 fork, website contact form, Tawk.to, APLM white-label |
| `v9.2` | Mar 25, 2026 | AI Suggest remark, Bulk WhatsApp, In Progress stat, Follow Up sort |
| `v9.1` | Mar 21, 2026 | Agency Business Profile |
| `v8.0` | Mar 18, 2026 | AI Suite — 4 features + Payment History |
| `v7.0` | Mar 18, 2026 | Daily subscription cron |
| `v6.0` | Mar 17, 2026 | Subscription system + Razorpay webhook |

---

## ⏳ PENDING TASKS

| Task | Priority |
|------|----------|
| Build aplmsales.com marketing website | 🔴 High |
| RC API key (Surepass) — ₹25k deposit | 🔴 High |
| Team Leader name column in commission (needs schema) | 🟡 Medium |
| Automated DB backup (weekly) | 🟡 Medium |
| Verify aplmsales.com domain in Resend | 🟡 Medium |
| Auto-reply support@icaweb.in (ImprovMX) | 🟡 Medium |

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v9.5 | Apr 1, 2026 | Circuit pulse login animation. Telecaller commission summary on leads page (total converted + commission on). Commission page telecaller-wise grouping + Mark All Paid. Improved welcome email (credentials, role onboarding steps, CTA). Login renewal card on expired subscription. Self-service renewal from icaweb.in with agency code. Secure server-side payment order (amount fixed, cannot be tampered). Payment History recording for website payments. Server security hardening (Fail2Ban, rate limiting, ports blocked). APLM CRM synced. |
| v9.4 | Mar 30, 2026 | GPS attendance (punch in/out, office location settings, radius check). Commission system (per service + agency default, auto-trigger on CONVERTED, mark PAID). Polish with AI (replaces AI Suggest). Remarks line-clamp-2 on lead cards. Telecaller default leads filter = NEW. Service commission amount on Add Service. APLM CRM fully synced. |
| v9.3 | Mar 28, 2026 | Mobile responsive all pages. PM2 fork mode. Website contact form. Tawk.to live chat. APLM white-label CRM launched at crm.aplmsales.com. |
| v9.2 | Mar 25, 2026 | AI Suggest remark, Bulk WhatsApp, In Progress stat, Follow Up sort, firstContactedAt. |
| v9.1 | Mar 21, 2026 | Agency Business Profile. |
| v8.0 | Mar 18, 2026 | AI Suite — Smart Remarks, Follow-up, Lead Scoring, CRM Chatbot. |
| v7.0 | Mar 18, 2026 | Daily subscription cron. |
| v6.0 | Mar 17, 2026 | Subscription system, 30-day billing, Razorpay webhook. |
| v1.0 | Jan 2026 | Initial release — lead management, 4 roles, JWT auth. |

---

*Last updated: April 1, 2026 | v9.5 | Sameer | ICA — Innovation, Consulting & Automation*
