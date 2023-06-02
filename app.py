from flask import Flask, render_template
from spotipy.oauth2 import SpotifyOAuth

scope="user-library-modify"

render = render_template
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render('index.html'
)