import sqlite3
import csv

conn = sqlite3.connect(r'C:\Users\joshu\Documents\GitHub\Projects\maimai SQLite\db.sqlite3')
cur = conn.cursor()


cur.execute("SELECT score FROM playerscores WHERE level = '14+';")
scores = cur.fetchall()

with open(r'maimai SQLite\Playerdata Process\playerdata.csv', 'r', encoding="utf8") as f:
    for line in csv.DictReader(f, delimiter='|'):
        print(line)

conn.close()
#print(scores)