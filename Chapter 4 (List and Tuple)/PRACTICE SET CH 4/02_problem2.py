#Q.2  Write a program to accept marks of 6 students and display them in a sorted manner.

Marks = []

f1 = int(input("Enter Marks of first student :"))
Marks.append(f1)
f2 = int(input("Enter Marks of second student :"))
Marks.append(f2)
f3 = int(input("Enter Marks of third student :"))
Marks.append(f3)
f4 = int(input("Enter Marks of fourth student :"))
Marks.append(f4)
f5 = int(input("Enter Marks of fifth student :"))
Marks.append(f5)
f6 = int(input("Enter Marks of sixth student :"))
Marks.append(f6)

Marks.sort()            #arrange marks in ascending order

print(Marks)
