# Use "flask run" to initialize the local server
# ---

from flask import Flask, render_template, redirect, request
from spotify_interaction import spotify_login

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

# Runs Flask app when the Python script is opened directly
if __name__ == '__main__':
    app.run(debug=True)