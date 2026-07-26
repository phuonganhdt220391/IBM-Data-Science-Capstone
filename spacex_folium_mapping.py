# spacex_folium_mapping.py
import folium
from folium.plugins import MarkerCluster

print("Initializing Folium map generator...")

# Create map centered around US launch coordinates
spacex_map = folium.Map(location=[28.573255, -80.646895], zoom_start=5)

# Add marker cluster for launch sites
marker_cluster = MarkerCluster().add_to(spacex_map)

# Example marker for CCAFS LC-40
folium.Marker(
    location=[28.5618571, -80.577366],
    popup='CCAFS LC-40',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(marker_cluster)

spacex_map.save("spacex_launch_map.html")
print("Interactive Folium map saved as 'spacex_launch_map.html'.")