#(1) Creating Tuples: 
tuple1 = (1, 2, 3)          # Tuple with integer
tuple2 = ('a', 'b', 'c')    # Tuple with alphabets
empty_tuple = ()
single_element_tuple = (5,) # note the comma after the single element

#(2) Accessing Elements:
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0])   # Output: 1          ->It will gives the opsition index of value
print(tuple1[1:3]) # Output: (2, 3)

#(3) Concatenating Tuples:
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

#(4) Repeating Tuples:
tuple1 = ('a', 'b')
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: ('a', 'b', 'a', 'b', 'a', 'b')

#(5) Finding Length:
tuple1 = (1, 2, 3, 4, 5)
print(len(tuple1))  # Output: 5

#(6) Checking Membership:
tuple1 = (1, 2, 3)
print(2 in tuple1)  # Output: True
print(4 in tuple1)  # Output: False

#(7) Iterating Through a Tuple:
tuple1 = (1, 2, 3)
for item in tuple1:
    print(item)     # Items will arrange vertical manner

#(8) Tuple Unpacking: You can unpack a tuple into individual variables.
tuple1 = ('John', 'Doe', 30)
first_name, last_name, age = tuple1    #"tuple1" always written in last 
print(first_name)  # Output: John
print(last_name)   # Output: Doe
print(age)         # Output: 30

#(9) Counting Elements: You can count occurrences of a specific element in a tuple using .count() method.
tuple1 = (1, 2, 2, 3, 4, 2)
count_of_twos = tuple1.count(2)  #it will count the total number of "2" in tuple1
print(count_of_twos)  # Output: 3

#(10) Finding Index of an Element:You can find the index of the first occurrence of an element using .index() method.
tuple1 = (1, 2, 3, 2, 4, 2)
index_of_two = tuple1.index(3)
print(index_of_two)  # Output: 2

print("Hi-\b@", "python") #extra [ "\b" removes one character in backward direction and replace that with front character tahat is@ so "-" replaced with "@". ]