# id: id function return address of our object in our computer's ram

2
a = 2
b = 2
c = 1 + 1

d = 4
4

"ali"
e = "ali"


def test():
    pass


f = test()
g = test


class Person:
    pass


p1 = Person()


# all tings that be or has same value have same address(id)

print("2: ", id(2))
print("a: ", id(a))
print("b: ", id(b))
print("c: ", id(c))

print("d: ", id(d))
print("4: ", id(4))

print("e: ", id(e))
print("ali: ", id("ali"))

print("test: ", id(test()))
print("f: ", id(f))
print("g: ", id(g))  # new point: has different id from f and test

print("Person: ", id(Person()))
print("p1: ", id(p1))  # new point: has different id from Person
