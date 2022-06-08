from operator import eq


def equal_check(tup):
    for i in tup:
        if i - tup[0] != 0:
            return False
    return True

tup1 = (10, 10, 10, 10)
print(equal_check(tup1))

tup2 = (10, 10, 2)
print(equal_check(tup2))
