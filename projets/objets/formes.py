"""
gestion des rectangles

"""
from copy import copy

from objets import points


class Rectangle:
    """
    Rectangle avec longueur et largeur
    """
    def __init__(self, long, larg, origine):
        """ creation d'un rectangle"""
        self.long = float(long)
        self.larg = float(larg)
        #self.origine = points.Point(origine.abscisse, origine.ordonnee)
        #self.origine = origine.__copy__()
        self.origine = copy(origine)


    def __str__(self):
        """x.__str__() => str(x)"""
        return "Rectangle: long = {:.2f}, larg={:.2f}, origine={}".format(self.long, self.larg, self.origine)

    def surface(self):
        """calcul de la surface"""
        return self.long * self.larg

    def perimetre(self):
        """calcul du perimetre"""
        return 2 * (self.long + self.larg)

    def deplacer(self, deplx, deply):
        self.origine.deplacer(deplx, deply)


if __name__ == "__main__":
    PT1 = points.Point(1, 2)
    print(PT1)
    REC1 = Rectangle(3, 3, PT1)
    REC2 = Rectangle(4, 6, PT1)
    print("REC1:", REC1)
    print("surface :", REC1.surface())
    print("perimetre :", REC1.perimetre())
    print("REC1:", REC1)
    print("REC2:", REC2)
    print("deplacer REC1 avec 3, 6")
    REC1.deplacer(3, 6)
    print("REC1:", REC1)
    print("REC2:", REC2)
