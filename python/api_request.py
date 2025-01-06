import requests
from auth import get_api_key
from datetime import datetime

BASE_URL = "https://api.collegefootballdata.com"

def make_request(endpoint, params=None):
    """Auth GET request via CFBD API."""
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "accept": "application/json"
    }

    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def make_request_for_years(endpoint, start_year=2000, params=None):
    """Fetch games for all years from start_year to the current year."""
    current_year = datetime.now().year
    all_games = []

    for year in range(start_year, current_year + 1):
        year_params = params.copy() if params else {}
        year_params["year"] = year
        print(f"Fetching games for {year}...")  # Debugging output

        # Fetch games for the specific year
        response = make_request(endpoint, year_params)
        all_games.extend(response)

    return all_games
