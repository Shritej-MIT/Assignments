import re

pan = input("Enter PAN number: ")

pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]$"

if re.fullmatch(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
