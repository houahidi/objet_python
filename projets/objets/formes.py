"""
gestion des rectangles

"""
from objets import points


class Rectangle:
    """
    Rectangle avec longueur et largeur
    """
    def __init__(self, long, larg):
        """ creation d'un rectangle"""
        self.long = float(long)
        self.larg = float(larg)

    def __str__(self):
        """x.__str__() => str(x)"""
        return "Rectangle: long = {:.2f}, larg={:.2f}".format(self.long, self.larg)

    def surface(self):
        """calcul de la surface"""
        return self.long * self.larg

    def perimetre(self):
        """calcul du perimetre"""
        return 2 * (self.long + self.larg)


if __name__ == "__main__":
    PT1 = points.Point(1, 1)
    print(PT1)
    REC1 = Rectangle(3, 3)
    print("REC1:", REC1)
    print("surface :", REC1.surface())
    print("perimetre :", REC1.perimetre())