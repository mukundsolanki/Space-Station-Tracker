import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import time

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_position = data['iss_position']
    return float(iss_position['latitude']), float(iss_position['longitude'])

def plot_iss_on_map(m, latitude, longitude):
    x, y = m(longitude, latitude)
    m.plot(x, y, 'ro', markersize=12, label='ISS Position')
    plt.legend()

def update_iss_position(m):
    while True:
        latitude, longitude = get_iss_location()
        plt.clf()
        m.bluemarble()
        plot_iss_on_map(m, latitude, longitude)
        plt.pause(5)  # Pause for 5 seconds before updating

def main():
    fig = plt.figure(figsize=(12, 6))
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.bluemarble()

    latitude, longitude = get_iss_location()
    plot_iss_on_map(m, latitude, longitude)

    update_iss_position(m)

if __name__ == "__main__":
    main()
