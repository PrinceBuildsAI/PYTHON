
#! Write a generator function that yields even number up to a specific limit

def even_generator(limit):
    for i in range(2, limit +1,2):
        yield i #also used as return but i dont store value in it

for num in even_generator(10):
    print(num)