# a strange point: you can change a variable to function
def my_func(number):
    return number + 10


my_variable = my_func  # new point: variable = function(without ())

print(my_variable(10))  # new point: use variable with ()


# lambda: one line function without name
# lambda syntax: lambda arguments: expression

lambda a: a + 10  # return = a + 10

x = lambda a: a + 10
print(x)
print(x(3))


y = lambda a, b: a + b
print(y)
print(y(21, 12))

# point: we can have nested functions
# point: we can return another function in our function


def my_func(a):
    def new(n):  # nested function
        return a * n
    return new  # return a function


my_doubler = my_func(2)  # create a function with another function by special argument(s)
my_tripler = my_func(3)

print(my_doubler(8))
print(my_tripler(8))

# in last example we should use lambda instead new


def my_func2(a):
    return lambda n: n * a


my_doubler2 = my_func2(2)
my_tripler2 = my_func2(3)

print(my_doubler2(8))
print(my_tripler2(8))
