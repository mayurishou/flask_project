import pandas as pd
from bs4 import BeautifulSoup
import requests

#read data for df
artist_spot = pd.read_csv('data/dane_spotify.csv')
artist_names = list(set(artist_spot['artist']))
artists_count = pd.read_csv('data/df_artists.csv')

def get_artist_photo(artist_name):
    # wikipedia URL for the artist
    artist_name = artist_name.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{artist_name}"

    # GET request to the URL and parse the response
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # finding the element containing the artist's image
    image_element = soup.find("img", class_="thumbimage")

    # returning the image URL if the element was found
    if image_element:
        return image_element["src"]
    else:
        pass

#list of scraped imgs
img_list = []
for artist in artist_names:
    y = get_artist_photo(artist)
    img_list.append(y)

#df of artist's names and scraped imgs
df_artists_img = pd.DataFrame(list(zip(img_list, artist_names)),
              columns =['img', 'artist'])

df_artists_img.to_csv('data/df_artists_1.csv')

