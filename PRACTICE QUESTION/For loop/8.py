
#! FActorial of a given number

n = int(input("Enter a number: "))

product = 1
for i in range(n,0,-1):
    product = product*i
    print(i, end=" X ")

print(f"= {product}")
    