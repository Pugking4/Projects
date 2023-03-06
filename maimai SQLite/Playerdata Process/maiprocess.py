import string
import csv

master = []
scores = {}
count = 0
average = float()

temp = ''

with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.txt','r',encoding="utf8") as fr:
    for lines in fr:
        #print(lines)
        #lines = lines.strip().split("\t")
        #print(lines)
        lines = lines.replace('	','|')
        temp += lines
        """
        if len(lines) == 6:
            #print(lines)
            song, genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
        else:
            song = "NoName"
            genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
        """
#print(scores)

#print(temp)

with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','w',encoding="utf8") as fw:
    fw.write('song|genre|difficulty|level|type|score\n')
    fw.write(temp)




with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','r',encoding="utf8",newline='') as fr:
    for lines in csv.DictReader(fr,delimiter='|'):
        #print(lines)
        #lines = lines.strip().split('   ')
        print(lines)
        """
        if len(lines) == 6:
            #print(lines)
            song, genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
        else:
            song = "NoName"
            genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
        """
#print(scores)




"""
with open('maiprocess_results.txt', 'w', encoding="utf8") as fw:
    for chart in scores:
        if "13+" in scores[chart]:
            count += 1
            fw.write(f"{chart} {scores[chart]}\n")
    fw.write(str(count))
#print(len(scores))

count = 0

for chart in scores:
    if '13+' in scores[chart]:
        temp = scores[chart][0].strip(string.punctuation)
        average += float(temp)
        count += 1
average = average / count
print(round(average, 4))
"""