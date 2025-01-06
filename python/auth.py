import os

def get_api_key(filepath="/home/ryan/college_football/keys/CFBD_API.txt"):
    """Reads the API key from a file."""
    with open(filepath, "r") as file:
        return file.read().strip()
