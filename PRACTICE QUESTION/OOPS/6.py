
#! Add a static method to the Car class that returns a general description of car

class Car:
    total_car = 0
    def __init__(self, brand, model): #__init__ method
        self.__brand = brand  # __(two underscore make is private and inaccessible)
        self.model = model
        Car.total_car += 1
    def get_brand(self): #method
        return self.__brand + "!"

    def full_name(self): #method
        return f"{self.brand} {self.model} {self.battery_size}"

    def fuel_type(self): #method
        return "Petrol or CNG" # return value bahar deta h function ke

    @staticmethod
    def general_description():
        return "cars are means of transport"
    


class ElectricCar(Car): # sub class 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self): #method
        return "Electric charge"


tesla = ElectricCar("Tesla", "Model S", "85KWh") #object
tata = Car("Tigor", "XZ") #object
Car("Audi", "R8") #object

# print(tata.general_description())
print(Car.general_description())
