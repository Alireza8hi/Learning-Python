import numpy as np

# make array with numpy
# way 1
a1 = np.array([2, 3, 4])
print(a1)
# way 2
a2 = np.empty((3, 4))  # size of random array
print(a2)
a21 = np.empty((3, 4), dtype=np.int8)
print(a21)
# way 2-2
example = ([-3, -4, -65], [-3, -9, -45])
a22 = np.empty_like(example, shape=(2, 3))  # make sth like example
print(a22)
# way 3: make matrix that items in diameter are 1 and else are 0
a31 = np.eye(4)  # number of row and column
print(a31)
a32 = np.eye(4, 6)  # number of row and column
print(a32)
a33 = np.eye(4, 6, 1)  # diameter up 1 level
print(a33)
a34 = np.eye(4, 6, -1)  # diameter down 1 level
print(a34)
# way 4: like eye but row = column
a4 = np.identity(5)
print(a4)
# way 5:array that items are 1
a5 = np.ones((3, 4, 5))
print(a5)
# way 6:array that items are 0
a5 = np.zeros((3, 4, 5))
print(a5)
# way 7:array that items are n
a5 = np.full((3, 4, 5), 8)  # n is 8
print(a5)
# way 8:array taht count
a61 = np.arange(20)
print(a61)
a62 = np.arange(20)
a62 = a62.reshape(4, 5)
print(a62)
a63 = np.arange(10, 20)
print(a63)
a64 = np.arange(10, 20)
a64 = a64.reshape(2, 5)
print(a64)

a = np.array([1, 2, 3, 4])
b = np.array([-1, -2, 3, 4])
# compare two array
print(np.array_equal(a, a))
print(np.array_equal(a, b))

a = np.array([
    [3, 4, 5],
    [6, 7, 8]])
# sum all items in array
print(a.sum())
# sum all items in each column
print(a.sum(axis=0))
# sum all items in each row
print(a.sum(axis=1))

# get min item in array
print(a.min())

# get max item in array
print(a.max())

# sum some of nparray: sum element by element(element_wise)
a = np.array([1, 2, 3, 4])
b = np.array([-1, -2, 3, 4])
c = a + b
print(c)
c2 = a == b
print(c2)
c3 = a + 1
print(c3)

d = ([
    [3, 4, 5, 6],
    [5, 6, 7, 7],
    [10, 20, 30, 40]
])

c4 = a + d  # sum each item in a by all items in d with same column
print(c4)

f = np.array([1, 2, 3])
g = np.array([
    [4],
    [5],
    [6]
])
c5 = f + g  # add 4 and 5 and 6 to f and show in 3 rows
print(c5)
