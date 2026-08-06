
#! Write a program to write a word in reverse

s = input("Enter your word: ")

for i in range(len(s)-1,-1,-1):
    print(s[i], end="")


