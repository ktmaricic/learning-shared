import csv

with open("survey.csv") as f:
    rows = list(csv.DictReader(f))

print(rows)
print("total rows:", len(rows))

missing = 0
totals = {}
counts = {}

for r in rows:
    if not r["score"].strip():
        missing += 1
        continue
    g = r["group"].strip()
    s = float(r["score"])
    totals[g] = totals.get(g, 0) + s
    counts[g] = counts.get(g, 0) + 1

print("missing scores:", missing)
for g in totals:
    print(g, totals[g] / counts[g])
