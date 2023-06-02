# Common Spotify code

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setting scopes exclusively for playlist and saved songs tinkering
scope="user-library-modify user-library-read playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"

# Setting up Spotipy's env app variables
SPOTIPY_CLIENT_ID='c04e8e4077284bd8902ea1ab7768da5d'
SPOTIPY_CLIENT_SECRET='ea3363bbfe944333afe32f9ea9538438'
SPOTIPY_REDIRECT_URI='http://localhost:5000/callback'

# Setting up Spotify API calls
spotify_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope)
spotify_api = spotipy.Spotify(auth_manager=spotify_oauth)

# ---
# Spotify functions

# Get login URL
def spotify_login(): return spotify_oauth.get_authorize_url()