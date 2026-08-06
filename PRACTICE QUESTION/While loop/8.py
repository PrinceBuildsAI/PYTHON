
#! calculate the power of a number

a = int(input("Enter your number: "))
b = int(input("Enter the power: "))

count = 1
power = 1
while count <= b:
    power = power * a
    count +=1
print(f"Result: {power}")
