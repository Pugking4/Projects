import string
key = 'mai'.upper()
plaintext = 'testcase'.upper()
encrypt = ''

def generate_vigenere_table():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    
    for i in range(26):
        row = list(alphabet[i:] + alphabet[:i])
        table.append(row)
    
    return table
count = 0
vigenere_table = generate_vigenere_table()
#print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, sep="  | ")
for rows in vigenere_table:
    count += 1
#    print(count, rows)

count = 0
for letter in plaintext.upper():
    if letter.isalpha():
        #print("Letter:", letter, "Key:", key[count])
        x = vigenere_table[0].index(key[count])
        y = vigenere_table[0].index(letter)
        #print("x:", x, "y:", y)
        #print(vigenere_table[y][x])
        encrypt += vigenere_table[x][y]
        count += 1
        if count > len(key) - 1:
            count = 0
    else:
        encrypt += letter

print(encrypt)