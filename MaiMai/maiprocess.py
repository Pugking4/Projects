import string
scores = {}
count = 0
average = float()

with open('playerdata.txt','r',encoding="utf8") as fr:
    for lines in fr:
        #print(lines)
        lines = lines.strip().split("\t")
        if len(lines) == 6:
            #print(lines)
            song, genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
        else:
            song = "NoName"
            genre, difficulty, level, type, score = lines
            scores[song, difficulty, type] = score, level, genre
#print(scores)

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