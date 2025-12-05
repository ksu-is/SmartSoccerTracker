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
