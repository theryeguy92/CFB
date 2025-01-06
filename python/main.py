from api_request import make_request
from process_data import filter_game_data

def main():
    """Fetch and display CFB data."""
    try:
        # Fetch Data
        games = make_request("/games", {"year": 2022, "seasonType": "regular"})
        filtered_games = filter_game_data(games)  # Corrected variable name

        # Results
        for game in filtered_games:  # Consistent variable name
            print(f"{game['home_team']} vs {game['away_team']}: {game['home_points']}-{game['away_points']} on {game['date']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
