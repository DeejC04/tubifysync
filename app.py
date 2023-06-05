from flask import Flask, render_template, redirect, request, jsonify
from spotify_interaction import spotify_login
import json

# Sets the user's Spotify key as null by default
spotify_key = None

# Flask boilerplate
render = render_template
app = Flask(__name__)

# Main page @ root
@app.route("/")
def landing_page():
    return render("index.html")

# Spotify login page link
@app.route("/spotify_login")
def spotify_login_page():
    return redirect(spotify_login())

# Spotify callback handling
@app.route("/callback")
def spotify_callback_landing_page():
    global spotify_key # Need to edit the global variable so the value is accessible inside landing_page()
    spotify_key=request.args.get("code") # Parses the suffix from the callback URL as the Spotify API key
    return redirect("/")

# Allows Flask to access the spotify_key variable (also converts it to JSON)
@app.route("/get_spotify_key")
def get_spotify_key():
    global spotify_key
    return jsonify(spotify_key=spotify_key)

# Runs Flask app when the Python script is opened directly
if __name__ == '__main__':
    app.run(debug=True)