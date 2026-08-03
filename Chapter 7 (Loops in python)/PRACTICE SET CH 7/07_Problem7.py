#Q.7 Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter the number: "))

for i in  range(1, n+1):
    print(" "*(n-i), end="")        # end="" gives a new line
    print("*"* (2*i-1), end="")     # 2*i-1 gives negative number
    print()

