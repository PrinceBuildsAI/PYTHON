
#! Create a python function to calculate the circumference and area of circle
import math

def circle(r):
    radius = math.pi*2*r*r
    circumference = math.pi*2*r
    return radius, circumference

a , b = circle(4)
print(f"Area: {a:.2f}", f"Circumference: {b:.2f}")
    
#! calculate area of circle by Herons formula

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c = float(input("Enter side C: "))

# s = (a+b+c)/2

# area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
# print("Area = ", area)