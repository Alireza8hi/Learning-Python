class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False

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


my_car = Car("benz", 160)
my_car.start()
my_car.start()
my_car.off()
my_car.off()
