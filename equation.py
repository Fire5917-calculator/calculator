from math import * 
def equation_de_second_degres(a,b,c):
    discriminant = b**2 - (4*a*c)
    if discriminant < 0:
        print(f"Aucune solution dans les réels car le discrimainant est inférieur à 0 (discriminant = {discriminant})")
    elif discriminant == 0:
        alpha = -b/(2*a)
        print("Le discriminant vaut 0")
        print(f"La solution est alpha (alpha = {alpha})")
        print(f"S = ({alpha})")
    elif discriminant > 0:
        print(f"Le discriminant vaut {discriminant}")
        print("Le discriminant est supérieur à 0 donc l'équation possède 2 solutions dans les réels")
        x1 = (-b + sqrt(discriminant))/ (2 * a)
        x2 = (-b - sqrt(discriminant))/ (2*a)
        print(f"x1 = (-({b}) + √{discriminant})/(2 * {a})")
        print(f"<=> x1 = {x1}")
        print(f"x2 = (-({b}) - √{discriminant})/(2 * {a})")
        print(f"<=> x2 = {x2}")
        liste_resultat = [x1, x2]
        liste_resultat.sort()
        print(f"S = {liste_resultat}")
def equation_de_droite(m,p):
    print(m,'x + ', p, ' = 0')
    p = -p
    print("<=> ",m,"x = ",p)
    print("<=> x = (",p,")/(",m,")")
    x = p/m
    print("<=> x = ", x)

    

