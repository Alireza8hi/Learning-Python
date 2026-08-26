# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def printname(self):
        print(self.name, self.lastname)


# how to create child class and use Inheritance
class Student(Person):  # class child(parent):
    pass
# now Person is parent class and Student is child class


p1 = Student("ali", "kamali")
print(p1.name)
p1.printname()


# Student is Person's child and is Owner's parent at the same time
class Owner(Student):
    pass

# when we don't write __init__ for child class, child class inherit __init__ from parent class, like last examples

# when we write __init__ for child class, child class doesn't inherit __init__ from parent class

# if we want to inherit __init__ from parent class and add more lines for __init__ in child class, so
# we called __init__ in parent class and add more lines


class Teacher(Person):

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age


class Admin(Person):
    def __init__(self, name, lastname, age):
        Person.__init__(self, name, lastname)
        self.age = age

# if you write a function with same name in function in parent class, child class doesn't inherit that from parent class


# super function: it comes stand for parent class in child class but need () and doesn't need self in argument

class Costumer(Person):
    def __init__(self, name, lastname, age):
        Person.__init__(self, name, lastname)
        super().__init__(name, lastname)  # it's same last line(super() stand for Person,we don't need self in argument)
        self.age = age


# we can add more properties and methods in child class that there ane not exit in parent class

class User(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)
        self.age = age

    def printage(self):
        print(self.age)


p2 = User("mohammad", "naderi", 23)
p2.printname()
p2.printage()
