from get_pitches import get_pitch_data

# Pull data from MLB seasons 2015-2017
get_pitch_data('..\Data\game_pbp_2015.json', '..\Data\pitches_2015.csv')

get_pitch_data('..\Data\game_pbp_2016.json', '..\Data\pitches_2016.csv')

get_pitch_data('..\Data\game_pbp_2017.json', '..\Data\pitches_2017.csv')