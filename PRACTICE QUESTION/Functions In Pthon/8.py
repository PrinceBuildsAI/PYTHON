
#! **Kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    
print_kwargs(power="laser",name="Alice")
print_kwargs(power="laser")
print_kwargs(name="Alice", surname = "Wake")