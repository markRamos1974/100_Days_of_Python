from dotenv import load_dotenv
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

class SpotifyManager:
    def __init__(self):
        self.CLIENT_ID = os.environ.get("CLIENT_ID")
        self.CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
        self.USERNAME = os.environ.get("USERNAME")
        self.REDIRECT_URI = os.environ.get("REDIRECT_URI")
        self.state = "3hg2g3d7etr3"
        # self.authorize_user()

        print("Authenticating...")
        self.scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"
        self.spotify = spotipy.Spotify(
                auth_manager=SpotifyOAuth(
                client_id=self.CLIENT_ID,
                client_secret=self.CLIENT_SECRET,
                scope=self.scope,
                redirect_uri=self.REDIRECT_URI

            )
        )
        print("Authentication success...")
        self.user_id = self.spotify.current_user()["id"]

        

    def create_playlist(self, playlist_name): 
       print("creating playlist...")
       new_playlist = self.spotify.user_playlist_create(user=self.user_id, name=playlist_name, public=False, description="playlist automation")
       return new_playlist["id"]
    
    def add_to_playlist(self, playlist_id, songs):
        track_uri_list = self.search_songs(songs)

        print("adding songs to playlist")
        self.spotify.playlist_add_items(playlist_id=playlist_id, items=track_uri_list)
    
    def search_songs(self, song_titles):
        track_uri_list = []
        
        print("searching songs from scraped data...")
        for title in song_titles:
            response = self.spotify.search(q=title, limit=1, type="track")
            track_uri = response["tracks"]["items"][0]["uri"]
            track_uri_list.append(track_uri)
        
        return track_uri_list