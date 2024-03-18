import pandas as pd
import matplotlib.pyplot as plt
# Read the ASCII file
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
log_headers = []
parsed_data = []
check=[]
# Iterate through each line in the file
for line in data:
    # Split the line into log header and fields
    log_header, fields = line.split(';')
    
    # Remove '#' and split log header into individual fields
    log_header = log_header[1:].split(',')
    # print("log",type(log_header),log_header)
    check_5=log_header[5]
    check_6=log_header[6]
    log_headers.append([check_5,check_6])
   
    # Split the fields into individual data points
    fields = fields.split(',')
    # Extracting required data
    sol_sat = fields[0]
    pos_type = fields[1]
    lat = float(fields[2])
    long = float(fields[3])
    hgt = float(fields[4])
    undulation = float(fields[5])
    datum = fields[6]
    std_lat = float(fields[7])
    std_lon = float(fields[8])
    std_hgt = float(fields[9])
    stn_id = fields[10]
    diff_age = float(fields[11])
    sol_age = float(fields[12])
    svs = int(fields[13])
    solnsvs = int(fields[14])
    solnl1svs = int(fields[15])
    solnmultisvs = int(fields[16])
    reserved = int(fields[17], 16)  # Convert hexadecimal string to integer
    ext_sol_stst = int(fields[18], 16)  # Convert hexadecimal string to integer
    
    # Handle special cases where field may not be an integer
    try:
        galileo = int(fields[19])
    except ValueError:
        galileo = fields[19]
    
    # Store the parsed data in a list
    parsed_data.append([sol_sat, pos_type, lat, long, hgt, undulation, datum, std_lat, std_lon, std_hgt, stn_id, diff_age, sol_age, svs, solnsvs, solnl1svs, solnmultisvs, reserved, ext_sol_stst, galileo])
    # check.append(check_5,check_6)
# Define column names
columns = ['sol_sat', 'pos_type', 'lat', 'long', 'hgt', 'undulation', 'datum', 'std_lat', 'std_lon', 'std_hgt', 'stn_id', 'diff_age', 'sol_age', 'svs', 'solnsvs', 'solnl1svs', 'solnmultisvs', 'reserved', 'ext_sol_stst', 'galileo']
# cols=['check_5','check_6']
# Create pandas DataFrame
df = pd.DataFrame(parsed_data, columns=columns)
df1=pd.DataFrame(log_headers,columns=['check_5','check_6'])
# Plot check_5 and check_6
plt.plot(df['long'], df['lat'], marker='o', linestyle='', markersize=2)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Latitude vs Longitude')
plt.grid(True)
plt.show()
# df1=pd.DataFrame(check,columns=cols)
# Print DataFrame
# print(df[0:5])
# print(df1[0:5])
# print(df1[0:2])
