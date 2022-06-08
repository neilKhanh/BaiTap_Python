x = "Nguyen ngOc HuY   hOANG"
lst = x.lower().split()
for i in range(len(lst)):
    lst[i] = lst[i].capitalize()
x = ' '.join(lst)
print(x)