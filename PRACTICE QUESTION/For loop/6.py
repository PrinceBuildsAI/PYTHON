
#! count vowels in a string

# n = input("Enter string: ")
# print("Total vowels: ")

# count = 0
# for i in range(len(n)):
#     if n[i] in "aeiou":
#         count += 1
#         print(n[i], end=", ")
# print()
# print(f"Total vowel count: {count}")

# ? Other method
# n = input("Enter string: ")

# count = 0

# for i in range(len(n)):
#     if n[i] == "a" or n[i] == "e" or n[i] == "i" or n[i] == "o" or n[i] == "u":
#         count += 1
#         print(f"{n[i]}", end= ", ")
# print()
# print(count)

# ? other method

word = input("Enter your word: ")
vowels = "aeiou"

count = 0

for i in word:
    if i in vowels:
        count += 1
        print(i, end=", ")
print()
print(count)
