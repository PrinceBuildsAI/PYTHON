
#! Print all even and odd number in a given range

#? Only even
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     if i%2 == 0:
#         print(i, end=", ")

#? Only odd
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     if i%2 != 0:
#         print(i,end=", ")

#? Odd and even 

# n = int(input("Enter a number: "))

# even = [ ]
# odd = [ ]

# for i in range(1,n+1):
#     if i%2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
    
# print(f"even number: {even}")
# print(f"odd number: {odd}")

#? Another method
# n = int(input("Enter a number: "))
# print(list(range(2, n + 1, )))
# print(list(range(1, n + 1, )))

# print()
# n = int(input("Number: "))
# print(*range(2, n+1, 2))
# print(*range(1,n+1,2))