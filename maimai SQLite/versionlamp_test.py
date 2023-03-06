import sqlite3
import io

conn = sqlite3.connect('C:\\Users\\joshu\\Documents\GitHub\\Projects\\maimai SQLite\\db.sqlite3')
cur = conn.cursor()

versions = ['maimai','maimai PLUS','GreeN','GreeN PLUS','ORANGE','ORANGE PLUS','PiNK','PiNK PLUS','MURASAKi','MURASAKi PLUS','MiLK','MiLK PLUS','FiNALE']

#dif = input("What difficulty? ")
dif = "master".upper()

with io.open('testver.txt','w',encoding='utf-8') as f:
    for version in versions:
        cur.execute(f"SELECT songId FROM Songs WHERE version = \"{version}\";")
        version_lamp = cur.fetchall()
        print(version + ":", end=" ")
        f.write(version + ": ")
        for song_id in version_lamp:
            print(''.join(song_id), end=" ")
            f.write(''.join(song_id)+', ')
        f.write('\n')




"""
for version in versions:
    #cur.execute("SELECT song,score FROM playerscores WHERE level = '14+' AND difficulty = 'MASTER';")
    #song = cur.fetchall()
    cur.execute(f"SELECT songId FROM Songs WHERE version = \"{version}\";")
    version_lamp = cur.fetchall()
    print(version+":",''.join(version_lamp))
"""