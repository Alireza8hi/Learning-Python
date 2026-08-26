# method in object: a function that belong to the object
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

# now we make an object method
    def hellow(self):  # an object method needs at least one argument(self)
        print(f"hellow {self.name} {self.lastname}")

    def hellow_many_times(self, number):
        for x in range(number):
            print(f"hellow {self.name} {self.lastname}")


p1 = Person("sara", "nazemi")
p1.hellow()
p1.hellow_many_times(3)  # now we called an object method


# Modify and delete object properties

p1.hellow()

p1.name = "narges"  # Modify object properties

p1.hellow()

del p1.lastname  # delete object properties

# p1.hellow() AttributeError: 'Person' object has no attribute 'lastname'

del p1  # delete object


# when we want to make an empty class, we use pass
class Empty:
    pass
