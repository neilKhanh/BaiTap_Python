input = input()

input = input[0] + input[1:].lower().replace(input[0].lower(), '$')

print(input)