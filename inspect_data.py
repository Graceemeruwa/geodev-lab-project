import csv


def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


facilities = inspect_column("ila_ward_results.csv", "facility_count")
load = inspect_column("ila_ward_results.csv", "residents_per_facility")

print("Facility count:", facilities)
print("Residents per facility:", load)
