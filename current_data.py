import requests
import json
import spotipy
import spotipy.util as util
from spotipy import oauth2
import os
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# from shapely.geometry import Polygon, Point, MultiPloygon

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

    longitude = current_data['iss_position']['longitude']

    return { "timestamp": timestamp,  "coords" : [ float(longitude), float(latitude) ] }


def get_playlist_id_from_country_name(country_name):

    """Given country name return playlist id"""

    with open('data/spotify_country_playlist_ids.json') as country_data:
        country_data = json.load(country_data)

        # if country does not have a spotify playlist return global top 50 playlist id
        if country_name not in country_data:

          return { 'country' : 'Global', 'playlist_id' : country_data['Global']['playlist_id']}

    return { 'country' : country_name, 
             'playlist_id' : country_data[country_name]['playlist_id'],
             'playlist_url' : country_data[country_name]['url']}


def get_spotify_data(playlist_id):

    top_playlist_id = playlist_id
    
    results = spotify.search(q='playlist:' + top_playlist_id, type='playlist')

    owner_id = "spotifycharts"

    playlist_tracks = spotify.user_playlist_tracks(owner_id, top_playlist_id, fields='items,uri,name,id,total')

    top_song_data = playlist_tracks['items'][0]

    top_song_name = top_song_data['track']['name']

    artists_data = top_song_data['track']['artists']

    artists_list = []

    for artist in artists_data:
        artists_list.append(artist['name'])

    return( { 'song': top_song_name, 'artists' : artists_list } )


def get_song_from_country(country_name):
    """Given [long, lat], get country."""

    playlist_data = get_playlist_id_from_country_name(country_name)

    playlist_id = playlist_data['playlist_id']

    top_song_data = get_spotify_data(playlist_id)

    playlist_data['song'] = top_song_data['song']
    playlist_data['artists'] = top_song_data['artists']

    return playlist_data




