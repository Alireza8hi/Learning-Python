friends = ['mohammad', 'ali', 'reza', 'sara', 'narges', 'akbar', 'asghar', 'laleh', 'ladan']
print(friends)
friends.remove("ladan")
print(friends)

friends.pop()
print(friends)

friends.pop(1)
print(friends)

del friends[0]  # new point
print(friends)

del friends  # new point
# print(friends) error: name friends is not defined

friends = ["ali", "reza", "sara", "sadegh"]
friends.clear()  # new point
print(friends)
