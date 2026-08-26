mydict = {
    "name": "Alireza",  # key: value
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Ardalan"],
    "age": 19
}

# dict(like list) is call by reference, so we need special ways to make a copy from dict(two ways)
new_dict = mydict.copy()
new_dict = dict(mydict)
