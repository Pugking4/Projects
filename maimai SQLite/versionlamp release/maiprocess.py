import sqlite3
import csv
import string

conn = sqlite3.connect(r'C:\Users\joshu\Documents\GitHub\Projects\maimai SQLite\db.sqlite3')
cur = conn.cursor()


#temp = ''
temp = []
main = []

with open(r'maimai SQLite\Playerdata Process\playerdata.txt','r',encoding="utf8") as fr:
    for lines in fr:
        lines = lines.replace('	','|')
        lines = lines.split('|')
        for word in lines:
            word = word.rstrip('\n')
            temp.append(word)
        main.append(temp)
        temp = []


#temp = temp.splitlines()
#print(main)

cur.execute(f"SELECT songId, version FROM Songs;")
version = cur.fetchall()
#print(player_version)

for score in main:
    #print(score[0])
    for song in version:
        if score[0] == song[0]:
            score.append(song[1])
#print(main)

cur.execute(f"SELECT songId, difficulty, internalLevel FROM SheetInternalLevels;")
float_level = cur.fetchall()
float_level = [list(item) for item in float_level]

#print(float_level[1])


for word in float_level:
    word[1] = word[1].upper()
    if word[1] == 'REMASTER':
        word[1] = 'RE:MASTER'

"""
dict_float = {item[0]: item for item in float_level}
dict_main = {item[0]: item for item in main}

for key in dict_main.keys() & dict_float.keys():
    #print(f"Comparing key {key}:")
    #print(f"  dict_main[{key}]: {dict_main[key]}")
    #print(f"  dict_float[{key}]: {dict_float[key]}")
    if dict_main[key][2] == dict_float[key][1]:
        print(dict_main[key][2], dict_float[key][1])
        dict_main[key].append(dict_float[key][2])
        #print(True)
    else:
        dict_main[key].append('N/A')

main = list(dict_main.values())"""

for chart in main:
    found = False
    for song in float_level:
        if chart[0] == song[0] and chart[2].upper() == song[1]:
            chart.append(song[2])
            found = True
            break
    if not found:
        chart.append('N/A')


#for i in main:
#    print(i)
#print(main)

#for chart in main:
#    if chart[2] != "BASIC" and chart[2] != "ADVANCED" and chart[3] == '14':
#        print(chart)


"""
for score in main:
    for song in float_level:
        print(score[0], song[0])
        if score[0] == song[0] and score[2].lower == song[1]:
            score.append(song[2])
            print(score)
"""
            
temp2 = ''

with open(r'maimai SQLite\Playerdata Process\playerdata.csv','w',encoding="utf8") as fw:
    fw.write('song|genre|difficulty|level|type|score|version|internal_level\n')
    for line in main:
        for word in line:
            temp2 += word+'|'
        temp2 = temp2.rstrip('|')
        fw.write(temp2 + '\n')
        temp2 = ''
#print(main)


cur.execute(f"SELECT songId, type, difficulty FROM IntlSheets;")
all = cur.fetchall()
all = [list(item) for item in all]

for i in all:
    if i[1] == 'std':
        i[1] = 'standard'

for score in all:
    #print(score[0])
    for song in version:
        if score[0] == song[0]:
            score.append(song[1])

with open(r'maimai SQLite\Playerdata Process\alldata.csv','w',encoding="utf8") as fw:
    fw.write('song|type|difficulty|version\n')
    for line in all:
        for word in line:
            temp2 += word+'|'
        temp2 = temp2.rstrip('|')
        fw.write(temp2 + '\n')
        temp2 = ''