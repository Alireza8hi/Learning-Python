# my class's name is like MyClass, not myClass, not my_class

class MyClass:  # class ClassName:
    x = 5  # properties
    y = "sara"  # properties


p1 = MyClass()  # make an object from a class
p2 = MyClass()

print(p1)
print(type(p2))
print(p1.x)  # object.property: access to properties in an object from a class
print(p2.y)
