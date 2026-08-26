# tuple is faster than list
# we can't change add remove items in tuple
# items in tuple are sorted and have index
# rules in tuple's items are like list

# join tuples
tuple1 = (2, 5, 6)
tuple2 = ("ali", True)
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple methods
print(tuple1.count(2))
print(tuple2.index("ali"))

a = ("ali")  # it is a string
print(type(a))
b = ("ali",)  # it is a tuple
print(type(b))
