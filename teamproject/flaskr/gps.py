from flask import Flask
from flask_googlemaps import GoogleMaps
import googlemaps
app = Flask(__name__)

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"

# Initialize the extension
GoogleMaps(app)
API_KEY = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"


def locate2():
    gmaps = googlemaps.Client(key=API_KEY)
    locations = gmaps.geolocate()
    latitude = locations['location']['lat']
    longitude = locations['location']['lng']

    return latitude, longitude
