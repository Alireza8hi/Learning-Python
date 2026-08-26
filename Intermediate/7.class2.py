class Cars:
    cars_number = 0  # it's a class property(also object property)

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False
        Cars.cars_number += 1  # for change class property

    def start(self):
        if self.status:
            print(f"now {self.name} is on, please don't start")
        else:
            self.status = True
            print(f"{self.name} is start now")

    def off(self):
        if self.status:
            self.status = False
            print(f"{self.name} is off now")
        else:
            print(f"now {self.name} is off, please first start")


print(Cars.cars_number)
car1 = Cars("benz", 160)
car1.start()
car1.start()
car1.off()
car1.off()
car2 = Cars("pejo", 90)
print(Cars.cars_number)

print(Cars.cars_number)  # access to class property(and objects property except modified object property) by class
print(car1.cars_number)  # access to object property by object

car1.cars_number = 10  # modified this object property(not another objects or class property)
print(car1.cars_number)
print(car2.cars_number)
print(Cars.cars_number)

Cars.cars_number = 5  # modified class property and objects property(except modified object property)
print(Cars.cars_number)
print(car2.cars_number)
print(car1.cars_number)

# class property is references for objects property
