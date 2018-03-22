# *-* coding:utf8 -*-
"""
gestion des comptes bancaires
un compte avec un numéro et un solde
"""


class Compte(object):

    def __init__(self, numero=None):
        """constructeur : initialiser un compte """
        if numero  is None:
            numero = input("saisir le num :")
        self.__numero = numero
        self.__solde = 100
        #pas besoin de retour: c'est le role d'un constructeur
        #return {"numero": numero, "solde": 100}

    def afficher(self):
        """ afficher le compte"""
        print("Compte(numero:{}, solde:{})".format(self.__numero, self.__solde))

    def crediter(self, somme):
        """
        crediter la somme
        """
        self.__solde += somme

    def debiter(self, somme):
        """
        debiter la somme
        """
        if somme < self.__solde:
            self.__solde -= somme
        else:
            print("découvert non autorisé")

    @property
    def numero(self):
        return self.__numero

    @property
    def solde(self):
        return self.__solde

    @solde.setter
    def solde(self, value):
        self.__solde = value




if __name__ == "__main__":
    CT1 = Compte(12)
    print("numero :", CT1.numero)
    #CT1.solde = 3000 # n'est pas autorise
    print("solde :", CT1.solde)
    CT1.afficher()
    CT1.crediter(100)
    CT1.afficher()
    CT1.debiter(50)
    CT1.debiter(500)
    CT1.afficher()