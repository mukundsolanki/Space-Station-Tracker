import requests
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import time
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

# Twitter API credentials
bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_position = data['iss_position']
    return float(iss_position['latitude']), float(iss_position['longitude'])

def get_iss_crew():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    return data['people']

def plot_iss_on_map(m, latitude, longitude, icon_path):
    x, y = m(longitude, latitude)
    iss_icon = plt.imread(icon_path)
    imagebox = OffsetImage(iss_icon, zoom=0.1)
    ab = AnnotationBbox(imagebox, (x, y), frameon=False, pad=0)
    m._check_ax().add_artist(ab)

def update_iss_position(m, icon_path, api):
    while True:
        latitude, longitude = get_iss_location()
        crew = get_iss_crew()

        plt.clf()
        m.bluemarble()
        plot_iss_on_map(m, latitude, longitude, icon_path)
        
        title_text = "ISS Location - Latitude: {:.6f}, Longitude: {:.6f}".format(latitude, longitude)
        plt.title(title_text, color='black')

        # Include crew information in the tweet text
        tweet_text = f"{title_text}\n\nCurrent Crew:\n"
        for member in crew:
            tweet_text += f"{member['name']} ({member['craft']})\n"

        # Save the current figure to a file
        plt.savefig('tweet_images/iss_location_map.png')
        media_id = api.media_upload(filename="tweet_images/iss_location_map.png").media_id_string

        # Tweet with both map image and crew information
        client.create_tweet(text=tweet_text, media_ids=[media_id])
        print("Tweet Successful")

        time.sleep(300)

def main():
    fig = plt.figure(figsize=(12, 6))
    m = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.bluemarble()

    latitude, longitude = get_iss_location()
    icon_path = 'images/space-station.png'
    plot_iss_on_map(m, latitude, longitude, icon_path)
    update_iss_position(m, icon_path, api)

if __name__ == "__main__":
    main()
