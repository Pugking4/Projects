import sqlite3
import csv

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute("SELECT score FROM playerscores WHERE level = '14+';")
scores = cur.fetchall()

conn.close()
print(scores)