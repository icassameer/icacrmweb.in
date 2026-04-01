path = "/var/www/ica-crm/client/src/pages/leads.tsx"
with open(path, "r") as f:
    content = f.read()

# Fix: add ") : (" right after stat cards closing div, before commission block
old = '        </div>\n      {/* Telecaller-wise Commission Summary'
new = '        </div>\n      ) : (\n      {/* Telecaller-wise Commission Summary'
content = content.replace(old, new)

# Fix: remove the orphaned ") : (" that is now after the commission block
old2 = '      })()}\n      ) : ('
new2 = '      })()}\n'
content = content.replace(old2, new2)

with open(path, "w") as f:
    f.write(content)
print("Done")
