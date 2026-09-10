# Take three sides as input from the user
side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# Sort the sides so the largest side is always at the end (hypotenuse 'c')
sides = sorted([side1, side2, side3])
a = sides[0]
b = sides[1]
c = sides[2]

# Check if a² + b² is equal to c²
if (a**2 + b**2) == c**2:
    print("Yes, it is a right-angled triangle!")
else:
    print("No, it is not a right-angled triangle.")
