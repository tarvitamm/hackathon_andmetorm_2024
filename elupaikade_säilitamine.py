#!pip install rasterio
import requests
import rasterio
from rasterio.plot import show
from pyproj import Transformer
import pandas as pd

def convert_to_m2(pindala):
    """
    Convert area to square meters (m2).
    """
    if 'ha' in pindala:
        # Convert hectares to m2
        value = float(pindala.replace('ha', '').replace(',', '.').strip()) * 10000
    elif 'm2' in pindala:
        # Clean up and retain m2 values
        value = float(pindala.replace('m2', '').replace(',', '').strip())
    else:
        raise ValueError(f"Unknown unit in Pindala: {pindala}")
    return value

def read_data(input_file):
    """
    Preprocess the data to convert 'Pindala' to square meters (m2).
    """
    data = pd.read_csv(input_file, delimiter=';')
    data['Pindala'] = data['Pindala'].apply(convert_to_m2)  # Overwrite the existing column
    return data

def geocode_address(aadress):
    """
    Perform geocoding for a single address and return its coordinates.
    """
    base_url = "https://inaadress.maaamet.ee/geocoder-api/api/online"
    params = {"text": aadress, "output": "json"}

    # Perform the GET request to geocode the address
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        geocode_data = response.json()
        if geocode_data:
            # Extract longitude and latitude from the response
            longitude = geocode_data.get("b")
            latitude = geocode_data.get("l")
            if longitude is not None and latitude is not None:
                return longitude, latitude
    else:
        print(f"Geocoding Error {response.status_code}: {response.text} for address '{aadress}'")
    return None, None

def geocode_addresses(input_file, output_file):
    """
    Geocode addresses from the input CSV and save the results to a new CSV.
    """
    # Preprocess the data to add Pindala_m2
    data = read_data(input_file)  # Ensure this is called to process 'Pindala'

    # Create a list to store geocoded results
    geocoded_results = []

    # Iterate over rows to geocode each address
    for index, row in data.iterrows():
        aadress = row['Aadress']
        pindala = row['Pindala']

        # Geocode the address
        longitude, latitude = geocode_address(aadress)

        # Append the result
        geocoded_results.append({
            "Aadress": aadress,
            "Longitude": longitude,
            "Latitude": latitude,
            "Pindala": pindala
        })

        print(f"Processed: {aadress} -> Longitude: {longitude}, Latitude: {latitude}")

    # Convert the results to a DataFrame
    geocoded_df = pd.DataFrame(geocoded_results)

    # Save the results to a new CSV
    geocoded_df.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Geocoded results saved to {output_file}")


# File paths
input_file = "data/tallinna_lennujaam.csv"  # Input file with Aadress and Pindala columns
output_file = "data/geocoded_addresses.csv"  # Output file for geocoded results

# Run the geocoding process
geocode_addresses(input_file, output_file)

def sample_raster(raster_file, geocoded_data):
    """
    Find the raster value for the geocoded coordinates and return results as an array.
    """
    raster_results = []

    with rasterio.open(raster_file) as src:
        transformer = Transformer.from_crs("EPSG:4326", src.crs.to_string(), always_xy=True)

        for row in geocoded_data:
            longitude = row["Longitude"]
            latitude = row["Latitude"]
            aadress = row["Aadress"]
            pindala = row["Pindala"]

            if longitude is not None and latitude is not None:
                # Transform coordinates to raster CRS
                x, y = transformer.transform(longitude, latitude)
                try:
                    # Sample raster value
                    value = list(src.sample([(x, y)]))[0][0]
                    raster_results.append({
                        "Aadress": aadress,
                        "Longitude": longitude,
                        "Latitude": latitude,
                        "Pindala": pindala,
                        "RasterValue": value
                    })
                except Exception:
                    raster_results.append({
                        "Aadress": aadress,
                        "Longitude": longitude,
                        "Latitude": latitude,
                        "Pindala": pindala,
                        "RasterValue": None
                    })
            else:
                raster_results.append({
                    "Aadress": aadress,
                    "Longitude": longitude,
                    "Latitude": latitude,
                    "Pindala": pindala,
                    "RasterValue": None
                })

    return raster_results

def count_data(values):
    return [1 if value >= 5 else 0 for value in values]

def dangerous_area(data, dangerous_or_not):
    return [data['Pindala'][i] for i in range(len(dangerous_or_not)) if dangerous_or_not[i] == 1]
# Load geocoded data from CSV
geocoded_data = pd.read_csv("data/geocoded_addresses.csv").to_dict(orient="records")

# Sample raster values
raster_file = "maps/elupaigahuve_pakkumine.tif"
raster_results = sample_raster(raster_file, geocoded_data)

# Extract RasterValues for further processing
raster_values = [item['RasterValue'] for item in raster_results if item['RasterValue'] is not None]

# Count dangerous areas
dangerous_flags = count_data(raster_values)

# Identify dangerous areas
raster_results_df = pd.DataFrame(raster_results)  # Convert to DataFrame for indexing
dangerous_areas = dangerous_area(raster_results_df, dangerous_flags)
dangerous_count = sum(dangerous_flags)

total_area = raster_results_df['Pindala'].sum()
# Calculate the total dangerous area
total_dangerous_area = sum(dangerous_areas)

# Extract the addresses associated with dangerous areas
dangerous_addresses = [
    raster_results[i]['Aadress']
    for i in range(len(dangerous_flags))
    if dangerous_flags[i] == 1
]

# Display the results
print("Addresses of Dangerous Areas:")
for address in dangerous_addresses:
    print(f" - {address}")

print(f"\nCount of Dangerous Flags: {dangerous_count}")
print(f"Total Dangerous Area (in m²): {total_dangerous_area:.2f}")
print(f"Total area by company: {total_area}")
print(f"Dangerous area percentage: {total_dangerous_area/total_area * 100:.2f}%")
