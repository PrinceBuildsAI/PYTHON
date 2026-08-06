
#! Calculate the number from a given range

n = int(input("Enter your range: "))
sum = 0

for i in range(n+1):
    sum = sum + i
print(f"Addition of range: {sum}")

#? other method
# n = int(input("Enter your range: "))
# print(sum(range(n + 1)))
