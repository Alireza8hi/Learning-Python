# generator is a function that has yields
# how work? everytime we call it,read between last yield until next yield and return next yield
# when use generator? if we want work with big data and traverse index without store it

def generator():
    yield 1
    print("ali")
    yield 2
    print("reza")
    yield 3
    yield 4
    yield 5


print(type(generator()))

for value in generator():  # you can traverse a generator function like range(n)
    i = 0
    print(f"{i}: {value}")


# Generator-Object : Generator functions return a generator object

# generator is iterable, and you can use it as iterator by assigning a variable ti it(two ways)

# first way
a = generator()

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


# second way
b = generator()

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
