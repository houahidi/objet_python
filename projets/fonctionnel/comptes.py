# *-* coding:utf8 -*-
"""
gestion des comptes bancaires
un compte a une numéro et un solde
"""


def init(numero=None):
    """initialiser un compte """
    if numero  is None:
        numero = input("saisir le num :")
    return {"numero": numero, "solde": 100}


def afficher(compte):
    """ afficher le compte"""
    print("Compte(numero:{}, solde:{})".format(compte["numero"], compte["solde"]))


def crediter(compte, somme):
    """
    crediter la somme
    """
    compte["solde"] += somme


def debiter(compte, somme):
    """
    debiter la somme
    """
    if somme < compte["solde"]:
        compte["solde"] -= somme
    else:
        print("découvert non autorisé")


if __name__ == "__main__":
    CT1 = init()
    afficher(CT1)
    crediter(CT1, 100)
    afficher(CT1)
    debiter(CT1, 50)
    debiter(CT1, 500)
    afficher(CT1)