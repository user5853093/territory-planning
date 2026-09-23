import csv
from pathlib import Path

BASE = Path(__file__).parent

def main():
    leads_path = BASE / "leads.csv"
    coords_path = BASE / "coordinates.csv"
    output_path = BASE / "leads_enriched.csv"

    with leads_path.open(newline="", encoding="utf-8") as f:
        leads = list(csv.DictReader(f))
    with coords_path.open(newline="", encoding="utf-8") as f:
        coords = {row["Street"]: row for row in csv.DictReader(f)}

    fieldnames = ["Company", "Street", "City", "State", "Latitude", "Longitude"]
    rows = []
    for lead in leads:
        coord = coords.get(lead["Street"])
        if coord is None:
            print(f"WARNING: no coordinates found for {lead['Street']}")
            continue
        rows.append({
            "Company": lead["Company"],
            "Street": lead["Street"],
            "City": lead["City"],
            "State": lead["State"],
            "Latitude": coord["Latitude"],
            "Longitude": coord["Longitude"],
        })

    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Merged {len(rows)} rows into {output_path.name}")

if __name__ == "__main__":
    main()