
#! Demonstrate the use of instance() to check if my_tesla is an instance of car and Electric car
#! create two class battery and engine and let the car class inherit from both, demonstrating muitiple inheritance

class Car: #class
    total_car = 0

    def __init__(self, brand, model):  # __init__ method
        self.__brand = brand  # __(two underscore make is private and inaccessible)
        self.__model = model
        Car.total_car += 1

    def get_brand(self):  # method
        return self.__brand + "!"

    def full_name(self):  # method
        return f"{self.__brand} {self.__model} {self.battery_size}"

    def fuel_type(self):  # method
        return "Petrol or CNG"  # return value bahar deta h function ke

    @staticmethod #Decorator
    def general_description():
        return "cars are means of transport"
    
    @property #Decorator
    def model(self):
        return self.__model


class ElectricCar(Car):  # sub class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):  # method
        return "Electric charge"

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

new_tesla = ElectricCarTwo("Tesla", "Model S")
print(new_tesla.engine_info())
print(new_tesla.battery_info())

# tesla = ElectricCar("Tesla", "Model S", "85KWh")  # object

# print(isinstance(tesla, Car))
# print(isinstance(tesla, ElectricCar)) #? Inheritence

