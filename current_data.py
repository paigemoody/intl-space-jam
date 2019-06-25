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


def get_spotify_data():

    top_US_playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
    
    results_US = spotify.search(q='playlist:' + top_US_playlist_id, type='playlist')

    owner_id_US= results_US['playlists']['items'][0]['owner']['id']

    playlist_tracks_US = spotify.user_playlist_tracks(owner_id_US, top_US_playlist_id, fields='items,uri,name,id,total')

    top_song_US_data = playlist_tracks_US['items'][0]

    top_US_song_name = top_song_US_data['track']['name']

    artists_data = top_song_US_data['track']['artists']

    artists_list = []

    for artist in artists_data:
        artists_list.append(artist['name'])

    return( { top_US_song_name : artists_list } )

print(get_spotify_data())



