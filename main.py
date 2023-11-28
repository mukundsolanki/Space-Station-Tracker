import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_position = data['iss_position']
    return float(iss_position['latitude']), float(iss_position['longitude'])

def plot_iss_on_map(m, latitude, longitude, icon_path):
    x, y = m(longitude, latitude)

    # Load the ISS icon image
    iss_icon = plt.imread(icon_path)
    imagebox = OffsetImage(iss_icon, zoom=0.1)

    # Create an annotation box at the ISS position
    ab = AnnotationBbox(imagebox, (x, y), frameon=False, pad=0)
    m._check_ax().add_artist(ab)

def update_iss_position(m, icon_path):
    while True:
        latitude, longitude = get_iss_location()
        plt.clf()
        m.bluemarble()
        plot_iss_on_map(m, latitude, longitude, icon_path)
        
        title_text = "ISS Location - Latitude: {:.6f}, Longitude: {:.6f}".format(latitude, longitude)
        plt.title(title_text, color='black')

        plt.pause(5)

def main():
    fig = plt.figure(figsize=(12, 6))
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.bluemarble()

    latitude, longitude = get_iss_location()
    icon_path = 'space-station.png'
    plot_iss_on_map(m, latitude, longitude, icon_path)
    update_iss_position(m, icon_path)

if __name__ == "__main__":
    main()
