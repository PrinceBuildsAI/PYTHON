
#! calculate the product of number from a given range

a = int(input("Enter starting range: "))
b= int(input("Enter ending range: "))

product =1
while a <= b:
    product = product * a
    a += 1
print(f"Product of numbers is: {product}")