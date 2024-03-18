import pandas as pd
import matplotlib.pyplot as plt
import math

# Function to convert latitude, longitude, and height to ECEF coordinates
def convert_to_ecef(lat, lon, height):
    a = 6378137.0  # semi-major axis of the WGS84 ellipsoid in meters
    f = 1 / 298.257223563  # flattening of the WGS84 ellipsoid
    
    # Convert latitude and longitude from degrees to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    
    # Compute auxiliary values
    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    sin_lon = math.sin(lon_rad)
    cos_lon = math.cos(lon_rad)
    
    # Compute prime vertical radius of curvature
    N = a / math.sqrt(1 - (f * (2 - f)) * sin_lat ** 2)
    
    # Compute ECEF coordinates
    x = (N + height) * cos_lat * cos_lon
    y = (N + height) * cos_lat * sin_lon
    z = ((1 - f) * N + height) * sin_lat
    
    return x, y, z

# Read the ASCII file and extract relevant fields
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
latitudes = []
longitudes = []
heights = []
ecef_data = []

# Iterate through each line in the file
for line in data:
    # Split the line into log header and fields
    log_header, fields = line.split(';')
    
    # Split the fields into individual data points
    fields = fields.split(',')
    
    # Extracting relevant data (latitude, longitude, and height)
    lat = float(fields[2])
    lon = float(fields[3])
    hgt = float(fields[4])
    
    # Store the parsed data in lists
    latitudes.append(lat)
    longitudes.append(lon)
    heights.append(hgt)
    
    # Convert latitude, longitude, and height to ECEF coordinates
    x, y, z = convert_to_ecef(lat, lon, hgt)
    ecef_data.append([x, y, z])

# Create DataFrame with relevant fields
df = pd.DataFrame({'lat': latitudes, 'lon': longitudes, 'hgt': heights})

# Define column names for ECEF DataFrame
ecef_columns = ['ecef_x', 'ecef_y', 'ecef_z']
df_ecef = pd.DataFrame(ecef_data, columns=ecef_columns)
print(df_ecef[0:5])
# Plot latitude and longitude using ECEF coordinates
plt.plot(df_ecef['ecef_y'], df_ecef['ecef_x'], marker='o', linestyle='', markersize=2)
plt.xlabel('ECEF Y')
plt.ylabel('ECEF X')
plt.title('ECEF X vs ECEF Y')
plt.grid(True)
plt.show()
