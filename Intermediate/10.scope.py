# scope : A variable is only available from inside the region it is created
def myfunc():
    x = 10
    print(x)  # x is available

    def myfunc2():
        y = 20
        print(x)  # x is available
        print(y)  # y is available
#    print(y)  error: y is unavailable


myfunc()
# print(x)  error: x is unavailable
# print(y)  error: un is unavailable


# global scope: when variable created out of all scopes, it's in global scope and available always

a = 30  # this variable is in global scope

# a strange point:
v = 40
print(v)


def test():
    v = 70
    print(v)  # this v, is v in this scope(most inside scope), if we don't have it, this will be v in global scope


test()
print(v)


# if we create a variable in local scope(not global scope),but we want it be global variable:
def test2():
    global z  # The global keyword makes the variable global.
    z = 12


test2()
print(z)

# a good example
v = 11
w = 10


def test3():
     global w
     w = 20  # this is global
     v = 21  # this is local


test3()
print(w)
print(v)
