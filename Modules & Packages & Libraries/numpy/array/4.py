import numpy as np

a = np.array([
    [3, 6, 56],
    [12, 34, 4],
])

print(a)
print(a.shape)

a = a.reshape(3, 2)  # reshape array
print(a)
print(a.shape)

# access to item in array 2-D
print(a[0][1])  # bad way
print(a[0, 1])  # good way

print(a[0, 0:2])  # access to some items in a row

# --------------------------------------------------combine arrays
a = ([
    [3, 5, 9],
    [4, 6, 8]
])
b = ([
    [0, 0, 0],
    [1, 2, 3]
])

c = np.vstack((a, b))  # vertical
print(c)
d = np.hstack((a, b))  # horizontal
print(d)
e = np.concatenate((a, b), axis=0)  # vertical
print(e)
f = np.concatenate((a, b), axis=1)  # horizontal
print(f)
# --------------------------------------------------------split array
arr = np.arange(36.0).reshape(6, 6)

g = np.vsplit(arr, 3)
print(g)
h = np.hsplit(arr, 3)
print(h)

# ----------------------------------------------------------------
a = np.array([3, 4, 45, 9, 3])
a2 = a.sort()  # sort array
print(a)
# -----------------------------copy array
b = a.copy()  # call by value
c = a.view()  # call by reference

print(c)
print(b)

print(a.base)  # get base(it is view of ?)
print(b.base)
print(c.base)
