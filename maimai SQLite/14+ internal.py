import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

# List of game versions
versions = ['maimai', 'maimai PLUS', 'GreeN', 'GreeN PLUS', 'ORANGE', 'ORANGE PLUS', 'PiNK', 'PiNK PLUS', 'MURASAKi', 'MURISAKi PLUS', 'MiLK', 'MiLK PLUS', 'FiNALE']

# Select songs with a level of 14+ and difficulty of master from the playerscores table
cur.execute("SELECT song,score FROM playerscores WHERE level = '14+' AND difficulty = 'MASTER';")
player_maimai = cur.fetchall()

# Iterate through each song
for i in player_maimai:
    # Retrieve the internal level for the song from the SheetInternalLevels table
    cur.execute(f"SELECT internalLevel FROM SheetInternalLevels WHERE songId = \"{i[0].strip()}\" AND (difficulty = 'master' OR difficulty = 'remaster');")
    temp = cur.fetchall()
    # Print the song, internal level, and score
    if len(temp) > 0:
        print(f"{i[0]} | {temp[0][0]} | {i[1]}")
    else:
        print(f"{i[0]} | Internal level not available | {i[1]}")

# Close the connection to the database
conn.close()
