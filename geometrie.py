from math import *
def pythagore_pour_trouver_hypothènuse(cote1, cote2):
    return sqrt(cote1**2 + cote2**2)
def pythagore_pour_trouver_autre_cote(cote1, hypothenuse):
    return sqrt(hypothenuse**2 - cote1**2)