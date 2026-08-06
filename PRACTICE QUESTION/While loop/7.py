
#! print first X multiple a number

n = int(input("Enter your number: "))
x = int(input("Enter you desired multiples: "))

count = 1

while count <= x:
    print(count * n, end=", ")
    count += 1

