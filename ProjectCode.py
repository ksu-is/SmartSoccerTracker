
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
   for p in players:
        league = p.get("statistics", [{}])[0].get("league", {}).get("name", "")

        if league in TOP_LEAGUES:
            return {
                "id": p.get("player", {}).get("id"),
                "name": p.get("player", {}).get("name"),
                "team": p.get("statistics", [{}])[0].get("team", {}).get("name", ""),
                "league": league
            }
     

     print("Player Found, but not in Premier League, La Liga, or Serie A.")
       return None

    return {
      "games": stats.get("games",0),
      "minutes": stats.get("minutes",0),
      "goals": stats.get("goals",0)
      "assists": stats.get("assists",0)
      "rating": stats.get("averageRating", 0)
  }

def main():
    print("=== SmartSoccerTracker ===")
    player_name = input("Enter player name: ")

    info = search_player(player_name)
    if not info:
       return

  stats = get_stats(info["id"])
  if not stats:
       print("No stats found for this player.")
       return

  print("\n--- Player Info ---")
  print("Name:", info["name"])
  print("Team:", info["team"])
  print("League:", info["league"])

  print("\n--- Stats ---")
  print("Games:", stats["games"])
  print("Minutes:", stats["minutes"])
  print("Goals:", stats["goals"])
  print("Assists:," stats["assists"])
  print("Avg Rating:", stats["rating"])

  if __name__ == "__main__":
      main()
        
