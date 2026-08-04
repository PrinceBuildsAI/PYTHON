#try, except, else, finally, raise

# a = int(input("Enter your number: "))

# try:
#     print(10/a)

# # except ZeroDivisionError:
# except Exception as err:

#     print(f"sorry you cannot divide as {err}")
# else:
#     print("No exception")
# finally:
#     print("I will run no matter what")

# print("Division done")

'''raise'''

age = int(input("Tell your age: "))
try:

    if age < 10 or age >18:
        raise ValueError("Sorry your age must be 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"error occurred {err}")
    

print("The club will start soon")
