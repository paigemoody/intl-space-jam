from flask import Flask, render_template, redirect, request, flash, session, jsonify, send_file

from current_data import get_song_from_country

import json
import os


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ['flask_session_key']


@app.route('/')
def index():
    """Homepage."""
    return render_template("base.html")


@app.route('/top_song/<country_name>')
def get_top_song(country_name):

    song_data = get_song_from_country(country_name)

    print("country_name:", country_name)

    return jsonify(song_data)



if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug
    app.run(port=5000, host='0.0.0.0')
