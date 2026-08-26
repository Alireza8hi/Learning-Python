# str() is used for creating output for end user while repr() is mainly used for debugging and development.
# repr’s goal is to be unambiguous and str’s is to be readable

a = "hellow world"
b = 2.0 / 11.0

print(str(a))  # show string in a
print(repr(a))  # show string in a with ''

import datetime
today = datetime.datetime.now()

print(str(today))  # show time in today
print(repr(today))  # show more information about today

# ----------------------------------------------------------------------------------------------------------------------
print("------------------------------------------------------------------------------------------------")
# some points about __str__ and __repr__ dunder methods in class


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):  # new point
        return self.name

    def __repr__(self):  # new point
        return f"an object from Person class by name: {self.name}"


p1 = Person("alireza")
print(p1)  # if we have __str__ and __repr__, return __str__
print(str(p1))  # if we have __str__ and __repr__, return __str__
print(repr(p1))  # if we have __str__ and __repr__, return __repr__


print("------------------------------------------------------------------------------------------------")


class Person:
    def __init__(self, name):
        self.name = name

#    def __str__(self):
#       return self.name

    def __repr__(self):
        return f"an object from Person class by name: {self.name}"


p1 = Person("alireza")
print(p1)  # if we just have __repr__, return  __repr__
print(str(p1))  # if we just have __repr__, return  __repr__
print(repr(p1))  # if we just have __repr__, return  __repr__


print("------------------------------------------------------------------------------------------------")


class Person:
    def __init__(self, name):
        self.name = name

#    def __str__(self):
#       return self.name

#   def __repr__(self):
#       return f"an object from Person class by name: {self.name}"


p1 = Person("alireza")
print(p1)  # if we haven't __str__ and __repr__, return default value
print(str(p1))  # if we haven't __str__ and __repr__, return default value
print(repr(p1))  # if we haven't __str__ and __repr__, return default value


print("------------------------------------------------------------------------------------------------")


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

#   def __repr__(self):
#       return f"an object from Person class by name: {self.name}"


p1 = Person("alireza")
print(p1)  # if we just have __str__, return __str__
print(str(p1))  # if we just have __str__, return __str__
print(repr(p1))  # if we just have __str__, return default value
