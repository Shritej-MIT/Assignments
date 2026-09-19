# PYTHON PROGRAM TO CHECK WHETHER THE TRIANGLE IS RIGHT-ANGLED TRIANGLE OR NOT

def is_right_triangle(a, b, c):

    # Find the largest side
    if a >= b and a >= c:
        return b * b + c * c == a * a

    elif b >= a and b >= c:
        return a * a + c * c == b * b

    else:
        return a * a + b * b == c * c


# Accept three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Function calling
if is_right_triangle(a, b, c):
    print("The triangle is a right-angled triangle.")
else:
    print("The triangle is not a right-angled triangle.")
