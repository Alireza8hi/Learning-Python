num = 6
while num < 10:
    num += 1
    print(num)
"""
while num <= 10:
    print(num)   error: it's a loop for ever
"""
num2 = 4
while num2 < 10:
    num2 += 1
    print(num2)
else:  # when while is finished, else start
    print("while is finished")

while num <= 20:
    num += 1
    if num == 15:
        break  # while is finished here and else ignored
    print(num)
else:
    print("while is finished")


while num2 <= 20:
    num2 += 1
    if num2 == 15:
        continue  # go to line 25 and after while, else start
    print(num2)
else:
    print("while is finished")

