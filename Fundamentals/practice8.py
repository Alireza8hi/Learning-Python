def check_pass(password):
    if len(password) < 8:
        print("your password must be at least 8 characters")
    elif password.isnumeric():
        print("your password must has at least 1 character")
    elif password.isalpha():
        print("your password must has at least 1 number")
    else:
        print("your password saves successfully")


while True:
    password2 = input("enter your password: ")
    check_pass(password2)
