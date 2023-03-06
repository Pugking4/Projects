import sqlite3
import csv

master = []

with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','r',encoding="utf8",newline='') as fr:
    for lines in csv.DictReader(fr,delimiter='|'):
        if lines['song'] == ' ':
            lines['song'] = 'NoName'
        master.append(lines)

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='playerscores'")
result = cur.fetchone()

if result:
    #print(f"The 'playerscores' table exists in the database")
    cur.execute("DELETE FROM playerscores")
else:
    #print(f"The 'playerscores' table does not exist in the database")
    cur.execute('''CREATE TABLE playerscores (
                song TEXT,
                genre TEXT,
                difficulty TEXT,
                level TEXT,
                type TEXT,
                score TEXT
                )''')
    conn.commit()

for chart in master:
    sql = "INSERT INTO playerscores (song, genre, difficulty, level, type, score) VALUES (?, ?, ?, ?, ?, ?)"
    conn.execute(sql, (chart['song'], chart['genre'], chart['difficulty'], chart['level'], chart['type'], chart['score']))
    conn.commit()
conn.close()