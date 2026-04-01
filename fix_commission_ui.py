path = "/var/www/ica-crm/client/src/pages/leads.tsx"
with open(path, "r") as f:
    content = f.read()

old = '''        commissionsData.forEach((c: any) => {
          const key = c.userId;
          if (!grouped[key]) grouped[key] = { name: c.telecallerName || "Unknown", total: 0, pending: 0, paid: 0, converted: 0 };
          grouped[key].total += c.amount;
          grouped[key].converted += 1;
          if (c.paidStatus === "PAID") grouped[key].paid += c.amount;
          else grouped[key].pending += c.amount;
        });'''

new = '''        commissionsData.forEach((c: any) => {
          const key = c.userId;
          if (!grouped[key]) grouped[key] = { name: c.telecallerName || "Unknown", total: 0, pending: 0, paid: 0, converted: 0, totalConverted: c.totalConverted || 0 };
          grouped[key].total += c.amount;
          grouped[key].converted += 1;
          grouped[key].totalConverted = c.totalConverted || 0;
          if (c.paidStatus === "PAID") grouped[key].paid += c.amount;
          else grouped[key].pending += c.amount;
        });'''

content = content.replace(old, new)

old2 = '''                      <th className="text-left py-2 pr-4 font-medium">Telecaller</th>
                      <th className="text-center py-2 pr-4 font-medium">Conversions</th>
                      <th className="text-right py-2 pr-4 font-medium">Total Earned</th>
                      <th className="text-right py-2 pr-4 font-medium text-green-600">Paid</th>
                      <th className="text-right py-2 font-medium text-orange-500">Pending</th>'''

new2 = '''                      <th className="text-left py-2 pr-4 font-medium">Telecaller</th>
                      <th className="text-center py-2 pr-4 font-medium">Total Converted</th>
                      <th className="text-center py-2 pr-4 font-medium">Commission On</th>
                      <th className="text-right py-2 pr-4 font-medium">Total Earned</th>
                      <th className="text-right py-2 pr-4 font-medium text-green-600">Paid</th>
                      <th className="text-right py-2 font-medium text-orange-500">Pending</th>'''

content = content.replace(old2, new2)

old3 = '''                        <td className="py-2 pr-4 font-medium">{r.name}</td>
                        <td className="py-2 pr-4 text-center">
                          <span className="inline-flex items-center gap-1 bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 text-xs px-2 py-0.5 rounded-full">
                            <TrendingUp className="w-3 h-3" />{r.converted}
                          </span>
                        </td>'''

new3 = '''                        <td className="py-2 pr-4 font-medium">{r.name}</td>
                        <td className="py-2 pr-4 text-center">
                          <span className="inline-flex items-center gap-1 bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400 text-xs px-2 py-0.5 rounded-full">
                            <TrendingUp className="w-3 h-3" />{r.totalConverted}
                          </span>
                        </td>
                        <td className="py-2 pr-4 text-center">
                          <span className="inline-flex items-center gap-1 bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 text-xs px-2 py-0.5 rounded-full">
                            <TrendingUp className="w-3 h-3" />{r.converted}
                          </span>
                        </td>'''

content = content.replace(old3, new3)

old4 = '''                      <td className="py-2 pr-4 font-bold text-xs uppercase text-muted-foreground">Total</td>
                      <td className="py-2 pr-4 text-center font-bold">{rows.reduce((a,r)=>a+r.converted,0)}</td>'''

new4 = '''                      <td className="py-2 pr-4 font-bold text-xs uppercase text-muted-foreground">Total</td>
                      <td className="py-2 pr-4 text-center font-bold">{rows.reduce((a,r)=>a+r.totalConverted,0)}</td>
                      <td className="py-2 pr-4 text-center font-bold">{rows.reduce((a,r)=>a+r.converted,0)}</td>'''

content = content.replace(old4, new4)

with open(path, "w") as f:
    f.write(content)
print("Done")
