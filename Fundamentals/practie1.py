age = input("How old are you?")  # new point

age2 = int(age)*2
age2 += 8
age2 += int(age)
age2 -= 2
age2 /= 3
age2 -= int(age)
age2 *= 4
age2 = int(age2)

# answer always is 8
print("your age is", age2)  # new point


# you can assign many variable with same value in one line
x = y = z = "Orange"  # new point

# you can assign many variable with different values in one line
x, y, z = 3, 12, 24  # new point


x = 10
y = 12
print(x is y)  # new point
print(x is not y)  # new point
