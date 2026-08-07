
#! Greetings and return a default value if no value is given

def greet(name ="user"):
    return "Hello, " + name + "!"

print(greet())
print(greet("Prince"))