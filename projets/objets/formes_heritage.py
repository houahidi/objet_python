"""
gestion des rectangles

"""
from copy import copy

import math

from objets import points


class Forme(object):
    """
    Forme geometrique avec un point d'origine
    """
    def __init__(self, origine):
        """ creation d'une forme"""
        self.origine = copy(origine) #from copy import copy

    def __str__(self):
        """x.__str__() => str(x)"""
        return "Forme: origine={}".format(self.origine)

    def surface(self):
        """calcul de la surface"""
        return None

    def perimetre(self):
        """calcul du perimetre"""
        return None

    def deplacer(self, deplx, deply):
        """ deplace la forme geometrique"""
        self.origine.deplacer(deplx, deply)


class Rectangle(Forme):
    """
    Rectangle avec longueur et largeur
    """
    def __init__(self, origine, long, larg ):
        """ creation d'un rectangle"""
        Forme.__init__(self, origine)
        #super().__init__(origine)
        self.long = float(long)
        self.larg = float(larg)

    def __str__(self):
        """x.__str__() => str(x)"""
        return "Rectangle: long = {:.2f}, larg={:.2f}, origine={}".format(self.long, self.larg, self.origine)

    def surface(self):
        """calcul de la surface"""
        return self.long * self.larg

    def perimetre(self):
        """calcul du perimetre"""
        return 2 * (self.long + self.larg)



class Cercle(Forme):
    """
    Cercle avec un rayon et un point d'origine
    """

    def __init__(self,origine, rayon):
        """ creation d'un rectangle"""
        Forme.__init__(self, origine)
        self.rayon = float(rayon)

    def __str__(self):
        """x.__str__() => str(x)"""
        return "Cercle: rayon = {:.2f}, origine={}".format(self.rayon, self.origine)

    def surface(self):
        """calcul de la surface"""
        return math.pi * self.rayon ** 2

    def perimetre(self):
        """calcul du perimetre"""
        return 2 * math.pi * self.rayon


if __name__ == "__main__":
    PT1 = points.Point(1, 2)
    print(PT1)
    REC1 = Rectangle(PT1, 3, 3)
    REC2 = Rectangle(PT1, 4, 6)
    print("REC1:", REC1)
    print("surface :", REC1.surface())
    print("perimetre :", REC1.perimetre())
    print("REC1:", REC1)
    print("REC2:", REC2)
    print("deplacer REC1 avec 3, 6")
    REC1.deplacer(3, 6)
    print("REC1:", REC1)
    print("REC2:", REC2)
    CER1 = Cercle(PT1, 3)
    print("Cercle CER1:", CER1)
    print("surface :", CER1.surface())
    print("perimetre :", CER1.perimetre())
    print("deplacer REC1 avec 1, 6")
    CER1.deplacer(1, 6)
    print("Cercle CER1:", CER1)

