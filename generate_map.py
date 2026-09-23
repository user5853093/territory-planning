import csv
import json
from pathlib import Path

BASE = Path(__file__).parent
INPUT = BASE / "leads_enriched.csv"
TEMPLATE = BASE / "map_template.html"
OUTPUT = BASE / "map.html"

def main():
    with INPUT.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    leads = [{
        "company": r["Company"],
        "street": r["Street"],
        "city": r["City"],
        "state": r["State"],
        "lat": float(r["Latitude"]),
        "lon": float(r["Longitude"]),
    } for r in rows]

    template = TEMPLATE.read_text(encoding="utf-8")
    html = template.replace("{{LEADS_JSON}}", json.dumps(leads))
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT.name} with {len(leads)} leads")

if __name__ == "__main__":
    main()