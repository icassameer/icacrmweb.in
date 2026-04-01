path = "/var/www/ica-crm/client/src/pages/leads.tsx"
with open(path, "r") as f:
    content = f.read()

# 1. Add icons to imports
old_import = "  Upload, Download, Briefcase, Check, MessageCircle,"
new_import = "  Upload, Download, Briefcase, Check, MessageCircle, TrendingUp, IndianRupee,"
content = content.replace(old_import, new_import)

# 2. Add commission query after leads stats query
old_query = '    queryKey: ["/api/stats/leads"],\n    queryFn: () => apiFetch("/api/stats/leads"),'
new_query = '    queryKey: ["/api/stats/leads"],\n    queryFn: () => apiFetch("/api/stats/leads"),\n  });\n  const { data: commissionsData } = useQuery({\n    queryKey: ["/api/commissions"],\n    queryFn: () => apiFetch("/api/commissions"),\n    enabled: isAgencyAdmin,'
content = content.replace(old_query, new_query)

with open(path, "w") as f:
    f.write(content)
print("Done")
