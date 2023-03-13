import sqlite3
import csv
import string

conn = sqlite3.connect(r'C:\Users\joshu\Documents\GitHub\Projects\maimai SQLite\db.sqlite3')
cur = conn.cursor()

temp = []
main = []

with open(r'Projects\Discord-Bot\playerdata.txt','r',encoding="utf8") as fr:
    for lines in fr:
        lines = lines.replace('	','|')
        lines = lines.split('|')
        for word in lines:
            word = word.rstrip('\n')
            temp.append(word)
        main.append(temp)
        temp = []

cur.execute(f"SELECT songId, version FROM Songs;")
version = cur.fetchall()

for score in main:
    for song in version:
        if score[0] == song[0]:
            score.append(song[1])

cur.execute(f"SELECT songId, difficulty, internalLevel FROM SheetInternalLevels;")
float_level = cur.fetchall()
float_level = [list(item) for item in float_level]

for word in float_level:
    word[1] = word[1].upper()
    if word[1] == 'REMASTER':
        word[1] = 'RE:MASTER'

for chart in main:
    found = False
    for song in float_level:
        if chart[0] == song[0] and chart[2].upper() == song[1]:
            chart.append(song[2])
            found = True
            break
    if not found:
        chart.append('N/A')

temp2 = ''

with open(r'Projects\Discord-Bot\playerdata.csv','w',encoding="utf8") as fw:
    fw.write('song|genre|difficulty|level|type|score|version|internal_level\n')
    for line in main:
        for word in line:
            temp2 += word+'|'
        temp2 = temp2.rstrip('|')
        fw.write(temp2 + '\n')
        temp2 = ''

cur.execute(f"SELECT songId, type, difficulty FROM IntlSheets;")
all = cur.fetchall()
all = [list(item) for item in all]

for i in all:
    if i[1] == 'std':
        i[1] = 'standard'

for score in all:
    for song in version:
        if score[0] == song[0]:
            score.append(song[1])

with open(r'Projects\Discord-Bot\alldata.csv','w',encoding="utf8") as fw:
    fw.write('song|type|difficulty|version\n')
    for line in all:
        for word in line:
            temp2 += word+'|'
        temp2 = temp2.rstrip('|')
        fw.write(temp2 + '\n')
        temp2 = ''