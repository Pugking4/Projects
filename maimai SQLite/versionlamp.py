import csv

levels = ['1', '2', '3', '4', '5', '6', '7', '7+', '8', '8+', '9', '9+', '10', '10+', '11', '11+', '12', '12+', '13', '13+', '14', '14+', '15']
versions = ['maimai', 'maimai PLUS', 'GreeN', 'GreeN PLUS', 'ORANGE', 'ORANGE PLUS', 'PiNK', 'PiNK PLUS', 'MiLK', 'MiLK PLUS', 'FiNALE']
difficulties = ['BASIC', 'ADVANCED', 'EXPERT', 'MASTER', 'RE:MASTER']
ranks = {'D':0,'C':49.9999,'B':59.9999,'BB':69.9999,'BBB':74.9999,'A':79.9999,'AA':89.9999,'AAA':93.9999,'S':96.9999, 'S+':97.9999,'SS':98.9999, 'SS+':99.4999,'SSS':99.9999,'SSS+':100.4999, 0:0}


version = input('Version? (std only) ')
difficulty = input('Difficulty? ')
level = input('Level? ')
rank = input('Rank? ')

temp_list = []
check_list = []
count = 0
#version = 'maimai'
#difficulty = 'MASTER'
#level = ''
#rank = 'S'

if rank == '':
    rank = 0

if version == '':
    version = None

if difficulty == '':
    difficulty = None

if level == '':
    level = levels

#if level not in levels and level != None:
#    print('Invalid level.')
#    exit()

if version not in versions and version != None:
    print('Invalid version.')
    exit()

if rank not in ranks and rank != 0:
    print('Invalid rank.')
    exit()

if difficulty == 'REMASTER':
    difficulty = 'RE:MASTER'

if difficulty not in difficulties and difficulty != None:
    print('Invalid difficulty.')
    exit()

with open(r'maimai SQLite\Playerdata Process\playerdata.csv', 'r', encoding="utf8") as f:
    for line in csv.DictReader(f, delimiter='|'):
        line['score'] = line['score'].rstrip('%')
        if line['version'] == version and line['difficulty'].upper() == difficulty and line['level'] in level and float(line['score']) > ranks[rank]:
                #print(f"{line['song']}, {line['difficulty']}, {line['level']}, {line['internal_level']}, {line['score']}, {line['version']}")
                temp_list = [line['song'], line['difficulty']]
                check_list.append(temp_list)
                count += 1
                temp_list = []

print(f"Total that match the criteria: {count}")
count = 0

with open(r'maimai SQLite\Playerdata Process\alldata.csv', 'r', encoding="utf8") as f:
    for line in csv.DictReader(f, delimiter='|'):
        if line['difficulty'].upper() == difficulty and line['song'] not in [item[0] for item in check_list] and line['version'] == version:
                print("Not in check_list:", line['song'], line['difficulty'], line['version'])
                count += 1
print(f"Total that dont match rank criteria: {count}")