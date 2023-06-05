from flask import Flask, render_template, redirect
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import spotipy
import requests, os, base64
from dotenv import load_dotenv
from urllib.parse import urlencode


scope="user-library-modify"

render = render_template
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render('index.html')

if __name__ == "__main__":
    app.run(debug=True)