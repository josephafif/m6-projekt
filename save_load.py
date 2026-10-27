import json

SAVE_FILE = "savegame.json"


def save_game(money, shares, current_day, total_days, stocks):
    """Sparar spelets variabler i en JSON fil"""
    game_data = {
        "money": money,
        "shares": shares,
        "current_day": current_day,
        "total_days": total_days
    }
    game_data["stocks"] = stocks

    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(game_data, file, indent=4)
        return True
    except OSError:
        return False

def load_game():
    """Laddar in en sparad JSON fil"""
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            game_data = json.load(file)
        money = float(game_data["money"])
        shares = dict(game_data["shares"])
        current_day = int(game_data["current_day"])
        total_days = int(game_data["total_days"])
        stocks = game_data["stocks"]

        if money < 0:
            return None
        if any(int(antal) < 0 for antal in shares.values()):
            return None
        if current_day < 1 or total_days < 1 or current_day > total_days:
            return None

        return {
            "money": money,
            "shares": shares,
            "current_day": current_day,
            "total_days": total_days,
            "stocks": stocks
        }

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None
