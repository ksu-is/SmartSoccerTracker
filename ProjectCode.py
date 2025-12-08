
import requests
from b24 import BeautifulSoup

"X-RapidAPI-Key": "YOUR_API_KEY_HERE",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "User-Agent": "Mozilla/5.0"
}

TOP_LEAGUES = [
    "Premier League",
    "La Liga",
    "Serie A"
]

def search_player(player_name):
    url = f"https://api-football-v1.p.rapidapi.com/v3/players?search={player_name}"
    res = requests.get(url, headers=HEADERS)

    if res.status_code != 200:
        print("API Error:", res.status_code, res.text)
        return None

    data = res.json()
    players = data.get("response", [])
   
if not players:
        print("No player found.")
        return None

    for p in players:
        league = p.get("statistics", [{}])[0].get("league", {}).get("name", "")

        if league in TOP_LEAGUES:
            return {
                "id": p.get("player", {}).get("id"),
                "name": p.get("player", {}).get("name"),
                "team": p.get("statistics", [{}])[0].get("team", {}).get("name", ""),
                "league": league
            }

     print("Player found, but not in top leagues.")
    return None
if __name__ == "__main__":
    name = input("Enter a player name: ")
    result = search_player(name)

    if result:
        print("Player found in top league:")
        print(result)

        
