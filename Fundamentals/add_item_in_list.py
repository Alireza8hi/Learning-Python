friends = ["ali", "reza", "sara"]
print(friends)
friends.append("narges")
print(friends)

friends.insert(0, "mohammad")
print(friends)

new_friends = ["akbar", "asghar"]
friends.extend(new_friends)  # new point
print(friends)

new_friends2 = ("laleh", "ladan")
friends.extend(new_friends2)  # new point: we can add tuple to list in extend method
# new_friends2.extend(new_friends) error : we can't add list to tuple and tuple don't have extend method
print(friends)
