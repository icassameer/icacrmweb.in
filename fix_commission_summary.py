path = "/var/www/ica-crm/client/src/pages/leads.tsx"
with open(path, "r") as f:
    content = f.read()

# 1. Add TrendingUp and IndianRupee to lucide imports
old_import = "  Phone, Plus, ChevronLeft, ChevronRight, Filter, Search,\n  UserCheck, Clock, CheckCircle2, XCircle, AlertCircle,\n  Upload, Download, Briefcase, Check, MessageCircle,"
new_import = "  Phone, Plus, ChevronLeft, ChevronRight, Filter, Search,\n  UserCheck, Clock, CheckCircle2, XCircle, AlertCircle,\n  Upload, Download, Briefcase, Check, MessageCircle, TrendingUp, IndianRupee,"
content = content.replace(old_import, new_import)

# 2. Add commission query after leads stats query
old_query = '    queryKey: ["/api/stats/leads"],\n    queryFn: () => apiFetch("/api/stats/leads"),'
new_query = '    queryKey: ["/api/stats/leads"],\n    queryFn: () => apiFetch("/api/stats/leads"),\n  });\n  const { data: commissionsData } = useQuery({\n    queryKey: ["/api/commissions"],\n    queryFn: () => apiFetch("/api/commissions"),\n    enabled: isAgencyAdmin,'
content = content.replace(old_query, new_query)

# 3. Add commission summary after stat cards closing div
old_section = '        </div>\n      ) : ('
new_section = '''        </div>

      {/* Telecaller-wise Commission Summary — AGENCY_ADMIN only */}
      {isAgencyAdmin && commissionsData && commissionsData.length > 0 && (() => {
        const grouped: Record<string, { name: string; total: number; pending: number; paid: number; converted: number }> = {};
        commissionsData.forEach((c: any) => {
          const key = c.userId;
          if (!grouped[key]) grouped[key] = { name: c.telecallerName || "Unknown", total: 0, pending: 0, paid: 0, converted: 0 };
          grouped[key].total += c.amount;
          grouped[key].converted += 1;
          if (c.paidStatus === "PAID") grouped[key].paid += c.amount;
          else grouped[key].pending += c.amount;
        });
        const rows = Object.values(grouped);
        return (
          <Card className="mt-2">
            <CardContent className="p-4">
              <div className="flex items-center gap-2 mb-3">
                <IndianRupee className="w-4 h-4 text-green-600" />
                <h3 className="font-semibold text-sm">Telecaller Commission Summary</h3>
                <span className="text-xs text-muted-foreground ml-1">— this month</span>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b text-muted-foreground text-xs">
                      <th className="text-left py-2 pr-4 font-medium">Telecaller</th>
                      <th className="text-center py-2 pr-4 font-medium">Conversions</th>
                      <th className="text-right py-2 pr-4 font-medium">Total Earned</th>
                      <th className="text-right py-2 pr-4 font-medium text-green-600">Paid</th>
                      <th className="text-right py-2 font-medium text-orange-500">Pending</th>
                    </tr>
                  </thead>
                  <tbody>
                    {rows.map((r, i) => (
                      <tr key={i} className="border-b last:border-0 hover:bg-muted/30 transition-colors">
                        <td className="py-2 pr-4 font-medium">{r.name}</td>
                        <td className="py-2 pr-4 text-center">
                          <span className="inline-flex items-center gap-1 bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 text-xs px-2 py-0.5 rounded-full">
                            <TrendingUp className="w-3 h-3" />{r.converted}
                          </span>
                        </td>
                        <td className="py-2 pr-4 text-right font-semibold">₹{r.total.toLocaleString()}</td>
                        <td className="py-2 pr-4 text-right text-green-600 font-medium">₹{r.paid.toLocaleString()}</td>
                        <td className="py-2 text-right text-orange-500 font-medium">₹{r.pending.toLocaleString()}</td>
                      </tr>
                    ))}
                  </tbody>
                  <tfoot>
                    <tr className="border-t-2">
                      <td className="py-2 pr-4 font-bold text-xs uppercase text-muted-foreground">Total</td>
                      <td className="py-2 pr-4 text-center font-bold">{rows.reduce((a,r)=>a+r.converted,0)}</td>
                      <td className="py-2 pr-4 text-right font-bold">₹{rows.reduce((a,r)=>a+r.total,0).toLocaleString()}</td>
                      <td className="py-2 pr-4 text-right font-bold text-green-600">₹{rows.reduce((a,r)=>a+r.paid,0).toLocaleString()}</td>
                      <td className="py-2 text-right font-bold text-orange-500">₹{rows.reduce((a,r)=>a+r.pending,0).toLocaleString()}</td>
                    </tr>
                  </tfoot>
                </table>
              </div>
            </CardContent>
          </Card>
        );
      })()}

      ) : ('''
content = content.replace(old_section, new_section)

with open(path, "w") as f:
    f.write(content)
print("Done")
