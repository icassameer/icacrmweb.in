filepath = "/var/www/ica-crm/client/src/pages/users.tsx"

with open(filepath, "r") as f:
    content = f.read()

errors = []

# 1. Add editTLOpen, editTLUser state
OLD1 = '  const [resetOpen, setResetOpen] = useState(false);'
NEW1 = '''  const [resetOpen, setResetOpen] = useState(false);
  const [editTLOpen, setEditTLOpen] = useState(false);
  const [editTLUser, setEditTLUser] = useState<any>(null);
  const [editTLValue, setEditTLValue] = useState("");'''
if 'editTLOpen' in content:
    print("State: already added")
elif OLD1 in content:
    content = content.replace(OLD1, NEW1)
    print("Step 1 OK: editTL state added")
else:
    errors.append("Step 1: resetOpen state not found")

# 2. Add editTL mutation
OLD2 = '  const toggleMutation = useMutation({'
NEW2 = '''  const editTLMutation = useMutation({
    mutationFn: ({ id, teamLeaderId }: { id: string; teamLeaderId: string }) =>
      apiFetch(`/api/users/${id}`, { method: "PATCH", body: JSON.stringify({ teamLeaderId: teamLeaderId || null }) }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["/api/users"] });
      setEditTLOpen(false);
      setEditTLUser(null);
      setEditTLValue("");
      toast({ title: "Team Leader updated" });
    },
    onError: (err: any) => toast({ title: "Error", description: err.message, variant: "destructive" }),
  });

  const toggleMutation = useMutation({'''
if 'editTLMutation' in content:
    print("Mutation: already added")
elif OLD2 in content:
    content = content.replace(OLD2, NEW2)
    print("Step 2 OK: editTLMutation added")
else:
    errors.append("Step 2: toggleMutation not found")

# 3. Add Pencil to lucide imports
OLD3 = 'import { Users, Plus, Mail, Shield, KeyRound, Phone, Trash2 } from "lucide-react";'
NEW3 = 'import { Users, Plus, Mail, Shield, KeyRound, Phone, Trash2, Pencil } from "lucide-react";'
if 'Pencil' in content:
    print("Icon: Pencil already imported")
elif OLD3 in content:
    content = content.replace(OLD3, NEW3)
    print("Step 3 OK: Pencil icon imported")
else:
    errors.append("Step 3: lucide import not found")

# 4. Add Edit TL button on telecaller cards — after reset password button
OLD4 = '''                  {canResetPassword && u.id !== user?.id && u.role !== "MASTER_ADMIN" && (
                    <Button
                      variant="ghost" size="icon"
                      onClick={() => { setResetUser(u); setNewPassword(""); setResetOpen(true); }}
                      title="Reset Password"
                      data-testid={`button-reset-password-${u.id}`}
                    >
                      <KeyRound className="w-4 h-4" />
                    </Button>
                  )}'''
NEW4 = '''                  {canResetPassword && u.id !== user?.id && u.role !== "MASTER_ADMIN" && (
                    <Button
                      variant="ghost" size="icon"
                      onClick={() => { setResetUser(u); setNewPassword(""); setResetOpen(true); }}
                      title="Reset Password"
                      data-testid={`button-reset-password-${u.id}`}
                    >
                      <KeyRound className="w-4 h-4" />
                    </Button>
                  )}
                  {user?.role === "AGENCY_ADMIN" && u.role === "TELE_CALLER" && (
                    <Button
                      variant="ghost" size="icon"
                      onClick={() => { setEditTLUser(u); setEditTLValue(u.teamLeaderId || ""); setEditTLOpen(true); }}
                      title="Assign Team Leader"
                      data-testid={`button-edit-tl-${u.id}`}
                    >
                      <Pencil className="w-4 h-4" />
                    </Button>
                  )}'''
if 'button-edit-tl' in content:
    print("Button: already added")
elif OLD4 in content:
    content = content.replace(OLD4, NEW4)
    print("Step 4 OK: Edit TL button added on telecaller cards")
else:
    errors.append("Step 4: reset password button block not found")

# 5. Add Edit TL Dialog — before closing </div>
OLD5 = '      <Dialog open={resetOpen} onOpenChange={setResetOpen}>'
NEW5 = '''      <Dialog open={editTLOpen} onOpenChange={setEditTLOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Assign Team Leader: {editTLUser?.fullName}</DialogTitle>
          </DialogHeader>
          <div className="space-y-4">
            <div className="space-y-2">
              <Label>Team Leader</Label>
              <Select value={editTLValue} onValueChange={setEditTLValue}>
                <SelectTrigger>
                  <SelectValue placeholder="Select Team Leader" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="none">— No Team Leader —</SelectItem>
                  {(teamLeaders || []).map((tl: any) => (
                    <SelectItem key={tl.id} value={tl.id}>{tl.fullName}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <Button
              className="w-full"
              onClick={() => editTLMutation.mutate({ id: editTLUser.id, teamLeaderId: editTLValue === "none" ? "" : editTLValue })}
              disabled={editTLMutation.isPending}
            >
              {editTLMutation.isPending ? "Saving..." : "Save"}
            </Button>
          </div>
        </DialogContent>
      </Dialog>

      <Dialog open={resetOpen} onOpenChange={setResetOpen}>'''
if 'Assign Team Leader:' in content:
    print("Dialog: already added")
elif OLD5 in content:
    content = content.replace(OLD5, NEW5)
    print("Step 5 OK: Edit TL dialog added")
else:
    errors.append("Step 5: resetOpen Dialog not found")

if errors:
    print("ERRORS:", errors)
    exit(1)

with open(filepath, "w") as f:
    f.write(content)
print("SUCCESS: Edit TL UI patched")
