def find_all(x, sub):
    pos = []
    for h in range(len(x)):
        t = h + len(sub)
        if x[h: t] == sub:
            pos.append(h)
    return pos

x = input('Input:')
sub = input("You want to find:")
print(find_all(x, sub))



