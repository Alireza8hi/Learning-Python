me = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

# access to a value by its key (two ways)

x = me["name"]
print(x)

y = me.get("name")
print(y)

# access to keys or values

z = me.keys()
print(z)

w = me.values()
print(w)

# method item in dict

x = me.items()
print(x)


x = "name" in me  # new point
print(x)

if "family_name" in me:  # new point
    print(True)

