# items are set is unchangeable ,but you can add and remove item
# items in set are unordered and don't have index and not duplicate
# set is مجموعه in mathematics

my_set = {"amir", "mahdi", "reza"}
print("amir" in my_set)  # new point
print("hadi" in my_set)

# add item in set
my_set.add("mohammad")

# add tuple or list or set in set with update method
my_tuple = (3, 4)
my_list = [True, False]
print(my_set)
my_set.update(my_list)  # new point
print(my_set)
my_set.update(my_tuple)
print(my_set)

set1 = {1, 2}
set2 = {"ali", "reza"}
set3 = set1.union(set2)  # new point : اجتماع گیری
print(set3)

set1 = {1, 2, "ali"}
set2 = {"ali", "reza"}
set3 = set1.intersection(set2)  # اشتراک گیری
print(set3)
print(set1)
set1.intersection_update(set2)  # اشتراک گیری
print(set1)

set1 = {1, 2, "ali"}
set2 = {"ali", "reza"}

set3 = set1.symmetric_difference(set2)  # متمم اشتراک گیری
print(set3)

print(set1)
set1.symmetric_difference_update(set2)  # متمم اشتراک گیری
print(set1)

set1 = {1, 2, "ali"}
set2 = {"ali", "reza"}
print(set1 | set2)  # اجتماع گیری
print(set1 & set2)  # اشتراک گیری
