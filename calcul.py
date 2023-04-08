from math import *
from sympy import *
def calculer(expression):
    expression = expression.replace("²", "**2")
    expression = expression.replace("^", "**")
    return eval(expression)
def calculer_avec_variable(expression):
    return simplify(expression)
