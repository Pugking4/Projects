import sqlite3
import csv
import io

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = 'JACKY [Remix]' AND difficulty = 'master';")
internal_levels = cur.fetchall()
print(internal_levels)