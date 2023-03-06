# initialize an empty string variable called 'temp'
temp = ''

# open the file 'playerdata.txt' in read mode with UTF-8 encoding
with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.txt','r',encoding="utf8") as fr:
    # iterate over each line in the file
    for lines in fr:
        # replace all tab characters with vertical bar characters in the line
        lines = lines.replace('	','|')
        # concatenate the modified line to the 'temp' string variable
        temp += lines

# open the file 'playerdata.csv' in write mode with UTF-8 encoding
with open('Projects\\maimai SQLite\\Playerdata Process\\playerdata.csv','w',encoding="utf8") as fw:
    # write the column headers to the file
    fw.write('song|genre|difficulty|level|type|score\n')
    # write the contents of the 'temp' string variable to the file
    fw.write(temp)
