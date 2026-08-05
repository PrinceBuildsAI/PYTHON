# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side
    
# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
#     def perimeter(self):
#         pass
#     def area(self):
#         pass

# obj = Circle(7)

#! Dunder method

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f"Your sum of ages are {self.age + sum}"

obj = Animal("Lion",12)
obj2 = Animal("dolphin",14)
obj3 = Animal("tiger",34)
print(obj + (obj2,obj3))