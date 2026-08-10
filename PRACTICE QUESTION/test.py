# def demo():
#     return "hello"


# a = demo()
# print(a)

#! Another

def calculate(num1,num2):
    add = num1 + num2
    sub = num1-num2
    mul = num1*num2
    div = num1/num2
    
    # print(add, sub, mul, div) # output= 9 1 20 1.25
    return add,sub,mul,div

# print(calculate(5,4)) #works as (9, 1, 20, 1.25)
# calculate(5,4) #if print(add, sub, mul, div) output= 9 1 20 1.25

a,s,m,d = calculate(5,4)
print("Addition: ",a)
print("Subtraction: ",s)
print("Multiplication: ",m)
print("division: ",d)




