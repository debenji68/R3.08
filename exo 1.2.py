def plusgrand (a:int, b:int)->int:
    """
    :param a: un nombre choisi
    :param b: un nombre choisi
    :return: le plus grand des 2
    """
    if a > b:
        return a
    else:
        return b

#test de la fonctionplus garnd
print(plusgrand(3,4))
print(plusgrand(5,4))

#------------------------------------------------------------------------------------------------------------------------------------

def superieur (a:int, b=10)->int:

    """
    :param a: un nombre choisi
    :param b: un nombre défini
    :return: supérieur ou inférieur au paramètre b
    """
    if a > b:
        return (f"{a} est supérieur au seuil")
    else:
        return (f"{a} est inférieur au seuil")

#test de la fct superieur
print(superieur(4))
print(superieur(11))

#----------------------------------------------------------------------------------------------------------------------------------------

def plusgrandliste (a:list)->int:
    """
    :param a: une liste défini
    :return: le plus grand nombre de la liste
    """
    sup = a[0]  #création de la variable "sup" et incrémentation de la première valeur de la liste fournie
    for i in range(len(a)):
        if a[i] > sup:
            sup = a[i]
    return sup

#test de la fct plusgrandliste
print(plusgrandliste([1,2,9,4,5]))
print(plusgrandliste([1,2,3,4,5]))
print(plusgrandliste([-6,-2,-3]))

#----------------------------------------------------------------------------------------------------------------------------------------

def 