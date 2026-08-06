
#! write a program to show the number of occurrence of a character in a string

a = input("Enter your string: ")
b = input("Enter your character: ")

count = 0
index = 0
while index < len(a):
    if a[index] == b:
        count += 1
    index += 1
print(f"{b} = {count}")
