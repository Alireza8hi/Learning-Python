# __init__: constructor for class, when we make an object from a class this function called and set default properties
# self in class: it means every object that you work on it,like 'this' in c++

class MyClass:

    def __init__(self):
        self.name = "ali"  # this way we use self(for access to abject properties or object methods)
        self.last_name = "hosseini"


p1 = MyClass()
print(p1.name)
print(p1.last_name)


class MyClass2:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


# p2 = MyClass2() error: we need two arguments

p3 = MyClass2("ali", "hosseini")
print(p3.name)
print(p3.last_name)


# we can do everything in __init__(),but in real life we just set default properties or necessary work after make object
class Print:
    def __init__(self):
        print("the __init__() function called when we make an object from this class")


p4 = Print()
