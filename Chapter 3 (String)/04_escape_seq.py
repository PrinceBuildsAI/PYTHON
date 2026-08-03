"""(1) F\n: Newline - Moves the cursor to the beginning of the next line."""

#Example of escape sequence characters->\n, \t, ;, \\
a = "Prince is a good boy\nbut not a bad boy " #\n is used for creating a new line
print(a)

"""(2) For add[" "] (Double Quotation Marks) in string"""

b = "Hello my name is \"Prince\""  # We have to use \"(text)\" for enter [" "] (Double Quotation Marks)
print(b)

"""(3) \t: Tab - Moves the cursor to the next tab stop. """

print("hello\tworld")               # Hello   World

"""(4) \': Single Quote - Represents a single quote character within a string surrounded by single quotes. """

print("'It\'s a beautiful day'")    # It's a beautiful day

"""(5) \\: Backslash - Represents a single backslash character."""
 
print("C:\\Users\\John\\Desktop")   # C:\Users\John\Desktop

"""(6) \b: Backspace - Moves the cursor back one character (does not erase the character)."""

print("Hello\bWorld")               # HellWorld

"""(7) \r: Carriage Return - Moves the cursor to the beginning of the line (useful in some terminal applications)."""

print("Hello\rWorld")               # World

"""\xhh: Hexadecimal Escape - Represents a character specified by two hexadecimal digits(ASCII characters value)."""

print("\x48\x65\x6c\x6c\x6f")

 
