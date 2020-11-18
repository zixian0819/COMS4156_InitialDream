from flask import Blueprint
from flask import Flask, jsonify
from flask_googlemaps import GoogleMaps
import requests

app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"

# Initialize the extension
GoogleMaps(app)

import googlemaps

API_KEY = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"


bp = Blueprint('locate', __name__,url_prefix='/locate')

@bp.route('/locate', methods=('GET', 'POST'))
def locate():
    gmaps = googlemaps.Client(key=API_KEY)
    locations = gmaps.geolocate()
    latitude = locations['location']['lat']
    longitude = locations['location']['lng']

    # api-endpoint
    URL = "https://revgeocode.search.hereapi.com/v1/revgeocode"
    # API key
    api_key = 'jpDAhF_gyaj_2SgWcXsvAnYGw8ssVc6RnkLjufLyQh4'
    # Defining a params dictionary for the parameters to be sent to the API
    PARAMS = {
        'at': '{},{}'.format(latitude, longitude),
        'apikey': api_key
    }
    # Sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # Extracting data in json format
    data = r.json()

    # Taking out title from JSON
    address = data['items'][0]['title']

    return address

def locate2():
    gmaps = googlemaps.Client(key=API_KEY)
    locations = gmaps.geolocate()
    latitude = locations['location']['lat']
    longitude = locations['location']['lng']

    return latitude, longitude
