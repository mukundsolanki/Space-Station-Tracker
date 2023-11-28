import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.animation import FuncAnimation
import numpy as np
import time

def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        iss_position = data['iss_position']
        return float(iss_position['latitude']), float(iss_position['longitude'])
    except Exception as e:
        print(f"Error fetching ISS location: {e}")
        return None

def update_iss_position(num, marker):
    iss_location = get_iss_location()
    if iss_location:
        marker.set_data(*iss_location)
        plt.title(f"ISS Location\nLatitude: {iss_location[0]}, Longitude: {iss_location[1]}")
    return marker,

def main():
    fig, ax = plt.subplots(figsize=(10, 10))

    # Create a basemap centered around the initial ISS location
    initial_location = get_iss_location()
    if initial_location is None:
        return

    m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=80,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')
    m.drawcoastlines()
    m.drawparallels(np.arange(-90, 91, 30))
    m.drawmeridians(np.arange(-180, 181, 60))
    m.drawmapboundary(fill_color='aqua')

    marker, = m.plot(*initial_location, 'ro', markersize=8)

    ani = FuncAnimation(fig, update_iss_position, fargs=(marker,), interval=5000)

    plt.show()

if __name__ == "__main__":
    main()
