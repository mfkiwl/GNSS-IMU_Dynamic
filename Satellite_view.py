import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import folium
from pyproj import Proj, transform
# Read data from the text file
data = []
with open('/Users/ravitejakunchanapalli/Downloads/sd-stdmod-dev.txt', 'r') as file:
    for line in file:
        values = line.strip().strip('[],').split(',')
        data.append([float(val) for val in values])

# Extract latitude, longitude, and standard deviations
latitudes = [row[0] for row in data]
longitudes = [row[1] for row in data]
print(type(latitudes))
# Create a folium map and add the LLA points
m = folium.Map(
    location=[np.mean(latitudes), np.mean(longitudes)], 
    zoom_start=18,  # Set the zoom level similar to Google Maps
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google'
)

for lat, lon in zip(latitudes, longitudes):
    folium.CircleMarker(
        location=[lat, lon],
        radius=1,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Save the map as an HTML file
m.save('/Users/ravitejakunchanapalli/Desktop/org.html')

plt.show()


#########################       Distance between two Consecutive points       ################################

# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.pyplot as plt
# import folium
# from pyproj import Proj, transform
# import math

# # Function to calculate distance between two points using Haversine formula
# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371.0  # Radius of the Earth in kilometers

#     # Convert latitude and longitude from degrees to radians
#     lat1_rad = math.radians(lat1)
#     lon1_rad = math.radians(lon1)
#     lat2_rad = math.radians(lat2)
#     lon2_rad = math.radians(lon2)

#     # Compute differences in latitude and longitude
#     dlat = lat2_rad - lat1_rad
#     dlon = lon2_rad - lon1_rad

#     # Haversine formula
#     a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

#     # Calculate distance
#     distance = R * c
#     return distance

# # Read data from the text file
# data = []
# with open('/Users/ravitejakunchanapalli/Downloads/sd-stdmod-dev.txt', 'r') as file:
#     for line in file:
#         values = line.strip().strip('[],').split(',')
#         data.append([float(val) for val in values])

# # Extract latitude, longitude, and standard deviations
# latitudes = [row[0] for row in data]
# longitudes = [row[1] for row in data]

# distances = []
# for i in range(len(latitudes) - 1):
#     lat1, lon1 = latitudes[i], longitudes[i]
#     lat2, lon2 = latitudes[i + 1], longitudes[i + 1]
#     dist = haversine(lat1, lon1, lat2, lon2)
#     distances.append(dist)

# # Calculate mean distance
# mean_distance = sum(distances) / len(distances)
# mean_m=mean_distance*1000
# mean_cm=mean_m*100
# print("Mean distance between consecutive coordinates:", mean_m, "m")

# # Create a folium map and add the LLA points
# m = folium.Map(
#     location=[np.mean(latitudes), np.mean(longitudes)], 
#     zoom_start=18,  # Set the zoom level similar to Google Maps
#     tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
#     attr='Google'
# )

# for lat, lon in zip(latitudes, longitudes):
#     folium.CircleMarker(
#         location=[lat, lon],
#         radius=1,
#         color='blue',
#         fill=True,
#         fill_color='blue'
#     ).add_to(m)

# # Save the map as an HTML file
# m.save('/Users/ravitejakunchanapalli/Desktop/mod.html')
# plt.show()
















#########################       Completed       ################################
# std_latitudes = [row[2] for row in data]
# std_longitudes = [row[3] for row in data]
# percentage_changes = [(row[-1] - row[-2]) / row[-2] * 100 for row in data]

# # Calculate the average of latitude and longitude standard deviations
# avg_std = [(std_lat + std_lon) / 2 for std_lat, std_lon in zip(std_latitudes, std_longitudes)]

# # Normalize the average standard deviations for coloring
# min_avg_std = min(avg_std)
# max_avg_std = max(avg_std)
# norm_avg_std = [(std - min_avg_std) / (max_avg_std - min_avg_std) for std in avg_std]

# # Create scatter plot
# plt.figure(figsize=(20, 10))
# plt.subplot(121)
# plt.scatter(longitudes, latitudes, c=norm_avg_std, s=10, cmap='RdYlGn_r', label='Average Std Dev')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Geographical Data Visualization with Average Standard Deviation')
# plt.colorbar(label='Normalized Average Standard Deviation')

# # Find and annotate max and min standard deviations
# max_std_index = avg_std.index(max(avg_std))
# min_std_index = avg_std.index(min(avg_std))
# plt.annotate(f'Max Std: {avg_std[max_std_index]:.4f}', (longitudes[max_std_index], latitudes[max_std_index]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
# plt.annotate(f'Min Std: {avg_std[min_std_index]:.4f}', (longitudes[min_std_index], latitudes[min_std_index]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)

# plt.legend()
# plt.grid()

# percentage_changes = [(row[-1] - row[-2]) / row[-2] * 100 for row in data]

# # Normalize the percentage changes for coloring
# min_pc = min(percentage_changes)
# max_pc = max(percentage_changes)
# norm_pc = [(pc - min_pc) / (max_pc - min_pc) for pc in percentage_changes]

# plt.subplot(122)
# plt.scatter(longitudes, latitudes, c=norm_pc, s=5, cmap='RdYlGn_r', label='% Change')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Geographical Data Visualization with Satellite Coverage %')
# plt.colorbar(label='Satellite Coverage')
# # plt.legend()
# plt.grid()
# plt.show()
