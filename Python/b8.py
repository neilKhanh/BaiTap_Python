from numpy import average


num = [int(i) for i in input().split(" ")]
dict = {}

# a
for i in num:
    if i not in dict.keys():
        dict[i] = 0
        for j in num:
            if j == i:
                dict[i] += 1
print(dict)

# b
values = list(dict.values())
mx = []
mn = []
for i in dict:
    if dict[i] == min(values):
        mn.append(i)
    elif dict[i] == max(values):
        mx.append(i)

print("Nhieu nhat:", mx)
print("It nhat:", mn)

# c
print(average(values))