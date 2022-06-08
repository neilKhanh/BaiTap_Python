def replace_in_pos(x, sub, resub, pos):
    pos_sub = -1
    for h in range(len(x)):
        t = h + len(sub)
        if x[h: t] == sub:
            pos_sub += 1
            if pos_sub == pos:
                x = x[:h] + resub + x[t:]
                return x


x = "Khanh ucucuc Xuc"
sub = 'uc'
resub = 'ai'
pos = 1


print("After changing:", replace_in_pos(x, sub, resub, pos))