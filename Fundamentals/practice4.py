users = {
    "Reza": "2343",
    "Ali": "2566",
    "Laleh": "8058"
}

entered_username = input("enter your username: ")
entered_password = input("enter your password: ")

if entered_username in users:
    print("yes, you are our user")
else:
    print("oh no, you are not our user")
