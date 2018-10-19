import pandas as pd
import numpy as np

## Upload data from csv's
#df_2015 = pd.read_csv('..\Data\pitches_2015.csv', index_col = 'game_id')
#df_2016 = pd.read_csv('..\Data\pitches_2016.csv', index_col = 'game_id')
#df_2017 = pd.read_csv('..\Data\pitches_2017.csv', index_col = 'game_id')
#
## Combine all seasonal dataframes into one
#df = pd.concat([df_2015, df_2016, df_2017])
#
## Drop 'Unnamed' column
#df.drop('Unnamed: 0', axis = 1, inplace = True)
#
## Remove All-Star game stats since it's a 'non-competitive' game between elite
## players. The corresponding game_id for the All-Star games are below. Then
## reset the index
#all_star_gameid = [414988, 448202, 491434]
#
#for i in all_star_gameid:
#    df.drop(i, inplace=True)
#df.reset_index(inplace=True)
## View head of df
## print(df.head())
#
## print(df.describe())
#
#
## Determine what the call codes mean by sorting by code and description
#call_codes = df.groupby('call')['call_des'].unique()
##print(call_codes)

# Codes could be simplified to mean the same things
# i.e. 'Ball in Dirt' & 'Intent Ball' is 'Ball'
#
# 'W' - 'Swinging Strike (Blocked)' needs to be investigated

# When a batter swings at a ball in the dirt and misses with 2 strikes, the
# batter as the option to run to first base. If he successfully makes it to
# first, he's considered safe. It counts as a a strikeout for the pitcher but
# not an official out during the game.

swinging_strike_blocked = df[(df['call'] == 'W') & (df['count_strikes'] == 2)]
#print(len(swinging_strike_blocked))

# Consider standardizing such cases to 'outs' if it'll have minimal effect
# on the outcome
percent_ssb = len(swinging_strike_blocked)/len(df_2015)
percent_ssb_outs = len(swinging_strike_blocked)/((2418+2424+2429)*27*2)

# Seeing as blocked swinging strikes accounts for 1.9% of pitches and ~3% of
# outs in those 3 seasons, I'll assume no errors occured on such plays and
# categorize the pitch as a swinging strike and if the batter had 2 strikes,
# they'd be 'out'

# Create a dictionary that will be used to update the 'call' codes
new_call_codes_dict = {'*B':'B',
                       'B':'B',
                       'C':'C',
                       'D':'H',
                       'E':'H',
                       'F':'F',
                       'I':'B',
                       'L':'S',
                       'M':'S',
                       'P':'B',
                       'Q':'S',
                       'R':'F',
                       'S':'S',
                       'T':'S',
                       'W':'S',
                       'X':'X'}

## Simplify the 'call' columns using the dictionary above
#df['call'] = [new_call_codes_dict[df.call[i]] for i in df.index]



##df_2015['is_out'] = [(df_2015.call[i] == 'X') for i in df_2015.index]