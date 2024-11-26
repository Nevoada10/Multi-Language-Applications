import requests

# Functions.py

def get_current_location():
    """
    Purpose: Fetches the current location using the ipinfo.io API.
    Arguments: None
    Returns: tuple: (latitude, longitude) if successful, or (None, None) if not.
    """

    try:
        response = requests.get('http://ipinfo.io/json')

        if response.status_code == 200:
            data = response.json()
            location = data['loc']
            latitude, longitude = map(float, location.split(','))
            return latitude, longitude
        else:
            print("Failed to fetch location data.")
            return None, None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None, None
    print(latitude,longitude)




get_current_location()