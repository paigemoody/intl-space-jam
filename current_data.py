import requests
import json
import spotipy
import spotipy.util as util
from spotipy import oauth2
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials


SPOTIFY_CLIENT_ID= os.environ['spotify_client_id']
SPOTIFY_CLIENT_SECRET = os.environ['spotify_client_secret']

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                      client_secret=SPOTIFY_CLIENT_SECRET)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_current_lng_lat():
    """
    Get dict of current time and [lng, lat] of the ISS as a dict

    { unix_time_stamp : [lng ,lat] }

    """
    
    current_data = requests.get("http://api.open-notify.org/iss-now.json")

    current_data = current_data.json()

    timestamp = current_data['timestamp']

    latitude = current_data['iss_position']['latitude']

    longitude = current_data['iss_position']['latitude']

    return { timestamp : [ longitude, latitude ] }


def get_spotify_data(playlist_id):

    top_playlist_id = playlist_id
    
    results = spotify.search(q='playlist:' + top_playlist_id, type='playlist')

    # print("results", results)

    # owner_id= results['playlists']['items'][0]['owner']['id']

    owner_id = "spotifycharts"

    playlist_tracks = spotify.user_playlist_tracks(owner_id, top_playlist_id, fields='items,uri,name,id,total')

    top_song_data = playlist_tracks['items'][0]

    top_song_name = top_song_data['track']['name']

    artists_data = top_song_data['track']['artists']

    artists_list = []

    for artist in artists_data:
        artists_list.append(artist['name'])

    return( { top_song_name : artists_list } )

print("Argentina:", get_spotify_data('37i9dQZEVXbMMy2roB9myp'))

print("Egypt:", get_spotify_data('37i9dQZF1DX50MDbDwt4w8'))

print("Tunisia:", get_spotify_data('37i9dQZF1DX9TaUKtmYQ2X'))

print("Bahrain:", get_spotify_data('598uA4ClNJ0tGoAmrGTP2S'))





