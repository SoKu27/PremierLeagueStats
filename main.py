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

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("index.html")
 
 
@app.route('/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'GET':
        return redirect('/')
    

    team_name = request.form["teamname"]
    season = request.form["season"]
    url = BASE_URL + f"/teams?search={team_name}"

    
    teamstats = requests.get(url, headers=HEADERS).json()
    try:
        team_id = teamstats["response"][0]["team"]["id"]
    except (IndexError, KeyError):
        errormessage = "An error occured, please try again"
        return render_template("index.html", error=errormessage)
    url2 = BASE_URL + f"/leagues?team={team_id}"
    try:
        leaguestats = requests.get(url2, headers=HEADERS).json()
    except:
        errormessage = "An error occured, please try again"
        return render_template("index.html", error=errormessage)
    league_id = 39
    startyear = leaguestats["response"][0]["seasons"][1]["start"]
    print(league_id)
    print(season)
    print(startyear)


    
    try:
        finalstats = requests.get(BASE_URL + "/teams/statistics",headers=HEADERS, params = {
        "league" : league_id,
        "season" : season,
        "team" : team_id
    }).json() #without ".json()" this code isn't subscriptable which means that "finalstats" is just a response variable returned by the football api. With ".json" this variable gets converted to a python dictionary
        totalgamesplayed = finalstats["response"]["fixtures"]["played"]["total"]
    except (IndexError, KeyError):
        errormessage = "Please enter both a team and a year"
        return render_template("index.html", error=errormessage)
    goals = finalstats["response"]["goals"]["for"]["total"]["total"]
    logo = finalstats["response"]["team"]["logo"]
    return render_template("teams.html", team_name=team_name, season=season, stats = {
        "totalgamesplayed" : totalgamesplayed,
        "goals" : goals,
        "logo" : logo
    })

# @app.route('/players', methods=['GET', 'POST'])
# def players():
#     if request.method == 'GET':
#         return redirect('/')
    
#     form_data = request.form
    
#     player_name = form_data["playername"]
#     league_id = 140
#     team_name = BASE_URL + f"/?search={player_name}"
#     url = BASE_URL + f"/players?search={player_name}&league={league_id}"
#     playerstats = requests.get(url, headers=HEADERS).json()

#     player_id = [0]["player"]["id"]
#     print(playerstats)
#     player_id = playerstats[0]["player"]
#     print(player_id)


#     finalstats = requests.get(BASE_URL + "/players",headers=HEADERS, params = {
#         "league" : league_id,
#         "team" : player_id
#     }).json() 
   
#     return render_template("players.html")

if __name__ == '__main__':
    app.run(debug=True)