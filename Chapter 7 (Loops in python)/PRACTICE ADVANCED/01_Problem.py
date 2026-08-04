"""Accept the integer and Print hello world n times"""

# num = int(input("Enter the number: "))

# for i in range (num):
#     print("Hello world")

"""Print natural number upto n"""
# num = int(input("Enter your number: "))

# for i in range(num+1):
#     print(i)

"""Reverse for loop"""
# num = int(input("Enter your number: "))

# for i in range (num,0,-1):
#     print(i)

"""Print table"""

# num = int(input("Enter your number: "))

# for i in range (1,11):
#     print(f"{num} * {i} = {num*i}")

"""sum upto n terms"""

# num = int(input("Enter a number: "))

# sum = 0

# for i in range (1, num + 1):
#     sum = sum + i # sum += i
# print(f"your sum is { sum}")

"""Factorial"""

# n = int(input("Enter your number: "))
# fact = 1

# for i in range(1,n+1):
#     fact = fact*i

# print(f"your factorial is {fact}")

"""Print the sum of all even and odd number in a range separately"""

# n = int(input("Enter your number: "))

# even = 0
# odd = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"Sum of odd is :{even} and sum of even is {odd}")

"""Factors"""

# n = int(input("Which number factors you want: "))

# for i in range(1, n+1):
#     if n%i == 0:
#         print(i)

"""perfect number"""
# while True:

#     n = int(input("check your number is perfect or not: "))

#     sum = 0

#     for i in range(1, n):
#         if n % i == 0:
#             sum = sum + i

#     if sum == n:
#         print(f"{n} is perfect")

#     else:
#         print(f"{n} is not perfect")
#         continue

"""Prime or not"""
# while True:

#     a = int(input("Enter a number prime or not : "))
#     count = 0
#     for i in range (1, a+1):
#         if a%i == 0:
#             count = count + 1

#     if count == 2:
#         print("Your number is prime")
#     else:
#         print("Not prime")
#     continue

"""Print prime number in a given range"""

# n = int(input("Enter a number: "))
# print("Prime numbers are:")

# for num in range(2, n+1):
#     count = 0 # Count will reset if it placed outside the loop

#     for i in range(1, num+1):
#         if num%i == 0:
#             count += 1

#     if count == 2:
#         print(num)

"""reverse a string"""

# "a = "Prince"
# b = ""

# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)"

"""Check palindrome or not"""
# while True:
#     a = input("Enter a string: ")
#     b = ""

#     for i in range(len(a)-1,-1,-1):
#         b = b + a[i]

#     if a == b:
#         print("palindrome")

#     else:
#         print("Not palindrome")
#     continue

"""count all letter, digit and special symbol in a string"""

# a = input("Enter your string: ")

# char = 0
# dig = 0
# symbol = 0

# for i in a:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         symbol += 1

# print(f"Digit: {dig}\nAlphabet: {char}\nSpecial characters: {symbol}")

'''Do while loop'''

# a = 1

# while a<=30:
#     print(a)
#     a = a +1

'''separate the number'''

# a = int(input("Enter a number: "))

# while a > 0:
#     print(a % 10)
#     a = a//10

# a = int(input("Enter a number: "))
# rev = 0

# while a > 0:
#     digit = a%10
#     rev = rev * 10 + digit
#     a = a//10

# while rev > 0:
#     print(rev %10)
#     rev = rev // 10

'''Palindrome using while'''

a = int(input("Enter a number: "))
copy = a
rev = 0

while a>0:
    rev = rev*10 + a % 10
    a = a//10
if copy == rev:
    print("palindrome")
else:
    print("Not palindrome")