
#! Decorator

# def decorate(func):
#     def wrapper():
#         print("I will print my self before the function hello")
#         func()
#         print("I will print after the function")
#     return wrapper

# @decorate
# def hello():
#     print("Hello i am prince")

# hello()

# ? Second example

# def decorate(func):
#     def wrapper(a,b):
#         print("Addition to your number are")
#         func(a,b)
#         print("Thankyou I hope you like it")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"your total is {a+b}")

# addition(12,67)

#! Args and Kwargs

"""args"""

# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)


# addition(12, 12, 13)

"""kwargs"""

# def information(**kwargs):
#     print("Your information is\n\n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")


# information(name = "Prince", age = 22, designation = "AI/ML")

