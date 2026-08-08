
# username = "Prince"


# def func():
#     username = "Alice"
#     print(username)


# print(username)
# func()

#! Another approach
# x = 3

# def func2(y):
#     z = x + y   # here x is global
#     return z
# print(func2(3))

#! another

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()


# def PrinceCoder(num):
#     def actual(x):
#         return x**num

#     return actual


# f = PrinceCoder(2)
# g = PrinceCoder(3)

# print(f(2))
# print(g(3))

# Closure = Function + Us function ko future me chahiye hone wale outer variables ka saved snapshot.


def PrinceCoder(num):

    def actual(x):
        return x ** num

    return actual
    # return function ka result wapas (return) karta hai aur function ko wahi par khatam kar deta hai.
    '''return do kaam karta hai:
    1. Value/function ko caller ke paas wapas bhejta hai.
    2. Function ko turant stop kar deta hai.'''
f = PrinceCoder(5)

print(f(2))


def PrinceCoder(num):
    def actual(x):
        return x**num

    return actual


f = PrinceCoder(2)
g = PrinceCoder(3)

print(f(2))
print(g(3))

