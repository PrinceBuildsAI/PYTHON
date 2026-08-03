a = int(input("Enter your age:"))


# if statement No.1      # if is independent but else is not independent
if(a%2==0):
    print("The given number is even")

else:
    print("Given number is odd")
#End of if statement No.1

# if statement No.2
if (a>=18):         # if statement   # The empty space after print statement is known as "indent"
    print("You are above the age of consent")
    print("Good for you")


elif(a<0):          # elif statement  # After accepting one statement all the other statement will be ignored
    print("You are entering a negative number which is not valid!")
    print("pleas again Enter your age")

else:               # else statement
    print("You are below the age of consent")
    print("Thank you")
# end of if statement No.2