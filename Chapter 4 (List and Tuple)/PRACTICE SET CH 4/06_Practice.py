"""Print positive and negative elements of the list"""

# l = [12,-13,14,15,-1,34.5]

# print("Positive element are")
# for i in l:
#     if i >=0:
#         print(i)
# print("\n")
# print("Negative elements are")
# for i in l:
#     if i <= 0:
#         print(i)

'''Mean'''
# l = [12, 435, 67, 89, 23, 25, 69]

# sum = 0

# for i in l:
#     sum = sum + i
# print(sum/len(l))

'''Find the greatest'''
# l = [12, 35, 67, 89, 223, 25, 69]

# largest = l[0]
# index = 0

# for i in range (len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i
# print(f"Your largest number is {largest} at index {index}")

'''Find the second largest number'''

# l = [12, 35, 67, 223, 25, 69, 89]

# largest = l[0]
# second_largest = l[0]
# index1 = 0
# index2 = 0

# for i in range(1, len(l)):
#     if l[i] > largest:
#         second_largest = largest
#         index1 = index2

#         largest = l[i]
#         index2 = i

#     elif l[i] > second_largest:
#         second_largest = l[i]
#         index1 = i

# print(f"Second largest number is {second_largest} at index {index1}")
# print(f"Largest number is {largest} at index {index2}")

'''check if list is sorted or not'''

# l = [14,13,10,15,12]
# l = [10,11,12,13,14,15]

# for i in range(len(l)-1):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("Your list is sorted")

l = [14,13,10,15,12]

print(sorted(l))


