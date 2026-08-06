
#! find cube of a given range 

a = int(input("Enter a starting range: "))
b= int(input("Enter ending range: "))

while a <= b:
    print(a ** 3 ,end=", ")
    a += 1
    