from flask import Flask, render_template, request, redirect
import requests
import os
from dotenv import load_dotenv

load_dotenv()
STATS_KEY = os.getenv("STATS_KEY")
BASE_URL = "https://v3.football.api-sports.io"

HEADERS = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': STATS_KEY
}
player_name = "Lionel Messi"
league_id = 140
team_name = BASE_URL + f"/?search={player_name}"
url = BASE_URL + f"/players?search={player_name}&league={league_id}"
playerstats = requests.get(url, headers=HEADERS).json()
print(playerstats)