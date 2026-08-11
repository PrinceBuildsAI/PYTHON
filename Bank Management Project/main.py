import json
import random
import string
from pathlib import Path


class Bank:
    database = r'C:\Users\singh\Desktop\Education\PROGRAMMING\PYTHON\Bank Management Project\data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")

    except Exception as err:
        print(f"An exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 5)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
        

    def createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email":input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance":0
            
        }
        if info['age'] < 18 or info['age'] > 100 or len(str(info['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            print()
            for i in info:
                print(f"{i} : {info[i]}")
            print()
            print("Please note down your account number")
            
            Bank.data.append(info)
            Bank.__update()

def depositmoney(self):


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for Desositing money in the bank")
print("Press 3 for withdrawing money")
print("Press 4 for account details")
print("Press 4 for Updating the details")
print("Press 6 for deleting your account")
print()
check = int(input("tell your resnonse: "))

if check == 1:
    user.createaccount()
if check == 2:
    user.depositemoney()
#! git commit
#! git commit 2
#! git commit 3
#! git commit 4
