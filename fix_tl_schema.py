# ── PATCH 1: shared/schema.ts ─────────────────────────────────────────────────
filepath = "/var/www/ica-crm/shared/schema.ts"
with open(filepath, "r") as f:
    content = f.read()

errors = []

# 1a. Add teamLeaderId to users table
OLD1 = '  sessionToken: text("session_token"),\n  createdAt: timestamp("created_at").defaultNow(),'
NEW1 = '  sessionToken: text("session_token"),\n  teamLeaderId: text("team_leader_id"),  // Only set for TELE_CALLER\n  createdAt: timestamp("created_at").defaultNow(),'
if 'teamLeaderId: text("team_leader_id")' in content:
    print("Schema users: teamLeaderId already exists")
elif OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print("Step 1a OK: teamLeaderId added to users table")
else:
    errors.append("Step 1a: sessionToken line not found in users table")

# 1b. Add teamLeaderId to leads table
OLD2 = '  createdBy: text("created_by"),\n  createdAt: timestamp("created_at").defaultNow(),'
NEW2 = '  createdBy: text("created_by"),\n  teamLeaderId: text("team_leader_id"),  // Set when TL assigns lead\n  createdAt: timestamp("created_at").defaultNow(),'
if 'teamLeaderId: text("team_leader_id")' in content and 'leads = pgTable' in content:
    # check if it's in leads specifically
    leads_section = content[content.index('export const leads = pgTable'):content.index('export const auditLogs')]
    if 'teamLeaderId' in leads_section:
        print("Schema leads: teamLeaderId already exists")
    elif OLD2 in content:
        content = content.replace(OLD2, NEW2)
        print("Step 1b OK: teamLeaderId added to leads table")
    else:
        errors.append("Step 1b: createdBy line not found in leads table")
elif OLD2 in content:
    content = content.replace(OLD2, NEW2)
    print("Step 1b OK: teamLeaderId added to leads table")
else:
    errors.append("Step 1b: createdBy line not found in leads table")

# 1c. Add index on leads teamLeaderId
OLD3 = '  index("leads_service_idx").on(table.service),\n]);'
NEW3 = '  index("leads_service_idx").on(table.service),\n  index("leads_tl_idx").on(table.teamLeaderId),\n]);'
if 'leads_tl_idx' in content:
    print("Schema leads index: already exists")
elif OLD3 in content:
    content = content.replace(OLD3, NEW3)
    print("Step 1c OK: leads_tl_idx added")
else:
    errors.append("Step 1c: leads_service_idx closing not found")

if errors:
    print("ERRORS:", errors)
    exit(1)

with open(filepath, "w") as f:
    f.write(content)
print("schema.ts patched successfully")
