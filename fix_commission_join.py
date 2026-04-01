path = "/var/www/ica-crm/server/storage.ts"
with open(path, "r") as f:
    content = f.read()

old = '''  async getCommissionsByAgency(agencyCode: string): Promise<any[]> {
    return db.select().from(commissions)
      .where(eq(commissions.agencyCode, agencyCode))
      .orderBy(desc(commissions.convertedAt));
  }'''

new = '''  async getCommissionsByAgency(agencyCode: string): Promise<any[]> {
    const rows = await db.select().from(commissions)
      .where(eq(commissions.agencyCode, agencyCode))
      .orderBy(desc(commissions.convertedAt));
    const userIds = [...new Set(rows.map((r: any) => r.userId))];
    if (userIds.length === 0) return rows;
    const userRows = await db.select().from(users).where(inArray(users.id, userIds));
    const userMap: Record<string, string> = {};
    userRows.forEach((u: any) => { userMap[u.id] = u.fullName; });
    return rows.map((r: any) => ({ ...r, telecallerName: userMap[r.userId] || "Unknown" }));
  }'''

content = content.replace(old, new)

with open(path, "w") as f:
    f.write(content)
print("Done")
