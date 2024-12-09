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

# Explanation of võõrliikide_arv.py
## Analyzing Raster Data for Identifying Dangerous Areas

This notebook processes geospatial and raster data to detect and analyze areas flagged as potentially dangerous. The workflow includes data preprocessing, geocoding, raster value extraction, and statistical analysis.

### Key Steps
1. **Data Preparation:**
   - Reads area data (e.g., address, area size) and converts measurements to square meters.
   - Loads raster data (GeoTIFF format) for analysis.

2. **Geocoding Addresses:**
   - Retrieves geographical coordinates (latitude and longitude) for input addresses using a geocoding API.

3. **Sampling Raster Values:**
   - Extracts raster values corresponding to geocoded coordinates to assess conditions (e.g., soil quality, pollution levels).

4. **Flagging Dangerous Areas:**
   - Defines areas as dangerous if sampled raster values meet specified conditions (e.g., threshold values ≥ 5).

5. **Statistical Analysis:**
   - Calculates the total number of dangerous areas.
   - Sums the total area marked as dangerous.
   - Computes the proportion of dangerous areas relative to the total area.

6. **Output Results:**
   - Saves the analysis results, including flagged addresses and corresponding raster values.
   - Displays a summary of dangerous areas and their statistics.



