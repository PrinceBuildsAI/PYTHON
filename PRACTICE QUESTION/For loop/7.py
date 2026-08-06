
#! fibonacci series

# n = int(input("Enter the desired range for fibonacci sequence: "))
# a = 0
# b = 1
# print(a, b, end=" ")

# for _ n range(n-1):
#     next_term = a + b
#     print(next_term, end=" ")
#     a,b = b,next_term
    
#? Another approach 

n = int(input("Enter the desired range for fibonacci sequence: "))

a = 0
b = 1

for _  in range(n):
    print(a, end=" ")
    a, b = b, a + b
    # c = a + b
    # a = b
    # b = c
