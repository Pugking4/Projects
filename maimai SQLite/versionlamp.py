import sqlite3
import csv
import io

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

versions = ['maimai','maimai PLUS','GreeN','GreeN PLUS','ORANGE','ORANGE PLUS','PiNK','PiNK PLUS','MURASAKi','MURASAKi PLUS','MiLK','MiLK PLUS','FiNALE']

#dif = input("What difficulty? ")
dif = "master"
#ver = input("What version? ")
ver = "PiNK"

player_set = set()
ver_set = set()

cur.execute(f"SELECT song,difficulty,level,score FROM playerscores WHERE difficulty = \"{dif.upper()}\";")
player_scores = cur.fetchall()
#print(player_scores)

cur.execute(f"SELECT songId FROM Songs WHERE version = \"{ver}\";")
player_version = cur.fetchall()
#print(player_version)

cur.execute(f"SELECT songId FROM IntlSheets WHERE difficulty = \"{dif.lower()}\" AND type = 'std';")
int_sheets = cur.fetchall()
#print(int_sheets)


player_scores_new = []
for i in player_scores:
    song = i[0].replace("'", "''")
    #print(song, dif)
    cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = '{song}' AND difficulty = '{dif.lower()}' AND type = 'std';")
    internal_levels = cur.fetchall()
    #print(float(i[3].rstrip("%")))
    if song in [j[0] for j in player_version] and float(i[3].rstrip("%")) >= 97.0000:
        player_set.add(song)
        if len(internal_levels) > 0:
            player_scores_new.append((song, i[1], i[2], i[3], internal_levels[0][0]))
        else:
            player_scores_new.append((song, i[1], i[2], i[3], 'N/A'))
    elif song in [j[0] for j in player_version]:
        if len(internal_levels) > 0:
            player_scores_new.append((song, i[1], i[2], i[3], internal_levels[0][0]))
        else:
            player_scores_new.append((song, i[1], i[2], i[3], 'N/A'))

"""
for i in int_sheets:
    for x in player_scores:
        if i not in x:
            player_scores_new.append((i, i[1], i[2], i[3], 'N/A'))
"""
    
#print(player_scores_new[0][0])
#player_scores = player_scores_new

for i in player_version:
    if i in int_sheets:
        ver_set.add(i[0])

no_s = ver_set-player_set

for i in no_s:
    for x in player_scores_new:
        #print(i, 'compare', x[0])
        if i == x[0]:
            print(x[0], x[3])
        #else:
        #    print(x[0], '0.0000%')
#print(player_scores)


