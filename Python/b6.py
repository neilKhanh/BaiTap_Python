information = {
"name": "Tuan",
"age":18,
"salary": 8000,
"city": "Ha Noi"
}

# a
information["job"] = "IT"
print(information)

# b
print(information["salary"])

# c
del information["age"]
print(information)

# d
information["salary"] = 10000
print(information)