
#! check the given number is prime or not 

# n = int(input("Enter a number: "))

# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count += 1
# if count == 2:
#     print(f"{n} is a Prime Number")
# else:
#     print(f"{n} is not Prime Number")

#? Another approach

# num = int(input("Enter a number: "))

# is_prime = True

# for i in range(2, int(num ** 0.5)+1):
#     if num%i == 0:
#         is_prime = False
#         break

# if is_prime and num > 1:
#     print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

    

#! check the given number is prime or not in a given range

# n = int(input("Enter starting range: "))
# m = int(input("Enter ending range: "))


# for i in range(n,m+1):
#     count = 0
    
#     for j in range(1,i+1):
#         if i%j == 0:
#             count += 1

#     if count == 2:
#         print(i, end=", ")

#? Another approach

n = int(input("Enter starting range: "))
m = int(input("Enter ending range: "))


for i in range(n,m+1):
    is_Prime = True
    
    for j in range(2, int(i ** 0.5)+1):
        if i%j == 0:
            is_Prime = False
            break

    if is_Prime and i > 1:
        print(i, end=", ")        