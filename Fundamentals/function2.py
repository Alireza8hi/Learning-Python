# *args
def my_print(*names):
    print(names)
    print(type(names))


my_print()
my_print("ali")
my_print("alireza", "mohammad")
my_print("reza", "sahel", "reza", "ahmad")


def hellow(*args):
    for name in args:
        print(f"hellow {name}")


hellow()
hellow("ali")
hellow("ali", "reza", "sara", "kambiz")


def print_names(fname, lname, *args):
    print(fname)
    print(lname)
    print(args)


# print_names() error: print_names() missing 2 required positional arguments: 'fname' and 'lname'
print_names("ali", "sadeghi")
print_names("ali", "sadeghi", "mohammas", "amin", "emad")

