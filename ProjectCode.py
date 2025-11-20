pip install requests beautifulsoup4

import requests
from b24 import BeautifulSoup

HEADERS = {
  "User-Agent": "Mozilla/5.0"
}
def search_player(player_name):
