
#! Create a car class


class Car:
    def __init__(self, brand, model):  # brand and model are parameter given by user
        self.brand = brand  # self. means variable inside class
        self.model = model


my_car = Car("Audi", "R8")  # create an object with class
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Nexon")
print(my_new_car.brand)
print(my_new_car.model)
