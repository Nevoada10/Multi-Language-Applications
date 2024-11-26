import requests
from datetime import datetime as dt

# Functions.py

def get_current_location():
    """
    Purpose: Fetches the current location using the ipinfo.io API.
    Arguments: None
    Returns a tuple: (latitude, longitude) if successful, or (None, None) if not.
    """

    try:
        # Send a GET request to the ipinfo.io API to fetch location data
        response = requests.get('http://ipinfo.io/json')

        # Check if the response from the server is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response into a dictionary
            data = response.json()
            # Extract the 'loc' field from the data, which contains latitude and longitude as a string
            location = data['loc']
            # Split the 'loc' string into latitude and longitude, and convert them to float
            latitude, longitude = map(float, location.split(','))
            # Return the latitude and longitude as a tuple
            return latitude, longitude
        else:
            # Print an error message if the response was not successful
            print("Failed to fetch location data.")
            return None, None
    except Exception as e:
        # Handle exceptions that may occur during the request or data processing
        print(f"Error fetching location: {e}")
        return None, None
    
def get_current_time_iso8601():
    current_time = dt.now()
    return current_time.isoformat() + 'Z'

