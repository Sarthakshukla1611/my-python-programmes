# Creating a dictionary of a person
person = {
    "name": "ANSHUL",
    "age": 21
}

print(person)

# Getting values
print(person["name"])
print(person["age"])


person["city"] = "dewas"
print(person)


person["age"] = 20
print(person)

del person["city"]
print(person)
