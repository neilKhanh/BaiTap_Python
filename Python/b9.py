from re import A


scores = {'Hoang': 8, 'Giang beo': 7, 'Giang nghien': 9, 'meomeo': 10}

# a
name_input = input()
try:
    print(f"{name_input}: {scores[name_input]}")
except:
    print("Student is not available!")

# b
stu_name = input("Enter student's name:")
stu_score = int(input(f"Enter {stu_name}'s score:"))
scores[stu_name] = stu_score
print(scores)

# c
values = list(scores.values())
mx = []
mn = []
for i in scores:
    if scores[i] == min(values):
        mn.append(i)
    elif scores[i] == max(values):
        mx.append(i)

print("Highes score(s):", mx, max(values))
print("Lowest score(s):", mn, min(values))