mylist = ["ali", "sadegh", "mohammad", "sara", "ahmad", "amir"]
print(mylist)
mylist[0:3] = ["alireza", "mohammad sadegh", "mohammad reza"]  # new point
print(mylist)


print(len(mylist))
mylist[0] = ["ali", "reza"]  # two new points: 1. we can replace str and list 2. we have nested list
print(mylist)
print(len(mylist))
mylist[0:1] = ["ali", "reza"]  # new point
print(mylist)
print(len(mylist))

print(mylist)
print(len(mylist))
mylist[0:2] = ["alireza"]  # new point
print(mylist)
print(len(mylist))

mylist = ["red", "blue", "orange", "black"]
print(mylist)
print(len(mylist))
mylist.insert(2, "pink")  # new point
print(mylist)
print(len(mylist))

mylist[0] = "yellow"
print(mylist)
