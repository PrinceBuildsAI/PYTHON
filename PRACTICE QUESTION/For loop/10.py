
#! count the occurrence of each alphabet in a string:

a = input("Enter your string: ")

count = { }

for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
for key, value in count.items():
    print(key, ":", value)