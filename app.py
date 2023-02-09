from flask import Flask, render_template
import pandas as pd

#$env:FLASK_DEBUG = "1"

app = Flask(__name__)


#zad5
@app.route('/')
def display_artists():

    df = pd.read_csv('data/display_artists.csv')
    df = df
    
    return render_template('artist_list.html', df = df)


#zad6
@app.route('/display_songs/<artist>')
def display_songs(artist):

    df = pd.read_csv('data/dane_spotify.csv')
    df1 = df[df['artist']==artist]
    df1=df1

    df2 = pd.read_csv('data/df_artists_1.csv')
    df3 = df2[df2['artist']==artist]
    df3 = df3

    return render_template('songs_list.html', df1 = df1, df3 = df3)


#zad7
@app.route('/display_songs/display_lyrics/<title>')
def display_lyrics(title):

    df = pd.read_csv('data/dane_spotify.csv')
    df1 = df[df['title']==title]
    df1=df1

    return render_template('lyrics.html', df1 = df1)




