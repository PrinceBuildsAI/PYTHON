'''Syntax'''

# class Factory:
#     a = 12 #attribute
    
#     def hello(self): #method
#         print("how are you")
    

# obj = Factory()

# print(obj.a)
# obj.hello()

'''constructor'''

# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"Your object details are {self.material}, {self.pockets}, {self.zips}")
        
# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)

# reebok.show()
# campus.show()

'''Attribute:- class attribute, instance(object) attribute'''

# class Animal:
#     name = "Lion"   #class attribute
    
#     def __init__(self,age):
#         self.age = age  #instance attribute
    
#     def show(self): #instance method
#         print(f"How are you your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("how are you brother")
        
#     @staticmethod
#     def static():
#         print("Hello world")
        
# obj = Animal(12)
# obj.hello()

'''inheritance'''

# class Factorymumbai:    #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("Hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class / subclass
#     pass    

# obj = Factorymumbai()

# ob2 = Factorypune()

# ob2.hello()

'''constructor'''

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#             print(f"hello your name is {self.name}, {self.age}")

# person1= Human("Prince",22)
# animal1= Animal("Lion")

# person1.show()
# animal1.show()

'''Multilevel inheritance'''

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips
        
# class BhopalFactory(Factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material, zips)
#         self.colour = color

# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pocket = pockets

# obj = PuneFactory("cotton",2,"blue",3)

'''Polymorphism'''

# class Animal:
#     def show2(self):
#         print("Hello i am prince")

# class Human(Animal):
#     def show(self):
#         print("how are you")
    
# obj = Human()
# obj2 = Animal()

# obj.show()

#! Duck Typing

# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("Hello I am also showing")
        
# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

# ! Encapsulation , Private class

# class Factory:
#     __a = "pune" #* __(double underscore) use to protect class in python
    
#     def __show(self):
#         print("hello i am a pune factory")

# class Bhopal(Factory):
#     def show2(self):
#         print(super().__a)
                
# obj = Bhopal()
# obj.show2()

