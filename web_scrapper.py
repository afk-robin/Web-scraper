import requests
from bs4 import BeautifulSoup
import pandas as pd

player_names = []
Team_names = []
Goals = []
assists = []
num_matches = []
shots = []

url = "https://www.bbc.com/sport/football/premier-league/top-scorers"
try:
    response = requests.get(url)
    response.raise_for_status()
except Exception as e:
    print(e)
else:
    soup = BeautifulSoup(response.content,"html.parser")
    print("successsful!")
    print(len(soup.find_all('tbody')))
    print(len(soup.find('tbody').find_all("tr" , class_ ="ssrcss-qqhdqi-TableRowBody e1icz100")))
    players = soup.find('tbody').find_all("tr" , class_ ="ssrcss-qqhdqi-TableRowBody e1icz100")
    for player in players:
        player_name = player.find("div",class_ = "ssrcss-m6ah29-PlayerName e1n8xy5b1").get_text(strip=True)
        player_names.append(player_name)
        team_name = player.find("div",class_ = "ssrcss-qvpga1-TeamsSummary e1n8xy5b0").get_text(strip=True)
        Team_names.append(team_name)
        goal_scored = player.find("div",class_ = "ssrcss-18ap757-CellWrapper ef9ipf0").get_text(strip=True)
        Goals.append(int(goal_scored))
        stats = player.find_all("div",class_= "ssrcss-1vo7v3r-CellWrapper ef9ipf0")
        assist_made = int(stats[0].get_text(strip=True))
        matches_played = int(stats[2].get_text(strip=True))
        shots_taken = int(stats[-3].get_text(strip=True))
        assists.append(assist_made)
        num_matches.append(matches_played)
        shots.append(shots_taken)
    data= {
        "player" : player_names,
        "Team"  : Team_names,
        "matches": num_matches,
        "Goals"  : Goals,
        "Assists" : assists,
        "Shots" : shots
    }

    df_players = pd.DataFrame(data)
n = int(input("Number of data :"))
print(df_players.head((n+1)))