# An abstract class can be considered as a blueprint for other classes.

from abc import ABC, abstractmethod, abstractproperty  # we need them to make an abstract class


# abstract class: a class that contains abstract methods or abstract properties
class Animal(ABC):  # abstract class must inheritance ABC class

    @abstractmethod  # abstract method need abstractmethod decorator
    def move(self):  # abstract method
        pass  # we must don't implement for abstract methods in abstract class

    @abstractproperty  # abstract property need abstractproperty decorator
    def legs(self):  # abstract property
        pass  # we must don't implement for abstract properties in abstract class


class Lion(Animal):
    def move(self):  # we have to define and implement abstract methods from abstract parent class in child class
        print("lion is moving")

    @property  # if we want to say this function is a property, we add this line
    def legs(self):  # we have to define abstract properties from abstract parent class in child class
        return 4  # we have to return a value for abstract property from abstract parent class in child class


class Dog(Animal):
    def move(self):
        print("lion is moving")

    @property
    def legs(self):
        return 4


d1 = Dog()
d1.move()
print(d1.legs)
l1 = Lion()
l1.move()
print(l1.legs)
