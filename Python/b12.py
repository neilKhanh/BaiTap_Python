input = input("Enter your string:")
dict = {}

for i in input:
    if i not in dict.keys():
        dict[i] = 0
        for j in input:
            if j == i:
                dict[i] += 1
print(dict)