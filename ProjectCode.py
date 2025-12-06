
import requests
from b24 import BeautifulSoup

HEADERS = {
  "User-Agent": "Mozilla/5.0"
}
TOP_LEAGUES = ["Premier League", "LaLiga", "Serie A"]

def search_player(player_name):
   url = "https://api-football-v1.p.rapidapi.com/v3/players"
