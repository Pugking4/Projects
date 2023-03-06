import sqlite3
import csv

master = []

with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','r',encoding="utf8",newline='') as fr:
    for lines in csv.DictReader(fr,delimiter='|'):
        #print(lines)
        #lines = lines.strip().split('   ')
        #print(lines['song'])
        if lines['song'] == ' ':
            lines['song'] = 'NoName'
        if lines['song'] == ' ' or lines['song'] == 'NoName':
            print(lines)
        master.append(lines)

#print(master)

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')

# Create a cursor object
cur = conn.cursor()


# Check if the table exists
cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='playerscores'")
result = cur.fetchone()

if result:
    print(f"The 'playerscores' table exists in the database")
    cur.execute("DELETE FROM playerscores")
else:
    print(f"The 'playerscores' table does not exist in the database")
    cur.execute('''CREATE TABLE playerscores (
                song TEXT,
                genre TEXT,
                difficulty TEXT,
                level TEXT,
                type TEXT,
                score TEXT
                )''')

    # Commit the changes
    conn.commit()


# Execute the SQL command to create the table


# Close the database connection


for chart in master:
    sql = "INSERT INTO playerscores (song, genre, difficulty, level, type, score) VALUES (?, ?, ?, ?, ?, ?)"
    conn.execute(sql, (chart['song'], chart['genre'], chart['difficulty'], chart['level'], chart['type'], chart['score']))
    conn.commit()
conn.close()

"""
# Connect to the database
conn = sqlite3.connect('db.sqlite3')

# Define the data as a Python dictionary

data = {'name': 'John Doe', 'age': 30, 'email': 'johndoe@example.com'}

# Define an SQL command to insert the data into the table
sql = "INSERT INTO table_name (name, age, email) VALUES (?, ?, ?)"

# Execute the SQL command with the data as a tuple
conn.execute(sql, (data['name'], data['age'], data['email']))

# Commit the changes
conn.commit()

# Close the database connection
conn.close()
"""