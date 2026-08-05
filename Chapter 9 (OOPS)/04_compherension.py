
#! List comprehension ,  dictionary comprehension, set comprehension -  all operations are performed in one single line
# l = [i for i in range(1, 21) if i % 2 == 0]
# print(l)

# d = {i : i**2 for i in range(1,10)}
# print(d)

#! lambda

# addition = lambda a,b: a + b
# print(addition(12,13))

# addition = lambda a: "even"  if a%2 == 0 else "odd"
# print(addition(12))

#! Filter

a = [1,2,3,4,5,6,7,8,9]

result = filter(lambda x : True if x%2 == 0 else False, a)

print(list(result))