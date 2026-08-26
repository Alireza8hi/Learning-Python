def print_hellow():  # create a function
    print("Hellow")


print_hellow()  # call function
print_hellow()


# function with argument
def double_print(name):
    print(2 * name)


double_print("ali")
double_print("sara")


# function with return
def sum(number1, number2):
    return number1 + number2


a = sum(3, 5)
print(a)


def double_counter(number1, number2):
    number1 += 1
    number2 += 1
    return number1, number2


print(double_counter(3, 4))
print(type(double_counter(3, 4)))


# when function is empty and we want skip error
def empty():
    pass


print(empty())


# we can use list in argument
def my_function(this_list):
    for x in this_list:
        print(x)


my_list = ["ali", "reza", "sara"]
my_function(my_list)


# function with default argument
def print_your_city(city="Esfahan"):
    print("you are from ", city)


print_your_city("qom")
print_your_city("tehran")
print_your_city()
print_your_city("shiraz")


# keyword arguments
def print_children_name(child1, child2, child3):
    print(child1, child2, child3)


# when we use keyword arguments, we can change place in arguments
print_children_name(child1="alireza", child2="mohammad", child3="hossein")  # new point
print_children_name(child3="alireza", child2="mohammad", child1="hossein")  # new point, too
