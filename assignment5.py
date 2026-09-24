import re

string = input("Enter a string: ")

if re.fullmatch(r'[a-zA-Z0-9]+', string):
    print("Valid string")
else:
    print("Invalid string")