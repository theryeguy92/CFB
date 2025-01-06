def filter_game_data(games):
    """Filter & format data for readability"""
    filtered_data = []
    for game in games:
        filtered_data.append({  # Corrected the typo here
            "home_team": game.get("home_team", "N/A"),
            "away_team": game.get("away_team", "N/A"),
            "home_points": game.get("home_points", 0),
            "away_points": game.get("away_points", 0),
            "date": game.get("start_date", "Unknown")
        })
    return filtered_data
