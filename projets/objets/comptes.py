# *-* coding:utf8 -*-
"""
gestion des comptes bancaires
un compte a une numéro et un solde
"""


class Compte:

    def __init__(self, numero=None):
        """constructeur : initialiser un compte """
        if numero  is None:
            numero = input("saisir le num :")
        self.numero = numero
        self.solde = 100
        #pas besoin de retour: c'est le role d'un constructeur
        #return {"numero": numero, "solde": 100}

    def afficher(self):
        """ afficher le compte"""
        print("Compte(numero:{}, solde:{})".format(self.numero, self.solde))

    def crediter(self, somme):
        """
        crediter la somme
        """
        self.solde += somme

    def debiter(self, somme):
        """
        debiter la somme
        """
        if somme < self.solde:
            self.solde -= somme
        else:
            print("découvert non autorisé")


if __name__ == "__main__":
    CT1 = Compte(12)
    CT1.afficher()
    CT1.crediter(100)
    CT1.afficher()
    CT1.debiter(50)
    CT1.debiter(500)
    CT1.afficher()