import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


def extract_data_from_excel(file_path, column_name):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        # Extract data from the specified column
        latitude_data = df[column_name].tolist()
        return latitude_data
    except Exception as e:
        print("An error occurred:", e)


def compute_stats(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return mean, std_dev

# Example usage:
file_path1= '/Users/ravitejakunchanapalli/Downloads/bestpos.xlsx'
file_path2= '/Users/ravitejakunchanapalli/Downloads/gnsspos.xlsx' 

verify="lat"
latitude_best = extract_data_from_excel(file_path1, verify)
latitude_gnss=  extract_data_from_excel(file_path2, verify)

verify="lon"
longitude_best = extract_data_from_excel(file_path1,verify)
longitude_gnss = extract_data_from_excel(file_path2,verify)

# Computing statistics for latitude
mean_lat_best, std_dev_lat_best = compute_stats(latitude_best)
mean_lat_gnss, std_dev_lat_gnss = compute_stats(latitude_gnss)

# Computing statistics for longitude
mean_lon_best, std_dev_lon_best = compute_stats(longitude_best)
mean_lon_gnss, std_dev_lon_gnss = compute_stats(longitude_gnss)

verify="lat ?"
latitude_best_std = extract_data_from_excel(file_path1, verify)
lat_best_std=np.std(latitude_best_std)
latitude_gnss_std=  extract_data_from_excel(file_path2, verify)
lat_gnss_std=np.std(latitude_gnss_std)
verify="lon ?"
longitude_best_std = extract_data_from_excel(file_path1,verify)
lon_best_std=np.std(longitude_best_std)
longitude_gnss_std = extract_data_from_excel(file_path2,verify)
lon_gnss_std=np.std(longitude_gnss_std)

# Plotting Latitude
plt.subplot(2, 2, 1)  # (rows, columns, plot_number)
plt.plot(latitude_best, label=f'Best Pos (lat)\nMean: {mean_lat_best}, Std Dev: {lat_best_std}')
plt.plot(latitude_gnss, label=f'GNSS Pos (lat)\nMean: {mean_lat_gnss}, Std Dev: {lat_gnss_std}')
plt.xlabel('Data Point')
plt.ylabel('Latitude')
plt.title('Latitude Values Comparison')
plt.legend()


# Plotting Longitude
plt.subplot(2, 2, 2)  # (rows, columns, plot_number)
plt.plot(longitude_best, label=f'Best Pos (lon)\nMean: {mean_lon_best}, Std Dev: {lon_best_std}')
plt.plot(longitude_gnss, label=f'GNSS Pos (lon)\nMean: {mean_lon_gnss}, Std Dev: {lon_gnss_std}')
plt.xlabel('Data Point')
plt.ylabel('Longitude')
plt.title('Longitude Values Comparison')
plt.legend()


plt.subplot(2, 2, 3)  # (rows, columns, plot_number)
plt.plot(latitude_best_std, label='Best Pos (lat_std)')
plt.plot(latitude_gnss_std, label='GNSS Pos (lat_std)')
plt.xlabel('Data Point')
plt.ylabel('Latitude std')
plt.title('Latitude std Values Comparison')
plt.legend()


plt.subplot(2, 2, 4)  # (rows, columns, plot_number)
plt.plot(longitude_best_std, label='Best Pos (lon_std)')
plt.plot(longitude_gnss_std, label='GNSS Pos (lon_std)')
plt.xlabel('Data Point')
plt.ylabel('Longitude std')
plt.title('Longitude std Values Comparison')
plt.legend()


 # Adjust subplot parameters to give specified padding
plt.show()









