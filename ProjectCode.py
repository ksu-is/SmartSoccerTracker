pip install requests beautifulsoup4

import requests
from b24 import BeautifulSoup

HEADERS = {
  "User-Agent": "Mozilla/5.0"
}

def search_player(player_name):
   url = "https://api-football-v1.p.rapidapi.com/v3/players"
   res =  requests.get(url, headers=HEADERS)
   data = res.json()

  players = data.get("players", [])
   if not players: 
     print("No player found.")
     return none

   for p in players:
     league = p.get("team", {}).get("tournament", {}).get("name", "")
     if league in TOP_LEAGUES:
       return {
          "id": p.get("name")
          "name": p.get("name")
          "team": p.get("team", {}.get("name"),
          "league": league              
