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