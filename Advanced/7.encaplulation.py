class Person:
    def __init__(self):
        self.a = 10  # public: you can access and change this variable every place
        self._b = 12  # protected: you can access and change this variable just in this class and child classes
        self.__c = 15  # private: you can access and change this variable just in this class

    def test(self):  # we have to use and access and change protected and private properties in methods in class
        print(self._b)
        print(self.__c)


p1 = Person()
print(p1.a)
# print(p1._b)  error: you can't access protected properties out of class
# print(p1.__c)  error: you can't access private properties out of class
p1.test()  # instead you can access them by call methods in class


p1.__c = 20  # this variable isn't __c in class Person(that private variable), because we can't access that out of class
p1.test()


# but, how to change and access and delete protected and private properties out of class?
# with setter and getter and deleter methods in class and call them


# first model

class Person2:
    def __init__(self):
        self.name = "alireza"
        self._lastname = "hosseini"
        self.__age = 19

    def get_age(self):  # new point
        return self.__age

    def set_age(self, age):  # new point
        self.__age = age

    def del_age(self):  # new point
        del self.__age


p1 = Person2()
print(p1.get_age())  # new point
p1.set_age(23)  # new point
print(p1.get_age())
p1.del_age()  # new point
# print(p1.get_age())  error: AttributeError: 'Person2' object has no attribute '_Person2__age'  # new point


# second model

class Person3:
    def __init__(self):
        self.name = "alireza"
        self._lastname = "hosseini"
        self.__age = 19

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age)  # new point


p1 = Person3()

print(p1.age)  # new point
p1.age = 213  # new point
print(p1.age)
del p1.age  # new point


# third model

class Person4:
    def __init__(self):
        self.name = "alireza"
        self._lastname = "hosseini"
        self.__age = 19

    @property  # new point
    def age(self):  # new point
        return self.__age

    @age.setter  # new point
    def age(self, age):  # new point
        self.__age = age

    @age.deleter  # new point
    def age(self):  # new point
        del self.__age


p1 = Person4()
print(p1.age)  # new point
p1.age = 130  # new point
print(p1.age)
del p1.age  # new point


# why we define three methods for private and protected properties and can't change them like public properties?
# because we have to make limits for them in setter and getter and deleter methods

class Person5:
    def __init__(self):
        self.name = "alireza"
        self._lastname = "hosseini"
        self.__age = 19

    @property
    def age(self):
        if self.__age > 10:  # new point
            return self.__age
        else:  # new point
            raise Exception("you can't understand his name")  # new point

    @age.setter
    def age(self, age):
        if age < 50:  # new point
            self.__age = age
        else:  # new point
            raise ValueError("this age is too old")  # new point

    @age.deleter
    def age(self):
        if self.__age > 20:  # new point
            del self.__age
        else:  # new point
            raise Exception("you can't kill young persons")  # new point


p1 = Person5()
print(p1.age)
p1.age = 45
print(p1.age)
del p1.age
