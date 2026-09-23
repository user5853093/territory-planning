# Territory Planning — Lead Enrichment

Enriches a CSV of sales leads with geographic coordinates using a script-based workflow, verifies the results, and produces an interactive map of the leads.

## Source Data

- `leads.csv` — 25 sales leads with Company, Street, City, State
- `coordinates.csv` — pre-resolved latitude/longitude for each street address

## Scripts

- `merge_leads.py` — merges `leads.csv` and `coordinates.csv` into `leads_enriched.csv`
- `verify.py` — validates coordinates and produces `territory_summary.txt`
- `generate_map.py` — renders `map.html` from `leads_enriched.csv` using Leaflet

## Build
