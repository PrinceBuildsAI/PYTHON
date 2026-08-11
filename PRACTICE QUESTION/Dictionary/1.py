#! Dictonary

# square = {i: i * i for i in range(1, 6)}

# for a, b in square.items(): #? we can say a,b or key, values
#     print(a, ":", b)

#! creating dictonary to list

# key = ["name", "age", "city"]
# values = ["Alice", 25, "New York"]
# result = dict(zip(key, values))

# for key,values in result.items():
#     print(key,":",values)

#! calcualet the frequency of charchter in string

# str = "mississippi"

# dict = {}
# for i in str:
#     dict[i] = dict.get(i, 0)+ 1

# print(dict)

#! invert a dictonary i.e key in place of value and value in place of key

# input_dict = {"a": 1, "b": 2, "c": 3}

# inverted = {v: k for k, v in input_dict.items()}
# print(inverted)

#! reversed the element of dictonary

# input_dict = {"a": 1, "b": 2, "c": 3}

# print(dict(reversed(input_dict.items())))

#! Remove empty value from dictonary

# input_dict = {'a': 1, 'b': '','c': 3, 'd': None}
# remove = {k:v for k , v in input_dict.items() if v}
# print(remove)

#! check if dictonary is a subset of another dictonary


def check(dict1, dict2):
    return all(i in dict2.items() for i in dict1.items())


dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

print(check(dict1, dict2))
