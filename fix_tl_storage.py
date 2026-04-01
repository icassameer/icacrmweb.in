# ── PATCH 2: server/storage.ts ────────────────────────────────────────────────
filepath = "/var/www/ica-crm/server/storage.ts"
with open(filepath, "r") as f:
    content = f.read()

errors = []

# 2a. Add getTelecallersByTeamLeader to interface
OLD1 = '  getTelecallersByAgency(agencyCode: string): Promise<User[]>;'
NEW1 = '  getTelecallersByAgency(agencyCode: string): Promise<User[]>;\n  getTelecallersByTeamLeader(teamLeaderId: string): Promise<User[]>;'
if 'getTelecallersByTeamLeader' in content:
    print("Storage interface: getTelecallersByTeamLeader already exists")
elif OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print("Step 2a OK: getTelecallersByTeamLeader added to interface")
else:
    errors.append("Step 2a: getTelecallersByAgency interface not found")

# 2b. Add implementation after getTelecallersByAgency implementation
OLD2 = '  async getAllUsers(): Promise<User[]> {'
NEW2 = '''  async getTelecallersByTeamLeader(teamLeaderId: string): Promise<User[]> {
    return db.select().from(users).where(
      and(eq(users.teamLeaderId, teamLeaderId), eq(users.role, "TELE_CALLER"))
    ).orderBy(desc(users.createdAt));
  }

  async getAllUsers(): Promise<User[]> {'''
if 'getTelecallersByTeamLeader' in content and 'async getTelecallersByTeamLeader' in content:
    print("Storage impl: getTelecallersByTeamLeader already implemented")
elif OLD2 in content:
    content = content.replace(OLD2, NEW2)
    print("Step 2b OK: getTelecallersByTeamLeader implementation added")
else:
    errors.append("Step 2b: getAllUsers implementation not found")

# 2c. Update getLeadsByAgency interface signature to add teamLeaderIdFilter
OLD3 = '  getLeadsByAgency(agencyCode: string, page: number, limit: number, status?: string, assignmentFilter?: string, search?: string, assignedToFilter?: string): Promise<{ leads: Lead[]; total: number }>;'
NEW3 = '  getLeadsByAgency(agencyCode: string, page: number, limit: number, status?: string, assignmentFilter?: string, search?: string, assignedToFilter?: string, teamLeaderIdFilter?: string): Promise<{ leads: Lead[]; total: number }>;'
if 'teamLeaderIdFilter' in content:
    print("Storage interface: teamLeaderIdFilter already exists")
elif OLD3 in content:
    content = content.replace(OLD3, NEW3)
    print("Step 2c OK: teamLeaderIdFilter added to interface")
else:
    errors.append("Step 2c: getLeadsByAgency interface not found")

# 2d. Update getLeadsByAgency implementation signature
OLD4 = '  async getLeadsByAgency(agencyCode: string, page: number = 1, limit: number = 20, status?: string, assignmentFilter?: string, search?: string, assignedToFilter?: string): Promise<{ leads: Lead[]; total: number }> {'
NEW4 = '  async getLeadsByAgency(agencyCode: string, page: number = 1, limit: number = 20, status?: string, assignmentFilter?: string, search?: string, assignedToFilter?: string, teamLeaderIdFilter?: string): Promise<{ leads: Lead[]; total: number }> {'
if 'async getLeadsByAgency' in content and 'teamLeaderIdFilter?' in content:
    print("Storage impl: teamLeaderIdFilter already in signature")
elif OLD4 in content:
    content = content.replace(OLD4, NEW4)
    print("Step 2d OK: teamLeaderIdFilter added to implementation signature")
else:
    errors.append("Step 2d: getLeadsByAgency implementation signature not found")

# 2e. Add teamLeaderIdFilter condition inside getLeadsByAgency
OLD5 = '    if (assignedToFilter && assignedToFilter !== "ALL") {\n      conditions.push(eq(leads.assignedTo, assignedToFilter));\n    }\n    const where = and(...conditions);'
NEW5 = '    if (assignedToFilter && assignedToFilter !== "ALL") {\n      conditions.push(eq(leads.assignedTo, assignedToFilter));\n    }\n    if (teamLeaderIdFilter) {\n      conditions.push(eq(leads.teamLeaderId, teamLeaderIdFilter));\n    }\n    const where = and(...conditions);'
if 'teamLeaderIdFilter)' in content:
    print("Storage impl: teamLeaderIdFilter condition already added")
elif OLD5 in content:
    content = content.replace(OLD5, NEW5)
    print("Step 2e OK: teamLeaderIdFilter condition added to getLeadsByAgency")
else:
    errors.append("Step 2e: assignedToFilter condition block not found")

if errors:
    print("ERRORS:", errors)
    exit(1)

with open(filepath, "w") as f:
    f.write(content)
print("storage.ts patched successfully")
