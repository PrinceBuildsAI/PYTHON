
#! Polymorphism- When a single function, method, or object behave in different way depending on what calls it.
#! define a method fuel_type in both Car and ElectricCar classes, but different behaviours.


class Car:
    total_car = 0 #care collector
    def __init__(self, brand, model): #__init__ method
        self.model = model
        self.__brand = brand  # __(two underscore make is private and inaccessible)
        Car.total_car += 1
    def get_brand(self): #method
        return self.__brand + "!"

    def full_name(self): #method
        return f"{self.brand} {self.model} {self.battery_size}"

    def fuel_type(self): #method
        return "Petrol or CNG" # return value bahar deta h


class ElectricCar(Car): # sub class 
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self): #method
        return "Electric charge"


tesla = ElectricCar("Tesla", "Model S", "85KWh") #object
tata = Car("Tigor", "XZ") #object
audi = Car("Audi", "R8") #object

print(tata.fuel_type())
print(tesla.fuel_type())
print(Car.total_car)
