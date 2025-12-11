import math
def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return "L'équation est indéterminée (toutes les valeurs de x sont solutions)."
        else:
            return "L'équation est impossible (aucune solution)."
    else:
        x = -b / a
        return f"La solution est x = {x}"
def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)
    
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Les solutions sont x1 = {x1} et x2 = {x2}"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"La solution double est x = {x}"
    else:
        return "L'équation n'a pas de solutions réelles."
print("Choisissez le type d'équation :")
print("1. Équation du premier degré (ax + b = 0)")
print("2. Équation du deuxième degré (ax² + bx + c = 0)")
choice = int(input("Votre choix (1 ou 2) : "))
if choice == 1:
    a = float(input("Entrez a : "))
    b = float(input("Entrez b : "))
    result = solve_linear(a, b)
    print(result)
elif choice == 2:
    a = float(input("Entrez a : "))
    b = float(input("Entrez b : "))
    c = float(input("Entrez c : "))
    result = solve_quadratic(a, b, c)
    print(result)
else:
    print("Choix invalide.")