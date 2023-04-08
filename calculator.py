from math import *
from pystyle import Box
from sympy import *
import colorama
import suite, calcul, fonction, equation, binary, geometrie, derivation
print(f"{colorama.Fore.GREEN}Calculator By {colorama.Fore.YELLOW}Fire5917 {colorama.Fore.MAGENTA}| {colorama.Fore.GREEN}Version {colorama.Fore.MAGENTA}>>> {colorama.Fore.RED}v0.0")
print(colorama.Fore.RESET)
options = """MENU PRINCIPAL

[01] Equations
[02] Convertisseur de base
[03] Géométrie
[04] Calcul
[05] Fonction
[06] Dérivation
"""
options_equations = """EQUATION

[01] Equation du second degrès
[02] Equation de droite
"""
options_geometrie = """GEOMETRIE

[01] Pythagore
"""
options_calcul = """CALCUL

[01] Calcul sans variable
[02] Calcul avec variables
"""
options_pythagore = """PYTHAGORE

[01] Trouver l'hypothènuse
[02] Trouver un autre coté
"""
options_fonction = """FONCTIONS

[01] Tracer la courbe d'une fonction
"""
options_derivation = """DERIVATION

[01] Obtenir l'expression de la dérivée d'une fonction
"""
while True:
    print(Box.Lines(options))
    choice = int(input("Quel est votre choix? >>> "))
    if choice == 1:
        print(Box.Lines(options_equations))
        choice = int(input("Quel est votre choix? >>> "))
        if choice == 1:
            print('Votre équation se trouve sous la forme ax² + bx + c')
            valeur_a = float(input("Valeur de a >>> "))
            valeur_b = float(input("Valeur de b >>> "))
            valeur_c = float(input("Valeur de c >>> "))
            equation.equation_de_second_degres(valeur_a,valeur_b,valeur_c)
        if choice == 2:
            print("Votre équation se trouve sous la forme mx + p")
            valeur_m = float(input("Quelle est la valeur de m? >>> "))
            valeur_p = float(input("Quelle est la valeur de p? >>> "))
            equation.equation_de_droite(valeur_m, valeur_p)
    elif choice == 2:
        decimal = int(input("Quel est le nombre à convertir (en décimal / base 10) (seulement des entiers)>>> "))
        binary.convertisseur_output(decimal)
    elif choice == 3:
        print(Box.Lines(options_geometrie))
        choice = int(input("Quel est votre choix? >>> "))
        if choice == 1:
            print(Box.Lines(options_pythagore))
            choice = int(input("Quel est votre choix? >>> "))
            if choice == 1:
                a = float(input("Combien mesure votre premier coté? >>> "))
                b = float(input("Combien mesure votre 2eme coté? >>> "))
                print(f"L'hypothènuse mesure {geometrie.pythagore_pour_trouver_hypothènuse(a,b)}")
            elif choice == 2:
                longeur_hypo = float(input("Quelle est la longueur de l'hypothènuse? >>> "))
                longueur_autre_coté = float(input("Quelle est la longueur de l'autre coté? >>> "))
                print(f"La longueur du coté restant est {geometrie.pythagore_pour_trouver_autre_cote(longueur_autre_coté, longeur_hypo)}")
    elif choice == 4:
        print(Box.Lines(options_calcul))
        choice = int(input("Quel est votre choix? >>> "))
        print("""Dans l'expression de vos calcul certains signes doivent être remplacer par d'autre:
        5 x 5 (5 fois 5) --> 5*5
        √5 --> sqrt(5)
        Par exemple 5 x 5 x √(5-2) --> 5*5*sqrt(5-2)
        Attention aux parenthèses!
        
        """)
        if choice == 1:
            calcul_a_faire = input("Entrer votre calcul >>> ")
            print(f"Le résultat est : {calcul.calculer(calcul_a_faire)}")
        if choice == 2:
            calcul_a_effectuer = input("Quel estt le calcul à faire (la variable doit être x ou y) (2 variables max dans un calcul) >>> ")
            x = symbols('x')
            y = symbols('y')
            print(f"Le résultat de votre calcul est : {calcul.calculer_avec_variable(calcul_a_effectuer)}")
    elif choice == 5:
        print(Box.Lines(options_fonction))
        choice = int(input("Quel est votre choix? >>> "))
        if choice == 1:
            print("""Dans l'expression de votre fonction certains symboles doivent être remplacer par d'autre:
    5 x 5 (5 fois 5) --> 5*5
    √5 --> sqrt(5)
    Par exemple 5 x 5 x √(5-2) --> 5*5*sqrt(5-2)
    Attention aux parenthèses!
    """)
            function_expression = input("Entrez l'expression de la fonction f(x): ")
            start_value = float(input("Entrez le début de l'intervalle: "))
            end_value = float(input("Entrez la fin de l'intervalle: "))
            step_value = float(input("Entrez la précision: "))
            fonction.plot_function(start_value,end_value,step_value,function_expression)
    elif choice == 6:
        print(Box.Lines(options_derivation))
        choice = int(input("Quel est votre choix? >>> "))
        if choice == 1:
            expression = input("Quelle est l'expression de votre fonction ? >>> ")
            x = symbols('x')
            print(f"La dérivée de {expression} est {derivation.expression_derivee_fonction(expression)}")
            



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    input("Appuyez sur entrée pour continuer...")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

