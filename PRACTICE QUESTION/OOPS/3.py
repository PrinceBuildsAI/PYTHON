
#! create an electric car that inherits from the car class and has an additional attribute battery_size
#! Inheritance - just like property is given from one generation to another

class Car:
    def __init__(self, brand, model):
        self.model = model
        self.brand = brand

    def full_name(self):
        return f"{self.brand} {self.model} {self.battery_size}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


tesla = ElectricCar("Tesla", "Model S", "85KWh")
print(tesla.model)
print(tesla.full_name())
