import requests
import json


def get_current_lng_lat():
    """
    Get dict of current time and [lng, lat] of the ISS as a dict

    { unix_time_stamp : [lng ,lat] }

    """
    
    current_data = requests.get("http://api.open-notify.org/iss-now.json")

    current_data = current_data.json()

    timestamp = current_data['timestamp']

    latitude = current_data['iss_position']['latitude']

    longitude = current_data['iss_position']['latitude']

    return { timestamp : [ longitude, latitude ] }