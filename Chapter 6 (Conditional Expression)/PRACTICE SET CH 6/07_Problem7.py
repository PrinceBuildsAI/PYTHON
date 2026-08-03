#Q.7  Write a program to find out whether a given post is talking about “Prince” or not.

post = input("Enter the post:")

if("Prince".lower() in post.lower()):
    print("This post is talking about prince")

else:
    print("his post is not talking about Prince")