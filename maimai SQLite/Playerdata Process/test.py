import csv
with open('Projects\\maimai SQLite\\Playerdata Process\\example.csv', newline='') as f:
  for line in csv.DictReader(f):
    print(line)
    #print(line['name'], 'is', line['age'], 'and lives in', line['city'])