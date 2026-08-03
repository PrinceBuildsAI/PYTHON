a = 31
t = type(a)  #class <int>
print(t)

b = 31.5
t = type(b)
print(t)

c = "Harry"
t = type(c)
print(t)

 # A number can be converted into a string and vice versa (if possible)
d = "31.2"
e = float(a)    # String to float conversion
f = int(a)      # String to integer conversion   
t = type(e)
t = type(f)
print(t)