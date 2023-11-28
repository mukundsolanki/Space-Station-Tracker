import requests
import folium
from folium import Marker

def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        iss_position = data['iss_position']
        return float(iss_position['latitude']), float(iss_position['longitude'])
    except Exception as e:
        print(f"Error fetching ISS location: {e}")
        return None

def main():
    # Create a folium map centered around the initial ISS location
    initial_location = get_iss_location()
    if initial_location is None:
        return

    map_iss = folium.Map(location=initial_location, zoom_start=2)

    # Continuously update the ISS location on the map
    while True:
        iss_location = get_iss_location()

        if iss_location:
            # Clear previous ISS marker
            map_iss = folium.Map(location=iss_location, zoom_start=2)

            # Add a new marker for the current ISS location
            Marker(location=iss_location, popup="ISS").add_to(map_iss)

            # Save the map as an HTML file
            map_iss.save("iss_map.html")

if __name__ == "__main__":
    main()
