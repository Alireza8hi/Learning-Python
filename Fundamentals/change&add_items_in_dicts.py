me = {
    "name": "Alireza",
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

print(me)
me["name"] = "Ali"  # change item
print(me)
me["city"] = "Isfahan"  # add item
print(me)
me.update({"name": "Alireza"})  # change item
print(me)
me.update({"province": "Isfahan"})  # add item
print(me)
