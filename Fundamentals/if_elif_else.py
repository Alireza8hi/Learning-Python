a = 5
b = 10


if a == b:
    print("hii")


if a == b:
    print("hi")
else:
    print("by")


if a == b:
    print("hey you")
elif a > b:
    print("hello")
else:
    print("haha")


if a < b:
    print("ok1")
elif a == b:
    print("ok2")
elif a == b + 7:
    print("ok3")
else:
    print("ok4")


if a >= b: print("ok5")  # shorted if


print("ok6") if a != b else print("ok7")  # shorted if else


if True:
    print("ok8")
else:
    print("ok8.5")


if 0:
    print("ok9")

if 5:
    print("ok10")


if "Ali":
    print("ok11")

if "":
    print("ok12")


print("ok12") if a > b else print("ok13") if a == b else print("ok14")  # shorted nested if else


if a:  # nested if elif else
    if a > b:
        if a >= b + 10:
            print("ok15")
        elif a == b + 11:
            print("ok16")
        else:
            print("ok17")
    elif a == b:
        print("ok18")
    else:
        if a < b - 10:
            priny("ok19")
        elif a > b - 10:
            print("ok20")
        else:
            print("ok21")
else:
    print("ok22")


if 10 > 11 or 5 == 11 - 6:  # or in condition
    print("ok23")


if 10 > 9 and 5 >= 6:  # and in condition
    print("ok24")


if not 3 == 4:  # not in condition
    print("ok25")
