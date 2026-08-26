# more than one return

def validation(password):
    if len(password) < 8:
        return False  # if this line run, function will be finished
    else:
        return True


my_password = input("enter your password: ")

if validation(my_password):
    print("your password is ok!")
else:
    print("your password must be at least 8 character")
