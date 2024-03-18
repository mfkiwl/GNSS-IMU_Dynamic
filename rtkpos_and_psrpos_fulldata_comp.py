import matplotlib.pyplot as plt
import numpy as np
# Read data from the psrpos ascii
file_path1= "/Users/ravitejakunchanapalli/Downloads/org_RTKPOS.ASCII"
with open(file_path1, 'r') as file1:
    data1= file1.readlines()

# Read data from the rtkpos ascii
file_path2= "/Users/ravitejakunchanapalli/Downloads/org_PSRPOS.ASCII"
with open(file_path2, 'r') as file2:
    data2= file2.readlines()

# Initialize lists to store parsed data
rtk_latitudes = []
rtk_longitudes = []
rtk_std_latitudes=[]
rtk_std_longitudes=[]
psr_latitudes = []
psr_longitudes = []
psr_std_latitudes=[]
psr_std_longitudes=[]

# Iterate through each line in the file
for line in data1:
    # Split the line into log header and fields
    log_header, fields = line.split(';')

    # Split the fields into individual data points
    fields = fields.split(',')

    # Extracting relevant data (latitude, longitude)
    lat = float(fields[2])
    lon = float(fields[3])

    std_latitude = float(fields[7])
    std_longitude = float(fields[8])
    # Store the parsed data in lists

    rtk_latitudes.append(lat)
    rtk_longitudes.append(lon)
    rtk_std_latitudes.append(std_latitude)
    rtk_std_longitudes.append(std_longitude)
std_dev_lat_rtk=np.std(rtk_std_latitudes)
std_dev_lon_rtk=np.std(rtk_std_longitudes)
print("rtk_lat_mean",np.std(rtk_std_latitudes))
# Iterate through each line in the file
for line in data2:
    # Split the line into log header and fields
    log_header, fields = line.split(';')

    # Split the fields into individual data points
    fields = fields.split(',')

    # Extracting relevant data (latitude, longitude)
    lat = float(fields[2])
    lon = float(fields[3])

    std_latitude = float(fields[7])
    std_longitude = float(fields[8])
    # Store the parsed data in lists

    psr_latitudes.append(lat)
    psr_longitudes.append(lon)
    psr_std_latitudes.append(std_latitude)
    psr_std_longitudes.append(std_longitude)
   
print("psr_lat_mean",np.std(psr_std_latitudes))
std_dev_lat_psr=np.std(psr_std_latitudes)
std_dev_lon_psr=np.std(psr_std_longitudes)
# Plotting Latitude 
plt.subplot(2, 2, 1)  # (rows, columns, plot_number)
plt.plot(psr_latitudes, label=f'PSR Pos (lat)\n, Std Dev: {std_dev_lat_psr}')
plt.plot(rtk_latitudes, label=f'RTK Pos (lat)\n Std Dev: {std_dev_lat_rtk}')

plt.xlabel('Data Point')
plt.ylabel('Latitude')
plt.title('Latitude Values Comparison')
plt.legend()


# Plotting Longitude
plt.subplot(2, 2, 2)  # (rows, columns, plot_number)
plt.plot(psr_longitudes, label=f'PSR Pos (lat)\n, Std Dev: {std_dev_lon_psr}')
plt.plot(rtk_longitudes, label=f'RTK Pos (lat)\n Std Dev: {std_dev_lon_rtk}')

plt.xlabel('Data Point')
plt.ylabel('Longitude')
plt.title('Longitude Values Comparison')
plt.legend()


plt.subplot(2, 2, 3)  # (rows, columns, plot_number)
plt.plot(psr_std_latitudes, label='psr_lat_std')
plt.plot(rtk_std_latitudes, label='rtk_lat_std')

plt.xlabel('Data Point')
plt.ylabel('Latitude std')
plt.title('Latitude std Values Comparison')
plt.legend()


plt.subplot(2, 2, 4)  # (rows, columns, plot_number)
plt.plot(psr_std_longitudes, label='psr_lon_std')
plt.plot(rtk_std_longitudes, label='rtk_lon_std')

plt.xlabel('Data Point')
plt.ylabel('Longitude std')
plt.title('Longitude std Values Comparison')
plt.legend()


plt.tight_layout()  # Adjust subplot parameters to give specified padding
plt.show()





