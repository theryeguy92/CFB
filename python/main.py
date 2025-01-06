import pandas as pd
from api_request import make_request_for_years
from process_data import filter_game_data

# Relevant conferences to focus on
RELEVANT_CONFERENCES = ["SEC", "BIG 10", "BIG 12", "Pac-12"]

def filter_relevant_conferences(games):
    """Filter games to include only relevant conferences."""
    filtered_games = []
    for game in games:
        if game.get("home_conference") in RELEVANT_CONFERENCES or game.get("away_conference") in RELEVANT_CONFERENCES:
            filtered_games.append({
                "Team": game["home_team"],
                "Conf": game["home_conference"],
                "Season": game["season"],
                "Game": f"{game['home_team']} vs {game['away_team']}",
                "Home": game["home_team"],
                "Away": game["away_team"],
                "Points": game["home_points"],
                "Points Against": game["away_points"],
                #"Overtime": game["overtime"],
                "Date": game["start_date"]
            })
    return filtered_games

def main():
    """Fetch and process CFB data."""
    try:
        # Fetch Data for all years since 2000
        games = make_request_for_years("/games", start_year=2000, params={"seasonType": "regular"})
        
        # Filter games for relevant conferences
        filtered_games = filter_relevant_conferences(games)
        
        # Create a DataFrame
        df = pd.DataFrame(filtered_games)
        
        # Save DataFrame to CSV for further analysis
        df.to_csv("college_football_games.csv", index=False)
        print("Data saved to 'college_football_games.csv'.")
        
        # Display the first few rows of the DataFrame
        print(df.head())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
