import folium

# Load data from file
file_path = "/Users/ravitejakunchanapalli/Downloads/RTKdemo_file.ASCII"
with open(file_path, 'r') as file:
    data = file.readlines()

# Initialize a Folium map centered on the first coordinate
lat, lon = map(float, data[0].split(';')[1].split(',')[2:4])
center = [lat, lon]

mymap = folium.Map(location=center, zoom_start=10, tiles='OpenStreetMap')

# Parse data from file and add markers to the map
for line in data:
    fields = line.split(';')[1].split(',')
    lat, lon = map(float, fields[2:4])
    folium.CircleMarker(location=[lat, lon], radius=5, color='blue', fill=True, fill_color='blue').add_to(mymap)

# Save the map as an HTML file
output_file_path = '/Users/ravitejakunchanapalli/Downloads/11original_coordinates_map.html'
mymap.save(output_file_path)

print("Map saved successfully.")
