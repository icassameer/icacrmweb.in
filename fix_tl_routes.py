# ── PATCH 3: server/routes.ts ─────────────────────────────────────────────────
filepath = "/var/www/ica-crm/server/routes.ts"
with open(filepath, "r") as f:
    content = f.read()

errors = []

# 3a. POST /api/users — accept teamLeaderId, save it when creating TELE_CALLER
OLD1 = '''      const hashedPassword = await bcrypt.hash(password, 10);
      const user = await storage.createUser({
        username, password: hashedPassword, fullName, email, mobile: mobile || null,
        role, agencyCode, isActive: true, status: "ACTIVE"
      });'''
NEW1 = '''      const hashedPassword = await bcrypt.hash(password, 10);
      const teamLeaderId = role === "TELE_CALLER" ? (req.body.teamLeaderId || null) : null;
      const user = await storage.createUser({
        username, password: hashedPassword, fullName, email, mobile: mobile || null,
        role, agencyCode, isActive: true, status: "ACTIVE", teamLeaderId,
      });'''
if 'teamLeaderId = role === "TELE_CALLER"' in content:
    print("Routes: createUser teamLeaderId already added")
elif OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print("Step 3a OK: teamLeaderId saved on user creation")
else:
    errors.append("Step 3a: createUser block not found")

# 3b. GET /api/users — TL gets only their team telecallers
OLD2 = '''      if (req.user!.role === "TEAM_LEADER") {
        const userList = await storage.getTelecallersByAgency(agencyCode);'''
NEW2 = '''      if (req.user!.role === "TEAM_LEADER") {
        const userList = await storage.getTelecallersByTeamLeader(req.user!.id);'''
if 'getTelecallersByTeamLeader' in content:
    print("Routes: GET /api/users TL filter already updated")
elif OLD2 in content:
    content = content.replace(OLD2, NEW2)
    print("Step 3b OK: TL sees only their team's telecallers")
else:
    errors.append("Step 3b: GET /api/users TEAM_LEADER block not found")

# 3c. GET /api/leads — TL gets only leads where teamLeaderId = TL's id
OLD3 = '''      const agencyCode = req.user!.agencyCode;
      if (!agencyCode) return res.status(400).json({ success: false, message: "No agency" });
      const assignment = req.query.assignment as string;
      const assignedToFilter = req.query.assignedTo as string | undefined;
      const result = await storage.getLeadsByAgency(agencyCode, page, limit, status, assignment, search, assignedToFilter);
      res.json({ success: true, data: result });'''
NEW3 = '''      const agencyCode = req.user!.agencyCode;
      if (!agencyCode) return res.status(400).json({ success: false, message: "No agency" });
      const assignment = req.query.assignment as string;
      const assignedToFilter = req.query.assignedTo as string | undefined;
      const teamLeaderIdFilter = req.user!.role === "TEAM_LEADER" ? req.user!.id : undefined;
      const result = await storage.getLeadsByAgency(agencyCode, page, limit, status, assignment, search, assignedToFilter, teamLeaderIdFilter);
      res.json({ success: true, data: result });'''
if 'teamLeaderIdFilter = req.user' in content:
    print("Routes: GET /api/leads TL filter already added")
elif OLD3 in content:
    content = content.replace(OLD3, NEW3)
    print("Step 3c OK: TL sees only their team's leads")
else:
    errors.append("Step 3c: GET /api/leads agency block not found")

# 3d. PATCH /api/leads/:id — auto-set teamLeaderId when TL assigns
OLD4 = '''      if (req.body.assignedTo !== undefined && req.user!.role !== "TEAM_LEADER") {
        return res.status(403).json({ success: false, message: "Only Team Leaders can assign leads" });
      }'''
NEW4 = '''      if (req.body.assignedTo !== undefined && req.user!.role !== "TEAM_LEADER") {
        return res.status(403).json({ success: false, message: "Only Team Leaders can assign leads" });
      }
      if (req.body.assignedTo !== undefined && req.user!.role === "TEAM_LEADER") {
        req.body.teamLeaderId = req.user!.id;
      }'''
if 'req.body.teamLeaderId = req.user!.id' in content:
    print("Routes: PATCH leads teamLeaderId auto-set already added")
elif OLD4 in content:
    content = content.replace(OLD4, NEW4)
    print("Step 3d OK: teamLeaderId auto-set on lead assignment")
else:
    errors.append("Step 3d: PATCH leads assignedTo check not found")

# 3e. POST /api/leads/bulk-assign — auto-set teamLeaderId
OLD5 = '          await storage.updateLead(leadId, { assignedTo, service: service || lead.service });'
NEW5 = '          await storage.updateLead(leadId, { assignedTo, service: service || lead.service, teamLeaderId: req.user!.id });'
if 'teamLeaderId: req.user!.id' in content:
    print("Routes: bulk-assign teamLeaderId already added")
elif OLD5 in content:
    content = content.replace(OLD5, NEW5)
    print("Step 3e OK: teamLeaderId added to bulk-assign")
else:
    errors.append("Step 3e: bulk-assign updateLead line not found")

if errors:
    print("ERRORS:", errors)
    exit(1)

with open(filepath, "w") as f:
    f.write(content)
print("routes.ts patched successfully")
