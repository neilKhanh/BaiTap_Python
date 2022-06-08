list1 = [i for i in input().split(' ')]
list2 = [i for i in input().split(' ')]
ans = []

for i in range(len(list1)):
    ans.append(list1[i] + list2[i])

print(ans)