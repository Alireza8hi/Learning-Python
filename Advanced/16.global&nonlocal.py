# we can't change global variable in local scope
"""
x = 13


def test():
    x += 3  error: UnboundLocalError: local variable 'x' referenced before assignment
    print(x)


test()
print(x)
"""

# solution:

x = 13


def test():
    global x  # now x in this scope is global
    x += 3
    print(x)


test()
print(x)

print("---------------------------------------------------------------------------------------------------------")

x = 18  # global x
print(x)  # ==> 18


def test():
    x = 9  # local x
    print(x)  # ==> 9

    def test2():
        global x
        x = 27  # global x(reason: last line)
        print(x)  # ==> 27

    test2()
    print(x)  # ==> 9  # local x(reason: look at scope)


test()
print(x)  # ==> 27  # global x

print("---------------------------------------------------------------------------------------------------------")

x = 18  # global x
print(x)  # ==> 18


def test():
    x = 9  # local x
    print(x)  # ==> 9

    def test2():
        nonlocal x  # new point
        x = 27  # local x(last scope, not for this scope)(reason: last line)
        print(x)  # ==> 27

    test2()
    print(x)  # ==> 27  # local x(reason: look at scope)


test()
print(x)  # ==> 18  # global x
