import json
import random
import string
from pathlib import Path


class Bank:
    database = r"C:\Users\singh\Desktop\Education\PROGRAMMING\PYTHON\Bank Management Project\data.json"
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
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=5)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0,
        }
        if info["age"] < 18 or info["age"] > 100 or len(str(info["pin"])) != 4:
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

<<<<<<< HEAD
    def depositemoney(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        userdata = [
            i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if not userdata:
            print("Sorry no data found")
        else:
            amount = int(input("How much you want to deposite: "))
            if amount > 10000 or amount < 0:
                print("Sorry the ammount is too much you can deposite below 10000")

            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print("Amount deposite successfully")

    def withdrwamoney(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        userdata = [
            i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if userdata == False:
            print("Sorry no data found")
        else:
            amount = int(input("How much you want to withdraw: "))
            if userdata[0]["balance"] < amount:
                print("Sorry can't withdraw money")

            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdrew successfully")

    def showdetails(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))
        print()

        userdata = [
            i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        print("Your information are: \n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accnumber = input("Enter your Account number: ")
        pin = input("Enter your Pin: ")

        userdata = [
            i
            for i in Bank.data
            if i["accountNo."] == accnumber and str(i["pin"]) == pin
        ]

        if not userdata:
            print("No such user found")
            return

        print("You cannot change the age, account number, balance")
        print("Fill the details for change or leave it empty if no change")

        newdata = {
            "name": input("Please tell your name or Press enter to skip: "),
            "email": input("Please enter your new email or press Enter to skip: "),
            "pin": input("Enter your new pin or Press enter to skip: "),
        }

        if newdata["name"] == "":
            newdata["name"] = userdata[0]["name"]

        if newdata["email"] == "":
            newdata["email"] = userdata[0]["email"]

        if newdata["pin"] == "":
            newdata["pin"] = userdata[0]["pin"]
        else:
            newdata["pin"] = int(newdata["pin"])

        newdata["age"] = userdata[0]["age"]
        newdata["accountNo."] = userdata[0]["accountNo."]
        newdata["balance"] = userdata[0]["balance"]

        userdata[0].update(newdata)

        Bank.__update()

    print("Details updated successfully")

    def deleteaccount(self):
        accnumber = input("Enter your Account number: ")
        pin = int(input("Enter your Pin: "))

        userdata = [
            i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin
        ]

        if userdata == False:
            print("Sorry no such data exist")
        else:
            check = input("Press y to delete your account n to skip: ")
            if check == "n" or check == "N" or check == "no":
                print("Nothing change")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account delete successfuly")
                Bank.__update()
=======
def depositmoney(self):
>>>>>>> b5301536f34e6fc3ce97a69f57f81f1e3f9fc579


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for Desositing money in the bank")
print("Press 3 for withdrawing money")
print("Press 4 for account details")
print("Press 5 for Updating the details")
print("Press 6 for deleting your account")
print()
check = int(input("tell your resnonse: "))

if check == 1:
    user.createaccount()
if check == 2:
    user.depositemoney()
<<<<<<< HEAD
if check == 3:
    user.withdrwamoney()
if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.deleteaccount()
=======
#! git commit
#! git commit 2
#! git commit 3
#! git commit 4
>>>>>>> b5301536f34e6fc3ce97a69f57f81f1e3f9fc579
