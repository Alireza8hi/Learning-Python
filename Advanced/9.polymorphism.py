# polymorphism: functions with the same name ,but different argument(in types and numbers)


# polymorphism in inbuilt functions:
print(len("geeks"))
print(len([10, 20, 30]))


# polymorphism in user-built functions:
def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))


# polymorphism in class methods:
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()


# polymorphism in Inheritance:
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# polymorphism in  Function and objects:
def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)


# when use Polymorphism and why?
# polymorphism in Programming using inheritance and method overriding:
class Animal:
    def speak(self):  # a function that we have to implement in child classes with same name
        raise NotImplementedError("Subclass must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


d1 = Dog()
c1 = Cat()
a1 = Animal()  # in polymorphism,we shouldn't make object from parent class, because it's not implement in parent class

print(d1.speak())
print(c1.speak())
# print(a1.speak())  # error: NotImplementedError: Subclass must implement this method
