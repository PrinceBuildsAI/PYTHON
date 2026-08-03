'''gender'''
# a = input("Enter your gender: ")
# a = a.lower()

# if a == 'male' or a == 'm':
#     print("Hello sir")
# elif a == 'female' or a == 'f' :
#     print("Hello mam")
# elif a == 'trans' or a == "trans" or a == 't' :
#     print("Hello")
# else:
#     print("Invalid")
    

'''even odd'''

# a = int(input("Enter your number : "))

# if a%2 == 0:
#     print("Even")
# else:
#     print("odd")

'''loops-for loop'''
# import time

# start = time.perf_counter()

# for i in range(100000000):
#     pass

# end = time.perf_counter()

# print(f"Execute time:{end -start:.6f} seconds")

'''loops-for loop'''
# n = int(input("Enter your number : "))
# for i in range(n, (n*10)+1,n):
#     print(i)
'''loops - string'''

# a = "Prince"
# print(len(a))

# for i in range(6):
#     print(a[i])

# for char in a:
#     print(char)

'''Break/continue statement'''

for i in range(1,21):
    if i == 15:
        break #continue
    else:
        print(i)
    
