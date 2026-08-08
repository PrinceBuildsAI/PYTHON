
#! Encapsulation - Modify the car class to encapsulate the brand attribute, make it private and provide a getter method for it

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.__brand = brand # __(two underscore make is private and inaccessible)

    def get_brand(self):
        return self.__brand + "!" 

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


tesla = ElectricCar("Tesla", "Model S", "85KWh")

# print(tesla.brand)
print(tesla.get_brand())
