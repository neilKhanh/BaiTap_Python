input = ["Mike", "", "","", "", "Emma", "", "Kelly", "", "", "Brad"]

# for
input_copy = input.copy()
for i in input:
    if i == "":
        input_copy.remove("")
print(input_copy)

# list comprehend
ans = [i for i in input if i != ""]
print(ans)