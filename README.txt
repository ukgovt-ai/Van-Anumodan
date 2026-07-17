Authoritative GIS layers folder
================================
Put your authoritative boundary layers here as GeoJSON (.geojson/.json) or KML/KMZ.
The desktop engine reads this folder automatically; in the app, GIS tab -> "Check
against folder layers" intersects the proposal boundary against every file here.

Category is inferred from the file name:
  - Tiger Reserve / CTH  -> name contains "tiger", "cth", "tr", or "reserve"
  - Protected Area (Sanctuary/NP) -> "protected", "sanctuary", "national park", "pa"
  - Eco-Sensitive Zone   -> "esz", "eco-sensitive", "sensitive"
  - Wildlife corridor    -> "corridor"

To override the inferred category, add a manifest.json here (see manifest.example.json):
  { "my_layer.geojson": "tr", "another.kml": "esz" }

A proposal that intersects a Tiger Reserve/CTH or Protected Area automatically raises a
CRITICAL red flag (blocking "Ready for Forwarding"); ESZ and corridor raise MAJOR flags.
Officers still set Pass/Fail on the GIS checklist per their assessment.
