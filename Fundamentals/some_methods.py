a = 1234
b = "afds"
c = "234"
d = "adfsdf2"
e = "213423f"

# print(a.isnumeric()) error: numeric object don't have this method
# print(a.isalpha()) error: numeric object don't have this method
print(b.isnumeric())  # new point
print(b.isalpha())  # new point
print(c.isnumeric())
print(c.isalpha())
print(d.isnumeric())
print(d.isalpha())
print(e.isnumeric())
print(e.isalpha())

a = ["3", "4", "ali"]

b = "".join(a)  # new point
print(b)
b = ""
b = b.join(a)  # new point
print(b)
