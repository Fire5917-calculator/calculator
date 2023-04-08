from sympy import *
x = symbols('x')
def expression_derivee_fonction(f):
    f_prime = diff(f,x)
    return(f_prime)

print(f"La dérivée de 5x + 3 est {expression_derivee_fonction(5*x + 3)}")
