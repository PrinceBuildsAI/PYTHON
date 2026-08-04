# 1. Creating a Set

my_set = {1, 2, 3, 4, 5}

# 2. Adding and Removing Elements

my_set.add(6)  # Adds a single element to the set
my_set.update([7, 8, 9])  # Adds multiple elements to the set

my_set.remove(3)  # Removes the specified element from the set
my_set.discard(10)  # Removes the specified element if present, without raising an error
my_set.pop()  # Removes and returns an arbitrary element from the set

# 3. Checking Membership

if 4 in my_set:
    print('4 is present in the set')

# 4. Set Operations
# i: Union: Returns a new set containing all unique elements from both sets.
# ii: Intersection: Returns a new set containing common elements between two sets.
# iii: Difference: Returns a new set with elements present in the first set but not in the second.
# iv: Symmetric Difference: Returns a new set with elements in either of the sets but not in both.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1 | set2  # Union of set1 and set2
intersection_set = set1 & set2  # Intersection of set1 and set2
difference_set = set1 - set2  # Elements in set1 but not in set2
symmetric_difference_set = set1 ^ set2  # Elements in either set1 or set2 but not in both

print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(intersection_set)  # Output: {4, 5}
print(difference_set)  # Output: {1, 2, 3}
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

# 5. Other Useful Methods
# set.copy(): Returns a shallow copy of the set.
# set.clear(): Removes all elements from the set.
# Example Usage:

copy_set = my_set.copy()  # Shallow copy of my_set
print(copy_set)

my_set.clear()  # Clears all elements from my_set
print(my_set)  # Output: set()


