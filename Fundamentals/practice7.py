# we want count every character in your fullname
name = input("enter your fullname: ")

for x in name:
    print(f"your name has {name.count(x)}: {x}")

print("---------------------------")
# fix a bug(delete duplicated character like a and a)

name2 = []

for x in name:
    if x not in name2:
        name2.append(x)
        print(f"your name has {name.count(x)}: {x}")


print("---------------------------")
# fix another bug(delete duplicated character like a and A)

name = name.lower()
name2 = []

for x in name:
    if x not in name2:
        name2.append(x)
        print(f"your name has {name.count(x)}: {x}")


print("---------------------------")
# fix another bug(delete spaces)

name2 = []
name = name.strip()
name = name.replace(" ", "")

for x in name:
    if x not in name2:
        name2.append(x)
        print(f"your name has {name.count(x)}: {x}")
