'''Random number guess b/w 1 to 10'''
import random
num = random.randint(1,10)
count = 0
while True:
    a = int(input("Enter your number: "))

    if a>num:
        print("lower the number")
    elif(a<num):
        print("Increase the number")
    elif a == num:
        print(f"Congratulation! you guess the number {num}")
    count = count + 1
    print(f"Number of attempts: {count}\n")
    




