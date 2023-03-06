temp = ''
with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.txt','r',encoding="utf8") as fr:
    for lines in fr:
        lines = lines.replace('	','|')
        temp += lines

with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','w',encoding="utf8") as fw:
    fw.write('song|genre|difficulty|level|type|score\n')
    fw.write(temp)