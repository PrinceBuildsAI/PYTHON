
marks = {
    "harry": 100,
    "shubham": 56,
    "rohan": 24,
    2:"prince"
}

# print(marks.items())        #It prints all the items in dictonary
# print(marks.keys())         #It prints all the left and side element of dictonary
# print(marks.values())       #It prints all the right hand side element of dictonary
marks.update({"harry":99, "renu": 100})    #It is because dictonary is mutable
print(marks)
print(marks["renu"])
  