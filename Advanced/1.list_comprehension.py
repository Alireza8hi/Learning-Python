my_list = ["amir", "mohammad", "hourieh", "ahmad", "hossein", "ali"]
print(my_list)

new_list = []
for item in my_list:
    if "a" in item:
        new_list.append(item)

print(new_list)

# new list by list comprehension
new_list2 = [item for item in my_list if "a" in item]
print(new_list2)

# new list by list comprehension without if
new_list3 = [item for item in my_list]
print(new_list3)

# new point
new_list4 = [item.upper() for item in my_list if "a" in item]
print(new_list4)

# if and else in list comprehension
new_list8 = [x.upper() if "a" in x else "hahaha" for x in my_list]
print(new_list8)

# list comprehension for range and number
new_list5 = [x for x in range(10)]
print(new_list5)

# add if in last example
new_list6 = [x for x in range(10) if x % 2 == 1]
print(new_list6)

# add new point in last example
new_list7 = [x**2 for x in range(10) if x % 2 == 1]
print(new_list7)
