import os
from pathlib import Path

path = Path(
    r"C:\\Users\\singh\\Desktop\\Education\\PROGRAMING\\PYTHON\\Chapter 8 (Exception handling)\\Project")


def readfileandfolder():
    items = list(path.rglob("*"))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = path / name
        if not p.exists() or not p.is_file():
            with open(p, "w") as fs:
                data = input("What you want to write in this file: ")
                fs.write(data)

            print(f"FILE CREATED SUCCESSFULLY\n")
        else:
            print("File already exists\n")
    except Exception as err:
        print(f"An error occurred as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read:")
        p = path / name
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)

            print("READ SUCCESSFULLY\n")
        else:
            print("File does not exist\n")
    except Exception as err:
        print(f"An error occurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Tell me which file you wants to update: ")
        p = path / name
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file: ")
            print("Press 2 for overwriting the data in your file: ")
            print("Press 3 for appending some content in your file: ")

            res = int(input("tell your response: "))

            if res == 1:
                name2 = input("Tell your new file name: ")
                p2 = path / name2
                p.rename(p2)

            if res == 2:
                with open(p, "w") as fs:
                    data = input("Overwrite the data: ")
                    fs.write(data)

            if res == 3:
                with open(p, "a") as fs:
                    data = input("Append the data: ")
                    fs.write(" " + data)
    except Exception as err:
        print(f"An error occur as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of file you wants to delete: ")
        p = path / name

        if p.exists and p.is_file:
            os.remove(p)
    except Exception as err:
        print(f"An error occurred as {err}")
while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file\n")

    check = int(input("Please tell me your response: "))

    if check == 1:
        createfile()

    if check == 2:
        readfile()

    if check == 3:
        updatefile()

    if check == 4:
        deletefile()
    continue

