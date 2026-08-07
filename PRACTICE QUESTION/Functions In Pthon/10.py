#! create a recursive function to calculate the factorial of a number
# ? Recursion means when a function call itself repeatedly inside a function
"""Recursion me loop nahi hota, balki function khud ko baar-baar call karta hai.
Har call memory (call stack) me ek naya function banata hai aur har function ke paas
apna alag local variable hota hai."""

# def factorial (n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))


def hello(n):
    print("Start", n)

    if n == 0:
        return

    hello(n - 1)

    print("End", n)


hello(3)
