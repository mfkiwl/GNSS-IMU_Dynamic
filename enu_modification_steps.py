import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

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

# Function to convert ECEF to ENU
def ecef_to_enu(x, y, z, ref_x, ref_y, ref_z):
    # Calculate displacement vector
    dx = x - ref_x
    dy = y - ref_y
    dz = z - ref_z
    
    # Convert reference point to ENU
    phi = np.arctan2(ref_z, np.sqrt(ref_x**2 + ref_y**2))
    lam = np.arctan2(ref_y, ref_x)
    # ref_e = -np.sin(lam) * dx + np.cos(lam) * dy
    # ref_n = -np.sin(phi) * np.cos(lam) * dx - np.sin(phi) * np.sin(lam) * dy + np.cos(phi) * dz
    # ref_u = np.cos(phi) * np.cos(lam) * dx + np.cos(phi) * np.sin(lam) * dy + np.sin(phi) * dz
    
    # Convert displacement vector to ENU
    east = -np.sin(lam) * dx + np.cos(lam) * dy
    north = -np.sin(phi) * np.cos(lam) * dx - np.sin(phi) * np.sin(lam) * dy + np.cos(phi) * dz
    up = np.cos(phi) * np.cos(lam) * dx + np.cos(phi) * np.sin(lam) * dy + np.sin(phi) * dz
    
    return east, north, up

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

# Convert ECEF to ENU
window_size = 10  # Define window size for moving average
rolling_mean = df_ecef.rolling(window=window_size).mean().dropna()
# Calculate reference point as the rolling mean
reference_point = rolling_mean.iloc[0]  
# Apply ECEF to ENU conversion using the reference point
df_enu = df_ecef.apply(lambda row: ecef_to_enu(row['ecef_x'], row['ecef_y'], row['ecef_z'], reference_point['ecef_x'], reference_point['ecef_y'], reference_point['ecef_z']), axis=1)

# Create DataFrame for ENU coordinates
enu_columns = ['east', 'north', 'up']
df_enu = pd.DataFrame(df_enu.tolist(), columns=enu_columns)


plt.scatter(df_enu['east'], df_enu['north'])
plt.xlabel('east')
plt.ylabel('North')
plt.title('east vs North')
plt.grid(True)
plt.show()

