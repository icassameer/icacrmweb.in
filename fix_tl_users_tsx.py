# ── PATCH 4: client/src/pages/users.tsx ──────────────────────────────────────
filepath = "/var/www/ica-crm/client/src/pages/users.tsx"
with open(filepath, "r") as f:
    content = f.read()

errors = []

# 4a. Add teamLeaderId to form state
OLD1 = '  const [form, setForm] = useState({\n    username: "", password: "", fullName: "", email: "", mobile: "", role: "TELE_CALLER"\n  });'
NEW1 = '  const [form, setForm] = useState({\n    username: "", password: "", fullName: "", email: "", mobile: "", role: "TELE_CALLER", teamLeaderId: ""\n  });'
if 'teamLeaderId: ""' in content:
    print("users.tsx: teamLeaderId state already added")
elif OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print("Step 4a OK: teamLeaderId added to form state")
else:
    errors.append("Step 4a: form state not found")

# 4b. Fetch team leaders for agency admin
OLD2 = '  const { data: userList, isLoading } = useQuery({'
NEW2 = '''  const { data: teamLeaders } = useQuery({
    queryKey: ["/api/users/team-leaders"],
    queryFn: () => apiFetch("/api/users").then((list: any[]) => list.filter((u: any) => u.role === "TEAM_LEADER")),
    enabled: user?.role === "AGENCY_ADMIN",
  });

  const { data: userList, isLoading } = useQuery({'''
if 'team-leaders' in content:
    print("users.tsx: teamLeaders query already added")
elif OLD2 in content:
    content = content.replace(OLD2, NEW2)
    print("Step 4b OK: teamLeaders query added")
else:
    errors.append("Step 4b: userList query not found")

# 4c. Reset form to include teamLeaderId on success
OLD3 = '      setForm({ username: "", password: "", fullName: "", email: "", mobile: "", role: "TELE_CALLER" });'
NEW3 = '      setForm({ username: "", password: "", fullName: "", email: "", mobile: "", role: "TELE_CALLER", teamLeaderId: "" });'
if OLD3 in content:
    content = content.replace(OLD3, NEW3)
    print("Step 4c OK: form reset includes teamLeaderId")
else:
    errors.append("Step 4c: form reset not found")

# 4d. Add TL dropdown in create user form — after role select, before submit button
OLD4 = '''                <Button type="submit" className="w-full" disabled={createMutation.isPending} data-testid="button-submit-user">
                  {createMutation.isPending ? "Creating..." : "Add Member"}
                </Button>'''
NEW4 = '''                {user?.role === "AGENCY_ADMIN" && form.role === "TELE_CALLER" && (
                  <div className="space-y-2">
                    <Label>Assign to Team Leader</Label>
                    <Select value={form.teamLeaderId} onValueChange={(v) => setForm({ ...form, teamLeaderId: v })}>
                      <SelectTrigger data-testid="select-team-leader">
                        <SelectValue placeholder="Select Team Leader" />
                      </SelectTrigger>
                      <SelectContent>
                        {(teamLeaders || []).map((tl: any) => (
                          <SelectItem key={tl.id} value={tl.id}>{tl.fullName}</SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                  </div>
                )}
                <Button type="submit" className="w-full" disabled={createMutation.isPending} data-testid="button-submit-user">
                  {createMutation.isPending ? "Creating..." : "Add Member"}
                </Button>'''
if 'Assign to Team Leader' in content:
    print("users.tsx: TL dropdown already added")
elif OLD4 in content:
    content = content.replace(OLD4, NEW4)
    print("Step 4d OK: TL dropdown added to create user form")
else:
    errors.append("Step 4d: submit button not found")

# 4e. Show TL name on telecaller user cards
OLD5 = '                      {u.agencyCode && <span className="text-[10px]">{u.agencyCode}</span>}'
NEW5 = '''                      {u.agencyCode && <span className="text-[10px]">{u.agencyCode}</span>}
                      {u.role === "TELE_CALLER" && u.teamLeaderId && (
                        <span className="text-[10px] text-blue-500">
                          TL: {(teamLeaders || []).find((tl: any) => tl.id === u.teamLeaderId)?.fullName || "Assigned"}
                        </span>
                      )}'''
if 'TL: {(teamLeaders' in content:
    print("users.tsx: TL name on card already added")
elif OLD5 in content:
    content = content.replace(OLD5, NEW5)
    print("Step 4e OK: TL name shown on telecaller cards")
else:
    errors.append("Step 4e: agencyCode span not found")

if errors:
    print("ERRORS:", errors)
    exit(1)

with open(filepath, "w") as f:
    f.write(content)
print("users.tsx patched successfully")
