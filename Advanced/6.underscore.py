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

# When we are in a class

# 4.protected, before that name add underscore(only this class and its children could have direct access to this)
_name = "Alireza"


# 5.private, before that name add dunder(double underscore)(only this class could have access to this, not even its children)
__name = "Alireza"

# protected and private in python are just a show and like asking to not access, but you can access to them.
