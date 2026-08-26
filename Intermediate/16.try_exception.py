my_dict = {
    "name": "alireza"
}

try:
    print("1")
    print(x)  # when we arrive to error line, go to except
    print("2")
except:
    print("An exception occurred")


try:
    print(x)
except:
    print("we have error")
else:  # when we don't have error, is run
    print("first else is run")

try:
    x = 4
    print(x)
except:
    print("we have error")
else:
    print("second else is run")


try:
    print(my_dict["lastname"])
except:
    print("se have an error")
else:
    print("we don't have any errors")
finally:  # after try&except run,always run
    print("try except is finish")

try:
    print(my_dict["age"])
except NameError:  # special error
    print("we have name error")
except KeyError:
    print("we have key error")
except:  # when we have error, but not mentioned error, is run
    print("we have other error")
finally:
    print("try except is finish")

try:
    print(my_dict["age"])
except (NameError, KeyError):  # more than one type error in one except
    print("we have name error or key error")
except:  # when we have error, but not mentioned error, is run
    print("we have other error")
finally:
    print("try except is finish")

# we have nested try except
try:
    x = 2
    try:
        y = 3
        print(y)
    except:
        print("y is not defined")
    else:
        print("y is defined")
    finally:
        print("y try except is finish")
except:
    print("x in not defined")
else:
    print("x in defined")
finally:
    print("x try except is finish")

z = 4

if z < 5:
    raise Exception("you have an exception")  # To throw (or raise) an exception from yourself
if z < 5:
    raise ValueError("you have an exception")  # To throw (or raise) an exception from yourself with that's type
