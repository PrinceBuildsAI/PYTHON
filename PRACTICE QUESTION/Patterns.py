
#! Square pattern
# n = int(input("Enter a number: "))

# for i in range(n):
#     print("* " * n,)

#! Right triangle
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     print("*" * i)

#! Reversed right triangle
# n = int(input("Enter a number: "))

# for i in range(n, 0,-1):
#     print("*" * i)

#! Pyramid 
# n = int(input("Enter a number: "))

# for i in range(1,n+1):
#     print(" "*(n-i) + "* " * i)

#! Inverted pyramid

# n = int(input("Enter a number: "))

# for i in range(n, 0, -1):
#     print(" "*(n-i) + "* " *i)

#! Full pyramid
# n = int(input("Enter a number: "))

# for i in range(n):
#     print(" "*(n-i-1) + "*"*(2*i+1))

#! Diamond
# n = int(input("Enter a number: "))

# for i in range(n):
#     print(" "*(n-i-1) + "*"*(2*i + 1))
    
# for i in range(n-2,-1,-1):
#     print(" "*(n-i-1) + "*"*(2*i+1))
    
#! Hollow Square
# n = int(input("Enter a number: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#! Easy hollow square
# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or i == 5 or j == 1 or j == 5:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
