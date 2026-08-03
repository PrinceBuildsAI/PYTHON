friends = ["Apple", "Orange", 5, 345.06, False,"Akash", "Rohan"]
print(friends)

friends.append("Prince")  #c"append"is used to Adding data in existing list 
print(friends)

l1 = [1,8,7,2,21,15]

l1.sort()       # Remove last value from end-> [1,2,7,8,15,21] 

l1.reverse()    # Revesre the sequence of alphabets->  [15,21,2,7,8,1]

l1.append(8)    # Add 8 at the end of the list-> [1,2,7,8,15,8]

l1.insert(3,8)  # This will add 8 at 3 index-> [1, 8, 7, 8, 2, 21, 15]

l1.pop(2)       # Will delete element at index 2 and return its value.-> [1, 8, 2, 21, 15]

l1.remove(21)   # Will remove 21 from the list.->[1,8,7,2,15]


