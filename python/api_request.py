import requests
from auth import get_api_key

BASE_URL = "https://api.collegefootballdata.com"

def make_request(endpoint, params=None):
    """Auth GET request via CFBD API."""
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }

    # Use the correct module name `requests`
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")