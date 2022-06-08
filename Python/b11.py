input = input("Enter your string:")

dict = {'upper case':0, 'lower case':0, 'digit':0, 'special char':0}

for i in input:
    if i.isupper():
        dict['upper case'] += 1
    elif i.islower():
        dict['lower case'] += 1
    elif i.isdigit():
        dict['digit'] += 1
    else:
        dict['special char'] += 1

for i in dict:
    print(f"{i}: {dict[i]}")