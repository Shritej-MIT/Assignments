# PYTHON PROGRAM TO CHECK WHETHER THE TRIANGLE IS RIGHT-ANGLED TRIANGLE OR NOT

def check_triangle(a, b, c):
    if a*a + b*b == c*c:
        return True
    else:
        return False
