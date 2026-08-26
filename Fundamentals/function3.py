# **args
def my_print(fname, lname, *args, **args2):
    print(fname)
    print(lname)
    print(args)
    print(args2)
    print(type(args))
    print(type(args2))
    if "color" in args2:
        print(args2["color"])


my_print("ali", "hashemi")
my_print("hossein", "sohrabi", "nader", "naser", "yaser", "shayan", "amir")
my_print("ali", "alavi", "naser", "shantia", color="red")
my_print("ashkan", "hafezi", "hosseini", color="blue", age=29, city="tehran")
my_print("eshagh", "arash", age=39, color="black")