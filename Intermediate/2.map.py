# map: give a function(without ()) and list, so try every index in list on function and save them in a map object

my_list = [3, 5, 11, 14]


def my_func(number):
    return number * 2


x = map(my_func, my_list)

print(x)
print(list(x))

# point: we should use lambda instead my_func

x = map(lambda a: a * 2, my_list)
print(x)
print(list(x))

my_list2 = [2, 5, 12, 13]

y = map(lambda a, b: a * b, my_list, my_list2)
print(y)
print(list(y))
print(list(y))  # it's empty list ,because we can't use list from map more than one time, solve:

y = list(map(lambda a, b: a * b, my_list, my_list2))  # solve
print(y)
print(y)  # solved
print(y[2])
