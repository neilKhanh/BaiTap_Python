set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# a
seta = set1.union(set2)
print(seta)

# b
setb = set1.intersection(set2)
print(setb)

# c
setc = {i for i in set1 if i not in set2}
print(setc)