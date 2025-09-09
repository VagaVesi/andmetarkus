# Elektrihind rest teenusest

import requests
import json

# elering_url = "https://dashboard.elering.ee/api/nps/price?start=2025-01-01T00%3A00%3A01.999Z&end=2025-06-30T23%3A59%3A59.999Z"

# url ilma parameetriteta
elering_url = "https://dashboard.elering.ee/api/nps/price"

path = "day-3/elektrihind/"

# Elektrihind rest teenusest


def get_price(start: str, end: str) -> dict:
    """Hangi elektrihind antud ajavahemikus. Tagasta JSON andmed."""
    url = f"https://dashboard.elering.ee/api/nps/price?start={start}&end={end}"
    response = requests.get(url)
    return response.json()


def save_json(data: dict, filename: str):
    """Salvesta andmed faili JSON formaadis."""
    with open(path + filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Kontrollime kas fail olemas, siis lae failist, muuljuhul tee päring ja salvesta faili


def load_or_fetch_data(start: str, end: str, filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        data = get_price(start, end)
        save_json(data, filename)
        return data


# Näide kasutusest:
# data = get_price("2025-01-01T00:00:01.999Z", "2025-06-30T23:59:59.999Z")
# save_json(data, "elering_price.json")


""" start = "2025-02-01T00:00:01.999Z"
end = "2025-02-28T23:59:59.999Z"

data = get_price(start, end)
save_json(data, "elering_price_february_2025.json")
 """
