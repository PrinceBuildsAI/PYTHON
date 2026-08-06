
#! Calculate the number of consonant in a word

word = input("Enter a word: ")

vowels = "aeiou"
count = 0
index = 0

while index  < len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count += 1
        print(f"consonant: {word[index]}",end=" ")
    index += 1
print()
print(f"Total Number of consonant are {count}")