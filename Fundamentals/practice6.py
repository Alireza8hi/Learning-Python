names = ["ali", "reza", "alireza", "amir", "sara", "mohammad", "narges", "amin", "zahra", "mostafa"]
a_names = []

for name in names:
    if name[0] == "a":
        a_names.append(name)
print(a_names)


a = ["ali", "mahdi", "sara", "nastaran", "amir", "amin"]
b = ["mohammad", "ali", "narges", "amin", "nazanin"]
c = []

for x in a:
    for y in b:
        if x == y:
            c.append(x)
print(c)


d = []
for x in b:
    if x[-1] == "n":
        d.append(x)
print(d)
