# import necessary libraries
import sqlite3
import sys

# get user input for the desired difficulty and version
dif = sys.argv[1]
ver = sys.argv[2]

# connect to the SQLite database
conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

# create a list of valid game versions
versions = ['maimai','maimai PLUS','GreeN','GreeN PLUS','ORANGE','ORANGE PLUS','PiNK','PiNK PLUS','MURASAKi','MURASAKi PLUS','MiLK','MiLK PLUS','FiNALE']

# execute SQL queries to retrieve player scores and available songs for the specified version and difficulty
cur.execute(f"SELECT song,difficulty,level,score FROM playerscores WHERE difficulty = \"{dif.upper()}\";")
player_scores = cur.fetchall()
cur.execute(f"SELECT songId FROM Songs WHERE version = \"{ver}\";")
player_version = cur.fetchall()

# create a new list to store processed player scores
player_scores_new = []

# iterate over the player scores and retrieve the internal level for each song
for i in player_scores:
    # replace any apostrophes in the song name with double apostrophes to avoid SQL syntax errors
    song = i[0].replace("'", "''")
    cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = '{song}' AND difficulty = '{dif.lower()}' AND type = 'std';")
    internal_levels = cur.fetchall()
    # if the song is available in the specified version, print its information (including internal level if available)
    if song in [j[0] for j in player_version]:
        if len(internal_levels) > 0:
            print(song, '|', i[1], '|', i[3], '|', i[2], '|', internal_levels[0][0])
        else:
            print(song, '|', i[1], '|', i[3], '|', i[2], '|', 'N/A')
    # add the processed score information to the new list
    player_scores_new.append((song, i[1], i[2]))

# replace the original player score list with the processed one
player_scores = player_scores_new