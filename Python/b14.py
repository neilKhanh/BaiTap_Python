conso = 'ueoai'
x = input("Enter a verb:")

if x[-2] + x[-1] == 'ie':
    x = x[0:-2] + 'ying'
elif x[-1] == 'e':
    x = x[0:-1] + 'ing'
elif x[-1] in conso:
    x = x + x[-1] + 'ing'
else:
    x = x + 'ing'

print(x)