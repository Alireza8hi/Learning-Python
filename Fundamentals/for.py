my_list = ["ali", "reza", "sara", "amin"]
for x in my_list:
    print(x)

for item in my_list:
    print(item)

name = "alireza"
for y in name:
    print(y)
else:  # when while is finished, else start
    print("for is finished")

for x in my_list:
    if x == "sara":
        break  # while is finished here and else ignored
    print(x)
else:
    print("for is finished")

for x in my_list:
    if x == "sara":
        continue  # go to line 21 and after while, else start
    print(x)
else:
    print("for is finished")

for number in range(6):
    print(number)

for number in range(3, 6):
    print(number)

for x in range(2, 10, 2):
    print(x)

# nested for
colors = ["red", "blue", "orange", "white", "black"]
fruits = ["apple", "banana", "cherry"]

for color in colors:
    for fruit in fruits:
        print(f"{color}: {fruit}")

for color in colors:
    for fruit in fruits:
        print((color, fruit))


# when we need item and index of Sequence, we use two items in for and enumerate
for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)
