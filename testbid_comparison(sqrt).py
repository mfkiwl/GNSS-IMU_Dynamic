import matplotlib.pyplot as plt
import math
# Read data from the text file
data = []
with open('/Users/ravitejakunchanapalli/Downloads/sd-stdorg_dev.txt', 'r') as file:
    for line in file:
        values = line.strip().strip('[],').split(',')
        data.append([float(val) for val in values])
print(len(data[0]))
# Extract latitude, longitude, and standard deviations
latitudes = [row[0] for row in data]
longitudes = [row[1] for row in data]
std_latitudes = [row[2] for row in data]
std_longitudes = [row[3] for row in data]
percentage_changes = [(row[-1] - row[-2]) / row[-2] * 100 for row in data]
print("lat len",len(latitudes))
print("lon len",len(longitudes))

# Calculate the average of latitude and longitude standard deviations

#avg_std = [(std_lat + std_lon) / 2 for std_lat, std_lon in zip(std_latitudes, std_longitudes)]
avg_std = [math.sqrt((std_lat**2)+ (std_lon**2)) for std_lat, std_lon in zip(std_latitudes, std_longitudes)]
print("avg len",len(avg_std))

print("min(avg_std)",min(avg_std))
print("max",max(avg_std))
# Normalize the average standard deviations for coloring
min_avg_std = min(avg_std)
max_avg_std = max(avg_std)
norm_avg_std = [(std - min_avg_std) / (max_avg_std - min_avg_std) for std in avg_std]
print("min",min(norm_avg_std))
print("max",max(norm_avg_std))
# Create scatter plot
plt.figure(figsize=(20, 10))
plt.subplot(121)
plt.scatter(longitudes, latitudes, c=avg_std, s=10, cmap='RdYlGn_r', label='Average Std Dev')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Data Visualization with Average Standard Deviation')
plt.colorbar(label='Normalized Average Standard Deviation')

# Find and annotate max and min standard deviations
max_std_index = avg_std.index(max(avg_std))
min_std_index = avg_std.index(min(avg_std))
plt.annotate(f'Max Std: {avg_std[max_std_index]:.4f}', (longitudes[max_std_index], latitudes[max_std_index]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)
plt.annotate(f'Min Std: {avg_std[min_std_index]:.4f}', (longitudes[min_std_index], latitudes[min_std_index]), textcoords="offset points", xytext=(5,5), ha='center', fontsize=8)

plt.legend()
plt.grid()

percentage_changes = [(row[-1] - row[-2]) / row[-2] * 100 for row in data]

# Normalize the percentage changes for coloring
min_pc = min(percentage_changes)
max_pc = max(percentage_changes)
norm_pc = [(pc - min_pc) / (max_pc - min_pc) for pc in percentage_changes]

plt.subplot(122)
plt.scatter(longitudes, latitudes, c=norm_pc, s=5, cmap='RdYlGn_r', label='% Change')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Data Visualization with Satellite Coverage %')
plt.colorbar(label='Satellite Coverage')
# plt.legend()
plt.grid()
plt.show()
