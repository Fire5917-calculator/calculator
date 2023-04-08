def convertisseur_de_base(decimal,base):
    resultat = ""
    symboles = ["A", "B", "C", "D", "E", "F"]
    while decimal > 0:
        reste = decimal % base
        if reste < 10:
            resultat = str(reste) + resultat
        else:
            resultat = symboles[reste - 10] + resultat
        decimal = decimal // base
    return resultat
def convertisseur_output(decimal):
    print(f'Base 10     : {decimal}')
    print(f'Binaire     : {convertisseur_de_base(decimal, 2)}')
    print("Base 4      : ", convertisseur_de_base(decimal, 4))
    print("Base 8      : ", convertisseur_de_base(decimal, 8))
    print("Base 12     : ", convertisseur_de_base(decimal, 12))
    print("Hexadécimal : ", convertisseur_de_base(decimal, 16))