import pandas as pd

#reading data from assignment's file
all_data = pd.read_csv('data/dane_spotify.csv')

#creating df with counter column
artists_list = all_data[['artist']].drop_duplicates()
artists_counter = all_data[['title', 'artist']].groupby('artist').count()
artists_counter['counter'] = artists_counter[['title']]

#reading data from csv file created in webcraper 
artists_imgs = pd.read_csv('data/df_artists_1.csv')

#preparing data and merging
imgs = artists_imgs.iloc[:,1]
artists_counters = artists_list.join(artists_counter, on='artist')
artists_counters1 = artists_counters[['artist', 'counter']].astype(str)
artists_imgs1 = artists_imgs[['artist', 'img']].astype(str)
artists_counters_imgs = artists_counters1.merge(artists_imgs1, on='artist')

#creating csv file for route ('/') 
artists_counters_imgs.to_csv('data/display_artists.csv')

