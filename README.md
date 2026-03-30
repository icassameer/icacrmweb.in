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
| **Telecaller Attendance** | ✅ | GPS punch in/out, radius check |
| **Office Location Settings** | ✅ | Admin sets GPS + radius on Attendance page |
| **Commission System** | ✅ | Auto-triggered on CONVERTED, per service or agency default |
| **Service Commission** | ✅ | Per-service amount saved on Add Service |
| **Polish with AI** | ✅ | Telecaller types remark → AI polishes it |
| **Remarks line-clamp** | ✅ | Long remarks wrap to 2 lines on lead cards |
| **Telecaller default filter** | ✅ | Leads page shows NEW by default for telecaller |

---

## 🆕 v9.4 — Complete Feature Summary

### Telecaller Attendance
- GPS punch in/out via mobile browser
- Agency Admin sets office GPS + radius (one-time setup)
- "Use My Current Location" button on Attendance page
- Telecaller blocked if outside office radius
- Warning shown if office location not set
- Role views: Telecaller (own) → TL (team) → Admin (all + settings)

### Commission System
- Auto-triggered when lead → CONVERTED
- Service commission checked first → fallback to agency default
- Full history per role with PENDING/PAID status
- Agency Admin can mark commissions as PAID
- Summary: Total Earned / Pending / Paid Out

### Polish with AI
- Telecaller types their own remark in Update Lead dialog
- Clicks "✨ Polish with AI" — AI improves grammar, tone, clarity
- Telecaller reviews and clicks "Use" to apply
- Works on PRO + ENTERPRISE plans

### Other Fixes
- Remarks on lead cards: `line-clamp-2` — wraps to 2 lines, Update button always visible
- Telecaller leads page: default filter = NEW (not ALL)
- Service commission saved correctly when adding new service
- Commission trigger fires correctly on CONVERTED status change

---

## 🚀 Agency Onboarding Flow

```
Step 1 — MASTER_ADMIN creates agency + admin
Step 2 — Activate subscription
Step 3 — Share credentials
Step 4 — Agency Admin sets office location (Attendance page — one time)
Step 5 — Agency Admin sets commission per service (Services page)
Step 6 — Agency Admin sets default commission (Commission page)
Step 7 — Team Leader adds leads → assigns to telecallers
Step 8 — Telecallers punch in daily → call leads → update status
Step 9 — On CONVERTED → commission auto-created
Step 10 — Agency Admin marks commission as PAID when paying telecaller
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
# Copy changed files
cp /var/www/ica-crm/server/storage.ts /var/www/aplm-crm/server/storage.ts
cp /var/www/ica-crm/server/routes.ts /var/www/aplm-crm/server/routes.ts
cp /var/www/ica-crm/client/src/pages/leads.tsx /var/www/aplm-crm/client/src/pages/leads.tsx
# Fix APLM sidebar branding after copying app-sidebar.tsx
# Build + restart
cd /var/www/aplm-crm && npm run build && pm2 restart aplm-crm
```

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
| Login page | client/src/pages/login.tsx |
| Leads page | client/src/pages/leads.tsx |
| Attendance page | client/src/pages/attendance.tsx |
| Commission page | client/src/pages/commission.tsx |
| Services page | client/src/pages/services.tsx |
| Sidebar nav | client/src/components/app-sidebar.tsx |
| App routes | client/src/App.tsx |
| Nginx (CRM) | /etc/nginx/sites-enabled/ica-crm |
| Marketing website | /var/www/icaweb-in/index.html |

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

---

## 🏷️ Git Tags / Milestones

| Tag | Date | Description |
|-----|------|-------------|
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
| Verify aplmsales.com domain in Resend | 🟡 Medium |
| Auto-reply support@icaweb.in (ImprovMX) | 🟡 Medium |

---

## 📋 Version History

| Version | Date | Changes |
|---------|------|---------|
| v9.4 | Mar 30, 2026 | GPS attendance (punch in/out, office location, radius check). Commission system (per service + agency default, auto-trigger on CONVERTED, mark as PAID). Polish with AI (replaces AI Suggest — telecaller types remark, AI polishes). Remarks line-clamp-2 on lead cards. Telecaller default leads filter = NEW. Service commission saved on Add Service. APLM CRM launched + all v9.4 features deployed. |
| v9.3 | Mar 28, 2026 | Mobile responsive, PM2 fork, website contact form, Tawk.to, APLM white-label launched. |
| v9.2 | Mar 25, 2026 | AI Suggest remark, Bulk WhatsApp, In Progress stat, Follow Up sort, firstContactedAt. |
| v9.1 | Mar 21, 2026 | Agency Business Profile. |
| v8.0 | Mar 18, 2026 | AI Suite — Smart Remarks, Follow-up, Lead Scoring, CRM Chatbot. |
| v7.0 | Mar 18, 2026 | Daily subscription cron. |
| v6.0 | Mar 17, 2026 | Subscription system, 30-day billing, Razorpay webhook. |
| v1.0 | Jan 2026 | Initial release — lead management, 4 roles, JWT auth. |

---

*Last updated: March 30, 2026 | v9.4 | Sameer | ICA — Innovation, Consulting & Automation*
