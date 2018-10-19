import pandas as pd
import requests
import json

game_pbp_2015 = {}

for game_id in range(413661, 416080):
    url = "https://statsapi.mlb.com/api/v1/game/" + str(game_id) + "/playByPlay?"
    r = requests.get(url)
    json_data = r.json()
    game_pbp_2015[game_id] = json_data['allPlays']

with open('game_pbp_2015.json', 'w') as outfile:
    json.dump(game_pbp_2015, outfile)


game_pbp_2016 = {}

for game_id in range(446873, 449298):
    url = "https://statsapi.mlb.com/api/v1/game/" + str(game_id) + "/playByPlay?"
    r = requests.get(url)
    json_data = r.json()
    game_pbp_2016[game_id] = json_data['allPlays']

with open('game_pbp_2016.json', 'w') as outfile:
    json.dump(game_pbp_2016, outfile)



game_pbp_2017 = {}

for game_id in range(490099, 492529):
    url = "https://statsapi.mlb.com/api/v1/game/" + str(game_id) + "/playByPlay?"
    r = requests.get(url)
    json_data = r.json()
    game_pbp_2017[game_id] = json_data['allPlays']
    
with open('game_pbp_2017.json', 'w') as outfile:
    json.dump(game_pbp_2017, outfile)
