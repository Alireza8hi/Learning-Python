# iterator: an object that contains a countable number of values that you can traverse through all the values.
# iterable: you can get an iterator from it, iterables are list, tuple, dict, set, string
names = ["ali", "mohammad", "sadegh", "ahmad", "nahid"]
my_iter = iter(names)  # make iterator from iterable

print(next(my_iter))  # traverse an iterator
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter)) error: stop iterations
