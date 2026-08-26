# first class function : 1.functions are objects 2. Functions can be passed as arguments to other functions
# 3.Functions can return another function


# 1.functions are objects

def test1(number):
    print("functions in python are objects")
    return number


# first model
a = test1  # now is a function
a(5)

# second model
b = test1(5)

d = [test1, test1(3)]
print("list:", d, "first index:", d[0],"second index:",  d[1])  # strange point


# 2. Functions can be passed as arguments to other functions

def test3(number):
    return number


def test4(number):
    return number + 5


# first model
a = test3(test4)
c = a(12)
print(c)

# second model
a2 = test3(test4(10))
print(a2)


# 3.Functions can return another function


def test5(x):
    def test6(y):
        return x + y
    return test6


# nested arguments
# first model
e = test5(16)
print(e(3))

# second model
f = test5(4)(3)
print(f)
