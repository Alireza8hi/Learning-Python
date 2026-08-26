from mymodule import sms  # access to special thing from module

sms("2324")  # access to it, without use module name


from mymodule import hellow, num, User  # access to special things from module
hellow("ali")
print(num)
user1 = User()


from mymodule import *  # access to all things from module
print(myname)
print(my_dic["age"])
hellow("sara")
