
#! check if the number a perfect square or not

# n = int(input("Enter your number: "))

# root = n**0.5

# if root == int(root):
#     print("Perfect square")
# else:
#     print("Not a perfect square")

#! Using while loop

num = int(input("Enter your number: "))

count = 1

while count <= num:
    if count * count == num:
        print("Perfect square")
        break
    count += 1
else:
    print("Not a perfect square")

