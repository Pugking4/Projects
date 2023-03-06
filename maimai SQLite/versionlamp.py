import sqlite3
import csv
import io
import sys

dif = sys.argv[1]
ver = sys.argv[2]


conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

versions = ['maimai','maimai PLUS','GreeN','GreeN PLUS','ORANGE','ORANGE PLUS','PiNK','PiNK PLUS','MURASAKi','MURASAKi PLUS','MiLK','MiLK PLUS','FiNALE']

#dif = input("What difficulty? ")
#dif = "master"
#ver = input("What version? ")
#ver = "maimai"


cur.execute(f"SELECT song,difficulty,level,score FROM playerscores WHERE difficulty = \"{dif.upper()}\";")
player_scores = cur.fetchall()
#print(player_scores)

cur.execute(f"SELECT songId FROM Songs WHERE version = \"{ver}\";")
player_version = cur.fetchall()
#print(player_version)

player_scores_new = []
for i in player_scores:
    song = i[0].replace("'", "''")
    #print(song, dif)
    cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = '{song}' AND difficulty = '{dif.lower()}' AND type = 'std';")
    internal_levels = cur.fetchall()
    if song in [j[0] for j in player_version]:
        if len(internal_levels) > 0:
            print(song, '|', i[1], '|', i[3], '|', i[2], '|', internal_levels[0][0])
        else:
            print(song, '|', i[1], '|', i[3], '|', i[2], '|', 'N/A')
    player_scores_new.append((song, i[1], i[2]))
player_scores = player_scores_new
