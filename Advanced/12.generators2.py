# a practical example for generator
def fib(limit):
    a, b = 1, 1  # new point
    while a < limit:
        yield a
        a, b = b, a + b


x = fib(100)
y = fib(100)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

for item in y:
    print(item)
