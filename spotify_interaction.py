# Common Spotify code

import spotipy, os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Setting scopes exclusively for playlist and saved songs tinkering
scope = "user-library-modify user-library-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"

# Setting up Spotipy's env app variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_url = os.getenv("SPOTIPY_REDIRECT_URI")

# Setting up Spotify API calls
spotify_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_url, scope=scope)
spotify_api = spotipy.Spotify(auth_manager=spotify_oauth)

# ---
# Spotify functions

# Get login URL
def spotify_login(): return spotify_oauth.get_authorize_url()