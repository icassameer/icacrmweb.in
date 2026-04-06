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
| **Plan** | Micro — 2 vCPU, 4GB RAM, 40GB NVMe + 1GB Swap |
| **Support Portal** | https://clients.hostbet.in/ |
| **Current Version** | v9.8.5 |

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
RC_API_KEY=<Surepass production key — LIVE>
RC_API_URL=https://kyc-api.surepass.io/api/v1/rc/rc-full
RAZORPAY_KEY_ID=<live key>
RAZORPAY_KEY_SECRET=<live secret>
ADDON_WEBHOOK_SECRET=<addon webhook secret from Razorpay>
SARVAM_API_KEY=<active>
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
| RC Lookup | Surepass API (LIVE — production key active) |
| Process Manager | PM2 fork mode (1 instance per app) |
| Web Server | Nginx + SSL (Let's Encrypt — auto-renew cron active) |
| Security | Fail2Ban + UFW + Nginx rate limiting + Zod + Single Session |

---

## 👥 Roles & Access

| Role | Access |
|------|--------|
| MASTER_ADMIN | Full system — all agencies, users, plans, upgrade approvals, subscription management, payment history, activate subscriptions, send prospect emails |
| AGENCY_ADMIN | Own agency — leads (all), users, AI Proceeding, RC lookup, reports, plan upgrades, AI Tools (PRO+), addon credits, office location, commission settings, attendance, assign TL to telecallers |
| TEAM_LEADER | Own team only — leads (their team), their telecallers, team performance, team attendance, team commission grouped view, assign leads |
| TELE_CALLER | Own assigned leads (default: NEW filter) — update status/remarks, Polish with AI, WhatsApp, punch in/out attendance, own commissions |

> TEAM_LEADER is the **only** role that can assign leads to telecallers.
> Each telecaller belongs to exactly **one** Team Leader — set by Agency Admin via pencil icon.
> **Single session enforcement** — new login invalidates all previous sessions.

---

## 💰 Pricing Plans (FINAL — LOCKED)

| Feature | BASIC Rs 2,500/mo | PRO Rs 5,500/mo | ENTERPRISE Rs 12,000/mo |
|---------|:-:|:-:|:-:|
| Leads | Custom | Custom | Custom |
| Users | Custom | Custom | Custom |
| AI Proceeding | No | 15/month | 40/month |
| RC Lookup | No | 50/month | 200/month |
| AI Tools | No | Yes | Yes |
| AI Chatbot | No | No | Yes |
| Attendance & Commission | Yes | Yes | Yes |
| WhatsApp | Yes | Yes | Yes |
| Subscription | 30 days | 30 days | 30 days |

---

## ✅ RC Lookup — LIVE

RC Lookup is fully live using Surepass production API.

| Item | Detail |
|------|--------|
| **API Provider** | Surepass Technologies Pvt. Ltd. |
| **Production URL** | https://kyc-api.surepass.io/api/v1/rc/rc-full |
| **Account** | ica.ssameer_152413@surepass.io |
| **Key expiry** | 2026-05-02 (sandbox token in console) |
| **Data stored** | vehicle_details, owner_details, insurance_details, tax_details, pucc_details |
| **Sort order** | Nearest insurance expiry first |
| **Cache** | 24-hour cache — same RC number won't call API again within 24h |

### Adding RC Key to new environment
```bash
echo 'RC_API_KEY=<key>' >> /var/www/<app>/.env
echo 'RC_API_URL=https://kyc-api.surepass.io/api/v1/rc/rc-full' >> /var/www/<app>/.env
pm2 restart <app> --update-env
```

---

## Performance Scoring Formula

| Metric | Weight | Description |
|--------|--------|-------------|
| Conversion Quality | 50% | PRIMARY — 0 conversions never ranks above any conversion |
| Follow-Up Discipline | 20% | % of follow-ups NOT overdue |
| Speed to Contact | 15% | Avg hours to first contact |
| Lead Coverage | 10% | % of leads moved from NEW |
| Closure Decisiveness | 5% | % marked NOT_INTERESTED |

Confidence threshold: 20 leads. Neutral baseline: 25.

---

## Agency Onboarding Flow

```
Step 1  — MASTER_ADMIN creates agency + admin (welcome email auto-sent)
Step 2  — Activate subscription
Step 3  — Agency Admin logs in, changes password, sets office GPS
Step 4  — Set commission per service (Services page)
Step 5  — Set default commission (Commission page)
Step 6  — Create Team Leaders
Step 7  — Create Telecallers, assign each to a Team Leader (pencil icon)
Step 8  — Team Leader uploads leads, assigns to telecallers
Step 9  — Telecallers punch in, call leads, update status
Step 10 — On CONVERTED, commission auto-created
Step 11 — Agency Admin marks commission as PAID
Step 12 — Renewal: pay on icaweb.in with agency code, auto-activates
```

---

## APLM White-Label CRM

| Item | Detail |
|------|--------|
| **CRM URL** | https://crm.aplmsales.com LIVE |
| **GitHub** | https://github.com/icassameer/aplm |
| **Working Dir** | /var/www/aplm-crm |
| **PM2** | id 8, port 5001, fork mode |
| **Database** | aplm_crm (separate) |
| **Agency Admin** | Ram_mane (Parshuram Mane) — APLM-001 — ENTERPRISE |
| **Team Leaders** | Rekha Ramesh Rudroj, P Mane (Pmane@aplmsales.com) |
| **Current Version** | v9.8.4 (RC Lookup sync pending) |
| **WhatsApp** | APLM Team — +91 8830242124 |

### Syncing ICA to APLM
```bash
# Always diff first before copying
diff /var/www/ica-crm/client/src/pages/<file>.tsx /var/www/aplm-crm/client/src/pages/<file>.tsx

cp /var/www/ica-crm/server/routes.ts /var/www/aplm-crm/server/routes.ts
cp /var/www/ica-crm/server/storage.ts /var/www/aplm-crm/server/storage.ts
cp /var/www/ica-crm/shared/schema.ts /var/www/aplm-crm/shared/schema.ts
cd /var/www/aplm-crm && npm run db:push && npm run build && pm2 restart aplm-crm
```

DO NOT copy: login.tsx (APLM has own logo), app-sidebar.tsx (APLM has own branding)

### APLM Pending
- Add RC_API_KEY and RC_API_URL to /var/www/aplm-crm/.env
- Sync rc-lookup.tsx from ICA
- Rebuild APLM

---

## Key Fixes & Patterns (v9.8.x)

| Fix | Detail |
|-----|--------|
| Search focus | useRef + placeholderData on leads query — prevents input losing focus |
| Follow-up date | toLocaleDateString('en-GB', {day:'numeric', month:'short', year:'numeric'}) |
| Dashboard charts | CONTACTED status excluded — 4 statuses: New, Follow Up, Converted, Not Interested |
| RC Lookup fetch | Uses raw fetch() with Bearer token — NOT apiFetch (which unwraps data.data) |
| RC data transform | Surepass raw → nested vehicle_details/owner_details/insurance_details |
| Eye toggle | All password fields — change-password.tsx and users.tsx reset dialog |
| Commission backfill | SQL: INSERT commissions JOIN services ON name+agency_code for missing CONVERTED leads |

---

## Security Configuration

| Protection | Status | Detail |
|-----------|--------|--------|
| SSL/HTTPS | Active | Auto-renew cron monthly |
| Single Session | Active | sessionToken in DB |
| Port 5000/5001/8080 | Blocked | UFW deny |
| .env / .git | Blocked | Nginx 404 |
| Login rate limit | Active | 5/min |
| API rate limit | Active | 30/min |
| Fail2Ban SSH | Active | maxretry=3, ban=24h |
| Fail2Ban Nginx | Active | maxretry=10, ban=1h |
| Swap | 1GB | OOM protection |

---

## Common Server Commands

```bash
ssh root@203.174.22.119
cd /var/www/ica-crm
pm2 status
pm2 logs ica-crm --lines 50 --nostream

# Deploy ICA CRM
git pull origin master && npm run build && pm2 restart ica-crm --update-env

# Deploy APLM CRM
cd /var/www/aplm-crm && npm run build && pm2 restart aplm-crm --update-env

# DB checks
psql -U postgres -h localhost -d ica_crm -c "SELECT name, agency_code, plan, subscription_status FROM agencies;"
psql -U postgres -h localhost -d aplm_crm -c "SELECT name, agency_code, plan, subscription_status FROM agencies;"

# Fix TL leads after assignment (one-time)
psql -U postgres -h localhost -d ica_crm -c "UPDATE leads SET team_leader_id = users.team_leader_id FROM users WHERE leads.assigned_to = users.id AND users.team_leader_id IS NOT NULL;"

# Backfill missing commissions
psql -U postgres -h localhost -d aplm_crm -c "INSERT INTO commissions (agency_code, user_id, lead_id, amount, paid_status) SELECT l.agency_code, l.assigned_to, l.id, s.commission_amount, 'PENDING' FROM leads l JOIN services s ON s.name = l.service AND s.agency_code = l.agency_code WHERE l.status = 'CONVERTED' AND l.id NOT IN (SELECT lead_id FROM commissions WHERE agency_code = 'APLM-001') AND l.service IS NOT NULL;"

# Git tags
git tag -a vX.X.X -m "Description" && git push origin vX.X.X
```

---

## Key File Locations

| File | Path |
|------|------|
| Backend entry + cron | server/index.ts |
| Backend routes | server/routes.ts |
| Storage layer | server/storage.ts |
| DB schema | shared/schema.ts |
| Email templates | server/email.ts |
| Login page | client/src/pages/login.tsx |
| Leads page | client/src/pages/leads.tsx |
| Dashboard | client/src/pages/dashboard.tsx |
| RC Lookup | client/src/pages/rc-lookup.tsx |
| Attendance page | client/src/pages/attendance.tsx |
| Commission page | client/src/pages/commission.tsx |
| Change Password | client/src/pages/change-password.tsx |
| Services page | client/src/pages/services.tsx |
| Users page | client/src/pages/users.tsx |
| Reports page | client/src/pages/reports.tsx |
| Nginx (CRM) | /etc/nginx/sites-enabled/ica-crm |
| Nginx (APLM) | /etc/nginx/sites-enabled/aplm-crm |
| Marketing website | /var/www/icaweb-in/index.html |
| Fail2Ban config | /etc/fail2ban/jail.d/custom.conf |

---

## Troubleshooting

| Problem | Solution |
|---------|---------|
| Site not loading | pm2 restart ica-crm --update-env |
| 502 Bad Gateway | curl http://localhost:5000/api/auth/me — rebuild if fails |
| TL sees no leads | UPDATE leads SET team_leader_id = users.team_leader_id FROM users WHERE leads.assigned_to = users.id AND users.team_leader_id IS NOT NULL |
| RC Lookup not working | Check RC_API_KEY + RC_API_URL in .env then pm2 restart ica-crm --update-env |
| RC shows old data | 24h cache — delete from rc_records table to force fresh lookup |
| Session expired | Normal — user logged in elsewhere. Re-login required. |
| Punch-in blocked | Check office location set by Agency Admin |
| Commission not created | Check lead has assignedTo + CONVERTED status + service assigned |
| Browser showing old UI | Hard refresh Ctrl+Shift+R or Incognito |
| SSL expired | certbot renew && systemctl reload nginx |
| Build fails | rm -rf dist && npm run build |

---

## Git Tags

| Tag | Date | Description |
|-----|------|-------------|
| `v9.8.5` | Apr 6, 2026 | RC Lookup LIVE — Surepass production API, persistence fix |
| `v9.8.4` | Apr 6, 2026 | Dashboard chart fix — remove CONTACTED/In Progress, 4 clean statuses |
| `v9.8.3` | Apr 6, 2026 | RC lookup response transform, sort by insurance expiry |
| `v9.8.2` | Apr 6, 2026 | Eye toggle on reset/change password, APLM WhatsApp branding |
| `v9.8.1` | Apr 3, 2026 | Search focus fix, follow-up date format, APLM favicon+title |
| `v9.8` | Apr 2, 2026 | Attendance redesign, feature showcase on icaweb.in, demo agency seeded |
| `v9.7` | Apr 1, 2026 | teamLeaderId schema, TL team isolation, edit TL UI, scoring fix |
| `v9.6` | Apr 1, 2026 | Lead report TL+TC columns, single session, security hardening |
| `v9.5` | Apr 1, 2026 | Circuit pulse, commission summary, renewal card, secure payment |
| `v9.4` | Mar 30, 2026 | GPS attendance, commission system, Polish with AI |
| `v9.3` | Mar 28, 2026 | Mobile responsive, PM2 fork, APLM white-label |
| `v9.2` | Mar 25, 2026 | AI Suggest, Bulk WhatsApp, In Progress stat |
| `v9.1` | Mar 21, 2026 | Agency Business Profile |
| `v8.0` | Mar 18, 2026 | AI Suite, Payment History |
| `v7.0` | Mar 18, 2026 | Daily subscription cron |
| `v6.0` | Mar 17, 2026 | Subscription system, Razorpay webhook |

---

## Pending Tasks

| Task | Priority |
|------|----------|
| Sync RC Lookup to APLM (rc-lookup.tsx + .env keys) | HIGH |
| Build aplmsales.com marketing website | HIGH |
| Automated weekly DB backup | MEDIUM |
| Verify aplmsales.com domain in Resend | MEDIUM |
| Auto-reply support@icaweb.in (ImprovMX) | MEDIUM |
| Sarvam Batch API upgrade (60-min files + diarization) | LOW |

---

## Demo Agency Credentials (ICA-N9ZYQZ)

| Role | Username | Password |
|------|----------|----------|
| Agency Admin | Sam | existing |
| Team Leader 1 | rahul.sharma | Demo@1234 |
| Team Leader 2 | priya.verma | Demo@1234 |
| Telecaller 1-4 | amit.kumar, sunita.patil, ravi.desai, meena.joshi | Demo@1234 |
| Telecaller 5-8 | vijay.singh, kavita.rao, deepak.nair, anjali.mehta | Demo@1234 |

---

*Last updated: April 6, 2026 | v9.8.5 | Sameer Bagwan | ICA — Innovation, Consulting & Automation*
