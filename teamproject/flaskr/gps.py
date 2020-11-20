"""gps"""
from flask import Flask
from flask_googlemaps import GoogleMaps
import googlemaps
APP = Flask(__name__)

# you can set key as config
APP.config['GOOGLEMAPS_KEY'] = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"

# Initialize the extension
GoogleMaps(APP)
API_KEY = "AIzaSyB4OcXSEzn7nWLIKGHoossv2g0kiRkohBY"


def locate2():
    """locate"""
    gmaps = googlemaps.Client(key=API_KEY)
    locations = gmaps.geolocate()
    latitude = locations['location']['lat']
    longitude = locations['location']['lng']

    return latitude, longitude
