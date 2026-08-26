# decorator: decorators are used to modify the behaviour of function or class without change it.

def hellow_decorator(myfunc):  # give func in argument

    def inner():  # wrapper: inner func that replace to func
        print("change before call myfunc")
        myfunc()
        print("change after call myfunc")
    return inner


def myfunc():
    print("this is myfunc")


myfunc = hellow_decorator(myfunc)  # now, func = inner (func with changed) (hellow_decorator's return)

myfunc()


# we can type line 12 to 18 in short and standard form
@hellow_decorator
def myfunc():
    print("this is myfunc")


myfunc()


# -----------------------decorator for function with argument--------------------------------

# we have to add argument in myfunc and inner(three places)


def hellow_decorator(myfunc):

    def inner(name): # add argument here
        print("change before call myfunc")
        myfunc(name)  # add argument hire
        print("change after call myfunc")
    return inner


@hellow_decorator
def myfunc(name):  # add argument here
    print(f"this is myfunc hi {name}")


myfunc("Alireza")


# in standard form, we have to change arguments in inner and its myfunc this way

def hellow_decorator(myfunc):

    def inner(*args, **kwargs):  # change argument here
        print("change before call myfunc")
        myfunc(*args, **kwargs)  # change argument hire
        print("change after call myfunc")
    return inner


@hellow_decorator
def myfunc(name, lastname):
    print(f"this is myfunc hi {name} {lastname}")


myfunc("Alireza", "Hosseini")


# ---------------------------------if our func has return------------------------------------
def decorator(myfunc):

    def inner(*args, **kwargs):
        x = myfunc(*args, **kwargs)  # changed line
        return x  # changed line

    return inner


@decorator
def myfunc(name, lastname):
    return f"this is myfunc hi {name} {lastname}"


print(myfunc("Amir", "Asil"))


# ----------------------------we can have several decorators next to the each other------------------------

def dec1(myfunc):
    def inner():
        x = myfunc()
        return x * 3
    return inner


def dec2(myfunc):  # second decorator
    def inner():
        x = myfunc()
        return x* 10
    return inner


@dec2  # new point
@dec1  # new point
def myfunc():
    return 5


print(myfunc())


# another example 
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
