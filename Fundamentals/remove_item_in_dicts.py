me = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

print(me)
name = me.pop("name")
print(me)
print(name)

# me.pop() error: pop expected at least 1 argument, got 0

age = me.popitem()  # remove last item in dict
print(me)
print(age)

del me["family_name"]
print(me)

del me
# print(me) error: name 'me' is not defined

me = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

print(me)
me.clear()
print(me)
