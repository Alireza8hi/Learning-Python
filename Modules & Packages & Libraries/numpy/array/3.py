import numpy as np

# array in numpy: ndarray
# ndarray: n-dimensional array that items are the same type(if not, change or error)

a0 = np.array(23)  # make 0-dimensional array with numpy
a = np.array([1, 2, 3])  # make 1-dimensional array with numpy

print(a)
print(type(a))


# how to get number of dimensional
b = a.ndim
b0 = a0.ndim

# how to get number of items
print(a.size)

print(b)
print(b0)

a2 = np.array([[7], [19], [5]])  # make 2-dimensional array with numpy
a22 = np.array([[7, 2], [19, 3], [5, 12]])  # make 2-dimensional array with numpy

a3 = np.array([[[11], [9], [67]], [[4], [3], [0]], [[7], [25], [15]]])  # make 3-dimensional array with numpy

# how to get row and column of array
c22 = a22.shape
d22 = a22.shape[0]  # get special axis(row)
d222 = a22.shape[1]  # get special axis(column)

print(c22)
print(d22)

# change data to same data
aa = np.array([23, "alireza"])
aa2 = np.array([23, 24.5])
aa3 = np.array([23, True])
aa4 = np.array([False, "alireza"])
aa5 = np.array([23.5, True])

print(aa)
print(aa2)
print(aa3)
print(aa4)
print(aa5)

# see type of array with dtype
my_type = aa2.dtype
print(my_type)

# set type for array(two ways)
aaa = np.array([2, 3, 7], dtype=np.uint8)
aaa2 = np.array([4, 65, 34], np.int32)
print(aaa.dtype)
print(aaa2.dtype)

# make zero array
# 1
a = np.zeros(4)
print(f"np.zeros(4) :   a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.zeros((1, 5))
print(f"a shape = {a.shape}, a = {a}")
a = np.zeros((2, 1))
print(f"a shape = {a.shape}, a = {a}")
# 2
a = np.zeros((4,))
print(f"np.zeros(4,) :  a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

# make random array
# 1
a = np.random.random_sample(4)
print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")
a = np.random.random_sample((1, 1))
print(f"a shape = {a.shape}, a = {a}")
# 2
a = np.random.rand(4)
print(f"np.random.rand(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")


# make array with count
print(np.arange(3))
print(np.arange(3.0))
print(np.arange(3, 9))
print(np.arange(3, 9, 2))


# reshape array in numpy
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(np.reshape(a, 6))
print(np.reshape(a, 6, order='F'))
print(np.reshape(a, (3, -1)))       # -1 means 6/3 or 2


# index in numpy array

# vector indexing operations on 1-D vectors
a = np.arange(10)
print(a)
# access an element
print(f"a[2].shape: {a[2].shape} a[2]  = {a[2]}, Accessing an element returns a scalar")
# access the last element, negative indexes count from the end
print(f"a[-1] = {a[-1]}")
# indexes must be within the range of the vector or they will produce and error
try:
    c = a[10]
except Exception as e:
    print("The error message you'll see is:")
    print(e)

# vector indexing operations on matrices
a = np.arange(6).reshape(-1, 2)   # reshape is a convenient way to create matrices
print(f"a.shape: {a.shape}, \na= {a}")

# access an element
print(f"\na[2,0].shape:   {a[2, 0].shape}, a[2,0] = {a[2, 0]},     type(a[2,0]) = {type(a[2, 0])} Accessing an element returns a scalar\n")

# access a row
print(f"a[2].shape:   {a[2].shape}, a[2]   = {a[2]}, type(a[2])   = {type(a[2])}")


# slicing in numpy array

# vector slicing operations
a = np.arange(10)
print(f"a         = {a}")
# access 5 consecutive elements (start:stop:step)
c = a[2:7:1]
print("a[2:7:1] = ", c)
# access 3 elements separated by two
c = a[2:7:2]
print("a[2:7:2] = ", c)
# access all elements index 3 and above
c = a[3:]
print("a[3:]    = ", c)
# access all elements below index 3
c = a[:3]
print("a[:3]    = ", c)
# access all elements
c = a[:]
print("a[:]     = ", c)

# vector 2-D slicing operations
a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

# access 5 consecutive elements (start:stop:step)
print("a[0, 2:7:1] = ", a[0, 2:7:1], ",  a[0, 2:7:1].shape =", a[0, 2:7:1].shape, "a 1-D array")

# access 5 consecutive elements (start:stop:step) in two rows
print("a[:, 2:7:1] = \n", a[:, 2:7:1], ",  a[:, 2:7:1].shape =", a[:, 2:7:1].shape, "a 2-D array")

# access all elements
print("a[:,:] = \n", a[:, :], ",  a[:,:].shape =", a[:, :].shape)

# access all elements in one row (very common usage)
print("a[1,:] = ", a[1, :], ",  a[1,:].shape =", a[1, :].shape, "a 1-D array")
# same as
print("a[1]   = ", a[1],   ",  a[1].shape   =", a[1].shape, "a 1-D array")


a = np.array([1, 2, 3, 4])
print(f"a             : {a}")
# negate elements of a
b = -a
print(f"b = -a        : {b}")

# sum all elements of a, returns a scalar
b = np.sum(a)
print(f"b = np.sum(a) : {b}")

# mean all elements of a
b = np.mean(a)
print(f"b = np.mean(a): {b}")

# all elements ot a change to a**2
b = a**2
print(f"b = a**2      : {b}")

#  all elements ot a change to 5*a
b = 5 * a
print(f"b = 5 * a : {b}")
