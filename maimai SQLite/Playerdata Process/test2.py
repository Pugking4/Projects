list_a = [['apple', 2], ['banana', 3], ['orange', 4]]
list_b = [['apple', 'red'], ['banana', 'yellow'], ['kiwi', 'brown']]

dict_a = {item[0]: item for item in list_a}
dict_b = {item[0]: item for item in list_b}

for key in dict_a.keys() & dict_b.keys():
    dict_a[key].append(dict_b[key][1])

list_a = list(dict_a.values())

print(list_a)
