def convert_data(year, month, day):
    if month == 10:
        if day <= 10:
            return year + 621
        else:
            return year + 622
    elif month < 10:
        return year + 621
    else:
        return year + 622


def convert_data2(year, month, day):
    if month > 10 or month == 10 and day > 10:
        return year + 622
    else:
        return year + 621


my_day = input("enter day: ")
my_month = input("enter month: ")
my_year = input("enter year: ")
print(convert_data2(int(my_year), int(my_month), int(my_day)))
