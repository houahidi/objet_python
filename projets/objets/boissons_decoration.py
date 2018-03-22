
"""
Ilusterer le design pattern Decorateur avec les boissons
"""

class Boisson(object):
    """boisson"""

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def lenom(self):
        return self.nom

    def leprix(self):
        return self.prix

    def __str__(self):
        return "{} prix : {}".format(self.lenom(), self.leprix())


class BoissonDecorateur(Boisson):

    def __init__(self, boisson, nom_ingredient, prix_ingrediant):
        Boisson.__init__(self, nom_ingredient, prix_ingrediant)
        self.boisson = boisson

    def leprix(self):
        return self.boisson.leprix() + self.prix

    def lenom(self):
        return self.boisson.lenom() + " au " + self.nom

if __name__ == "__main__":
    CAFE = Boisson("Cafe", 2.5)
    print(CAFE)
    CafeAuLait = BoissonDecorateur(CAFE, "lait", 1.4)
    print(CafeAuLait)
    CafeAuLaitChocalat = BoissonDecorateur(CafeAuLait, "choco", 3.0)
    print(CafeAuLaitChocalat)