import sqlite3
import csv

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

versions = ['maimai','maimai PLUS','GreeN','GreeN PLUS','ORANGE','ORANGE PLUS','PiNK','PiNK PLUS','MURASAKi','MURISAKi PLUS','MiLK','MiLK PLUS','FiNALE']

cur.execute("SELECT song,score FROM playerscores WHERE level = '14+' AND difficulty = 'MASTER';")
player_maimai = cur.fetchall()

for i in player_maimai:
    #print(i[0])

    cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = \"{i[0].strip()}\" AND (difficulty = 'master' OR difficulty = 'remaster');")
    temp = cur.fetchall()
    if len(temp) > 0:
        print(f"{i[0]} | {temp[0][0]} | {i[1]}")
    else:
        print(f"{i[0]} | Internal level not avaliable | {i[1]}")
    #print(f"{''.join(i)} {''.join(temp)}")

conn.close()
#print(player_maimai)