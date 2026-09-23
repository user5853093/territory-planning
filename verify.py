import csv
from pathlib import Path

BASE = Path(__file__).parent
INPUT = BASE / "leads_enriched.csv"
REPORT = BASE / "territory_summary.txt"

LAT_MIN, LAT_MAX = 39.65, 39.95
LON_MIN, LON_MAX = -89.95, -89.55

def main():
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    total = len(rows)
    missing = [r for r in rows if not r["Latitude"].strip() or not r["Longitude"].strip()]
    out_of_range = []
    cities = {}

    for r in rows:
        try:
            lat = float(r["Latitude"])
            lon = float(r["Longitude"])
        except ValueError:
            out_of_range.append((r["Company"], "invalid format"))
            continue
        if not (LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX):
            out_of_range.append((r["Company"], f"{lat}, {lon}"))
        cities[r["City"]] = cities.get(r["City"], 0) + 1

    lines = []
    lines.append("TERRITORY PLANNING - VERIFICATION REPORT")
    lines.append("=" * 45)
    lines.append(f"Total leads processed: {total}")
    lines.append(f"Rows missing coordinates: {len(missing)}")
    lines.append(f"Rows outside Central IL bounds: {len(out_of_range)}")
    lines.append("")
    lines.append("Leads per city:")
    for city, count in sorted(cities.items()):
        lines.append(f"  {city}: {count}")
    lines.append("")
    if out_of_range:
        lines.append("Out-of-range leads:")
        for company, info in out_of_range:
            lines.append(f"  {company}: {info}")
    else:
        lines.append("All coordinates within expected Central Illinois bounds.")

    output = "\n".join(lines)
    REPORT.write_text(output, encoding="utf-8")
    print(output)
    print(f"\nReport written to: {REPORT.name}")

if __name__ == "__main__":
    main()