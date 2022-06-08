x = '''Inteface ethernet0 is up
Inteface ethernet1 is down
Inteface serial0 is down
Inteface serial1 is up '''

# a
lst = x.split("\n")
for i in range(len(lst)):
    lst[i] = lst[i].replace('Inteface', 'Interface')
print(lst)

# b
count_up = 0
inter_up = []
for i in range(len(lst)):
    char_lst = lst[i].split()
    for j in range(len(char_lst)):
        if char_lst[j] == 'up':
            count_up += 1
            inter_up.append(char_lst[1])
print("Count Up:",count_up)

# c
print("Interface Up:", inter_up)