import pandas as pd
import json

def get_pitch_data(json_data, output_path):
    '''Function to sift trough MLB gameday json data. Extracts relevant
    columns and outputs a csv'''
    
    # Upload json data
    with open(json_data, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Initialize empty array to store data
    df_dict = []
    
    # For every game in season as json data
    for game_id in json_data:
        
        # For every at-bat in game
        for play_summary in game_summary:
            
            # Initialize count in at-bat
            count_balls = 0
            count_strikes = 0
            
            # For every pitch in at-bat
            for pitch in play_summary['playEvents']:
                
                # Extract pitches only. Don't want pickoff plays, etc
                if pitch['type'] == 'pitch':
                    
                    # extract inning information
                    try:
                        play_summary['about']['inning']
                    except KeyError:
                        inning_num = float('nan')
                    else:
                        inning_num = play_summary['about']['inning']
                    
                    inning_top_bot = play_summary['about']['halfInning']
                    
                    
                    # Matchup information
                    batSide_code = play_summary['matchup']['batSide']['code']
                    batSide_des = play_summary['matchup']['batSide']['description']
                    
                    batter = play_summary['matchup']['batter']['fullName']
                    batter_id = play_summary['matchup']['batter']['id']
                    
                    pitchHand_code = play_summary['matchup']['pitchHand']['code']
                    pitchHand_des = play_summary['matchup']['pitchHand']['description']
                    
                    pitcher = play_summary['matchup']['pitcher']['fullName']
                    pitcher_id = play_summary['matchup']['pitcher']['id']
                    
                    # Pitch details
                    try:
                        pitch['details']['code']
                    except KeyError:
                        call = float('nan')
                    else:
                        call = pitch['details']['code']
                        call_des = pitch['details']['description']
                    
                    try:
                        pitch['details']['type']['code']
                        pitch['details']['type']['description']
                    except KeyError:
                            pitch_type = float('nan')
                            pitch_type_des = float('nan')
                    else:
                        pitch_type = pitch['details']['type']['code']
                        pitch_type_des = pitch['details']['type']['description']
                    
                    try:
                        pitch['pitchData']['startSpeed']
                    except KeyError:
                        pitch_speed = float('nan')
                    else:
                        pitch_speed = pitch['pitchData']['startSpeed']
                    
                    try:
                        pitch['pitchData']['coordinates']['pX']
                        pitch['pitchData']['coordinates']['pZ']
                    except KeyError:
                        pitch_locx = pitch['pitchData']['coordinates']['x']
                        pitch_locy = pitch['pitchData']['coordinates']['y']
                    else:
                        pitch_locx = pitch['pitchData']['coordinates']['pX']
                        pitch_locy = pitch['pitchData']['coordinates']['pZ']
                    
                    # Append data to list
                    df_dict.append({'game_id':game_id,
                                   'inning_num':inning_num,
                                   'inning_top_bot':inning_top_bot,
                                   'batter':batter,
                                   'batter_id':batter_id,
                                   'batSide_code':batSide_code,
                                   'batSide_des':batSide_des,
                                   'pitcher':pitcher,
                                   'pitcher_id':pitcher_id,
                                   'pitchHand_code':pitchHand_code,
                                   'pitchHand_des':pitchHand_des,
                                   'count_balls':count_balls,
                                   'count_strikes':count_strikes,
                                   'pitch_type':pitch_type,
                                   'pitch_type_des':pitch_type_des,
                                   'pitch_speed':pitch_speed,
                                   'pitch_locx':pitch_locx,
                                   'pitch_locy':pitch_locy,
                                   'call':call,
                                   'call_des':call_des})
    
                    # Update the count                
                    count_balls = pitch['count']['balls']
                    count_strikes = pitch['count']['strikes']
    
    # Convert the list to a data frame and export
    df = pd.DataFrame.from_dict(df_dict)
    
    df.to_csv(output_path)
            
    
