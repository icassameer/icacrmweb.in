path = "/var/www/ica-crm/client/src/pages/leads.tsx"
with open(path, "r") as f:
    content = f.read()

old = '    queryFn: () => apiFetch("/api/commissions"),\n    enabled: isAgencyAdmin,\n    enabled: isAgencyAdmin,'
new = '    queryFn: () => apiFetch("/api/commissions"),\n    enabled: isAgencyAdmin,'
content = content.replace(old, new)

with open(path, "w") as f:
    f.write(content)
print("Done")
