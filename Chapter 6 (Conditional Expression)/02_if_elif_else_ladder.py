# Program for checking the Entered age given by the user is above 18 or nor
# if elif else ladder
a = int(input("Enter your age:"))

if (a>=18):         # if statement   # The empty space after print statement is known as "indent"
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):          # elif statement  # After accepting one statement all the other statement will be ignored
    print("You are entering a negative number which is not valid!")
    print("pleas again Enter your age")

elif(a==0):
    print("You have entered age zero which is not valid.")
    print("Pleas again enter your age")

else:               # else statement
    print("You are below the age of consent")
    print("Thank you")