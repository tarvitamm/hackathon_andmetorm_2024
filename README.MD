# Explanation of elupaikade_säilitamine.py
## Dangerous Area Detection with Raster and Geocoding

This project combines raster data analysis with geocoding to identify potentially dangerous areas based on predefined conditions. The process integrates geospatial data with address-based geocoding and calculates areas flagged as dangerous using raster values.

### Features
1. **Convert Area Units:** Processes area (`Pindala`) values, converting them from hectares (ha) or square meters (m²) into a unified format (m²).
2. **Geocode Addresses:** Retrieves latitude and longitude coordinates for given addresses using a public API.
3. **Sample Raster Values:** Samples raster values from a given GeoTIFF file using geocoded coordinates.
4. **Identify Dangerous Areas:** Flags areas as dangerous if a condition (e.g., raster value >= 5) is met.
5. **Calculate Statistics:**
   - Total number of dangerous areas.
   - Total area flagged as dangerous.
   - Dangerous area percentage of the total area.
6. **Output Results:**
   - Saves geocoded data and raster analysis results.
   - Prints addresses flagged as dangerous.

---

# Explanation of `elupaikade_säilitamine.py`
## Dangerous Area Detection with Raster and Geocoding

This script combines raster data analysis with geocoding to identify dangerous areas based on predefined conditions. It integrates geospatial data and address-based geocoding, calculating areas flagged as dangerous.

### Features
1. **Convert Area Units:** Converts area values from hectares or square meters into a unified format (m²).
2. **Geocode Addresses:** Uses a public API to get latitude and longitude for input addresses.
3. **Sample Raster Values:** Extracts raster values from a GeoTIFF file at geocoded locations.
4. **Identify Dangerous Areas:** Flags areas as dangerous if a specified raster condition (e.g., value ≥ 5) is met.
5. **Calculate Statistics:**
   - Total number of dangerous areas.
   - Total area flagged as dangerous.
   - Percentage of the total area flagged as dangerous.
6. **Output Results:** Saves results, including geocoded data and flagged addresses, and prints flagged addresses.

--- 


