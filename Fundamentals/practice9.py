def even_or_odd(number):
    number = int(number)
    if number % 2:
        print("odd")
    else:
        print("even")


while True:
    number = input("enter a number: ")
    even_or_odd(number)
