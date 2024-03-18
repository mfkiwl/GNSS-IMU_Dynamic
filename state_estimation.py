from filterpy.kalman import KalmanFilter
import numpy as np

# Create a Kalman filter for LLA data
kf = KalmanFilter(dim_x=3, dim_z=3)  # State: [latitude, longitude, altitude], Measurement: [latitude, longitude, altitude]
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize lists to store parsed data
latitudes = []
longitudes = []
heights = []
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
# Initialize the Kalman filter
initial_state = np.array([latitudes[0], longitudes[0], heights[0]])
print(initial_state)
print(latitudes[1],longitudes[1],heights[1])
kf.x = initial_state

# Define state transition matrix (process model)
dt = 1.0  # Time step
kf.F = np.eye(3)  # Assume no changes in position over time

# Define measurement function (measurement model)
kf.H = np.eye(3)

# Define measurement noise covariance matrix
measurement_noise_variance = 1.0  # Adjust according to the noise level in your measurements
kf.R = np.eye(3) * measurement_noise_variance

# Define process noise covariance matrix
process_noise_variance = 0.1  # Adjust according to the dynamics of your system
kf.Q = np.eye(3) * process_noise_variance

# Process each sample of LLA data
ila_data=[[latitudes[0], longitudes[0], heights[0]],
          [latitudes[1], longitudes[1], heights[1]],
          [latitudes[2], longitudes[2], heights[2]]]
estimated_states = []
for sample in ila_data:
    # Predict the next state based on the process model
    kf.predict()

    # Update the state estimate based on the current measurement
    kf.update(sample)

    # Retrieve the estimated state
    estimated_states.append(kf.x)

# Convert estimated states to numpy array
estimated_states = np.array(estimated_states)

# Print the estimated states
print("Estimated States (latitude, longitude, altitude):")
for state in estimated_states:
    print(state)