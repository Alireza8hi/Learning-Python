def myfunc(name):
    upr = 0
    lwr = 0
    for x in name:
        if x.isupper():  # new point
            upr += 1
        elif x.islower():  # new point
            lwr += 1
        else:
            pass
    print(f"lower cases: {lwr}")
    print(f"upper cases: {upr}")


myfunc("alireza")
myfunc("Ali Kamali")
myfunc("ALI")

while True:
    name = input("enter your name: ")
    myfunc(name)
