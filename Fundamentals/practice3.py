password = "1234"

entered_password = input("enter password: ")

while entered_password != password:
    entered_password = input("im sorry, your password isn't correct, please enter it again:")
else:
    print("you sign in successfully")
