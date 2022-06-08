def get_input(dict):
    while True:
        prod = input("Enter the name of product: ")
        if prod == 'end':
            break
        amount = int(input(f"Enter the amount of {prod}:"))
        if prod not in dict.keys():
            dict[prod] = amount
        elif prod in dict.keys():
            dict[prod] += amount

dict = {}
get_input(dict)

# a
prod = input("Enter the name of product:")
try:
    print(f"The amount of {prod} is {dict[prod]}")
except:
    print("This product is not availabe!")

# b
values = list(dict.values())
mx = []
for i in dict:
    if dict[i] == max(values):
        mx.append(i)
print(f"{mx} have/has the largest quantity: {max(values)}")


print(dict) 
