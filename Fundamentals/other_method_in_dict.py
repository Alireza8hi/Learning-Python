my_tuple = ("Ali", "Reza", "Amir")
my_list = [1, 2, 3]
my_list2 = 3
# make a dict with same values for each item in first argument
my_dict = dict.fromkeys(my_tuple, my_list)  # new point
my_dict2 = dict.fromkeys(my_tuple, my_list2)  # new point
my_dict3 = dict.fromkeys(my_tuple)  # new point
print(my_dict)
print(my_dict2)
print(my_dict3)


me = {
    "name": "Alireza",
    "family_name": "Hosseini",
    "friends": ["Ali", "Mohammad", "Amir Ali"],
    "age": 19
}

# if we don't have value return default value in second argument, but if we have value, argument ignored
print(me)
x = me.setdefault("age", 20)  # new point
me.setdefault("age", 20)  # new point
print(me)
print(x)

print(me)
y = me.setdefault("color", "red")  # new point
me.setdefault("color", "red")  # new point
print(me)
print(y)
