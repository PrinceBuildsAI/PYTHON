# 1. Creating a Dictionary

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

#2. Accessing Elements

print(my_dict['name'])  # Output: 'Alice'
print(my_dict.get('age'))  # Output: 25

#3. Adding or Modifying Elements

my_dict['age'] = 26  # Modifying existing key
my_dict['country'] = 'USA'  # Adding new key-value pair

#4. Removing Elements

del my_dict['city']  # Removing a specific key-value pair
my_dict.pop('age')  # Removing and returning a specific key-value pair
my_dict.clear()  # Clearing all key-value pairs

#5. Checking Membership

if 'name' in my_dict:
    print('Name is present in the dictionary')

#6. Iterating Over a Dictionary

for key in my_dict:
    print(key, my_dict[key])
    
# Using items() method
for key, value in my_dict.items():
    print(key, value)

#7. Dictonary Methods
# ->dict.keys(): Returns a view object that displays a list of all the keys.
# ->dict.values(): Returns a view object that displays a list of all the values.
# ->dict.items(): Returns a view object that displays a list of key-value tuple pairs.
# ->dict.copy(): Returns a shallow copy of the dictionary.
# ->dict.update(): Updates the dictionary with key-value pairs from another dictionary or iterable.

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)  # Output: dict_keys(['name', 'age', 'country'])
print(values)  # Output: dict_values(['Alice', 26, 'USA'])
print(items)  # Output: dict_items([('name', 'Alice'), ('age', 26), ('country', 'USA')])

new_dict = {'profession': 'Engineer'}
my_dict.update(new_dict)  # Adds key-value pair from new_dict to my_dict


