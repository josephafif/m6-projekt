import json

SAVE_FILE = "savegame.json"


def save_game(money, shares, stock_price, current_day, total_days):
    """Sparar spelets variabler i en JSON fil"""
    game_data = {
        "money": money,
        "shares": shares,
        "stock_price": stock_price,
        "current_day": current_day,
        "total_days": total_days
    }

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

        money = int(game_data["money"])
        shares = int(game_data["shares"])
        stock_price = int(game_data["stock_price"])
        current_day = int(game_data["current_day"])
        total_days = int(game_data["total_days"])

        if money < 0 or shares < 0 or stock_price < 1:
            return None
        if current_day < 1 or total_days < 1 or current_day > total_days:
            return None

        return {
            "money": money,
            "shares": shares,
            "stock_price": stock_price,
            "current_day": current_day,
            "total_days": total_days
        }

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
        return None
