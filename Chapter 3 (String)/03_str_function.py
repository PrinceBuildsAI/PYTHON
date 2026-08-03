name = "Harry"

print(len(name))
print(name.endswith("rry"))         #output ="True"
print(name.endswith("ay"))
print()

print(name.startswith("Ha"))
print(name.startswith("ha"))        # cahpiat letter "H" and small letter "h" both are different
                                    # case sensitive
print(name.capitalize())
print(name.upper())                     # "HARRY"-> lower(): Convert the string to lowercase 
print(name.lower())                     # "harry"-> upper(): Convert the string to uppercase 
print(name.strip())                     # "Harry"-> strip(), lstrip(), rstrip(): Remove whitespace characters from the beginning, left end, or right end of the string.
print(name.split(", "))                 # "['Harry']"-> split(): Splits the string into a list of substrings based on a delimiter.
print("-".join(["a", "b", "c"]))        # "a-b-c"-> join(): Concatenates strings from an iterable into a single string with a specified separator.  
print(name.replace("Harry", "Prince"))  # "Prince"-> replace(): Replaces occurrences of a substring with another substring.
