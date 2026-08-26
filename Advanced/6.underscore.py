# underscore or underline or _

# 1.if we want to create an object that we need that for not special thing, named it _

list1 = ["ali", "reza", "hossein"]

for _ in list1:
    print(_)

_ = list1[0]
print(_)

# 2.if we want to use a name for object that this name was reserved, after that name add underscore

for_ = "alireza"


# 3.for dunder method or magic method, we add before and after that dunder(double underscore)
class Ali:

    def __init__(self):  # __init__ is dunder method or magic method
        pass


# 4.protected, before that name add underscore
_name = "Alireza"


# 5.private, before that name add dunder(double underscore)
__name = "Alireza"
