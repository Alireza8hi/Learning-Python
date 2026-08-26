# dictionary or dict
me = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

me2 = {"name": "Alireza", "family_name": "Hosseini", "friends": ["Ali", "Mohammad", "Ardalan"], "age": 19}

# items aren't duplicated(keys) but are changeable and ordered, and we can add and remove

print(len(me))
print(me)
me = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19,  # now it's ignored
    "age": 20
}
print(len(me))  # don't increase by  two age
print(me)
