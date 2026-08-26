users = {
    "Reza": "2343",
    "Ali": "2566",
    "Laleh": "8058"
}

entered_username = input("enter your username: ")
entered_password = input("enter your password: ")

while entered_username not in users or users[entered_username] != entered_password:
    print("im sorry, your password or username is wrong,please enter again.")
    entered_username = input("enter your username: ")
    entered_password = input("enter your password: ")
else:
    print("you log in successfully")
