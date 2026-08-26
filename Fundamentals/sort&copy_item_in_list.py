mylist = ["soheil", "ali", "bahram", "mohammad"]
print(mylist)
mylist.sort()  # change mylist to sorted mylist
new_list = sorted(mylist)  # make new list and assign into sorted mylist
print(mylist)
print(new_list)

mylist.sort(reverse=True)  # new point
print(mylist)

# list is call by reference, so we need special ways to make a copy from list(two ways)
new_list = mylist.copy()
new_list = list(mylist)
new_list = mylist[:]

# ways to join lists(three ways)
list1 = ["ali", "reza"]
list2 = [3, 4, 5]

list3 = list1 + list2
print(list3)

print(list1)
for x in list2:
    list1.append(x)
print(list1)

list1 = ["ali", "reza"]
list2 = [3, 4, 5]
print(list1)
list1.extend(list2)
print(list1)
