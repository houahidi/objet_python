# *-* coding:utf8 *-*
"""
 gestion des points 2D
"""
import math


class Point:
    """point en 2 D"""
    def __init__(self, abscisse=None, ordonnee=None):
        """initialiser les coordonnees d'un point"""
        if abscisse is None:
            abscisse = input("Saisir x:")
        if ordonnee is None:
            ordonnee = input("Saisir y:")

        self.abscisse = int(abscisse)
        self.ordonnee = int(ordonnee)

    def deplacer(self, diffx, diffy):
        """ changer les coordonnees du point"""

        self.abscisse += diffx  # equivalent point["x"] = point['x'] + diffx
        self.ordonnee += diffy

    def __str__(self):
        """afficher les coordonnees du point"""
        #print("Point(x:", point["x"], ",y:", point["y"], ")", sep="")
        return "Point(x:{0},y:{1})".format(self.abscisse, self.ordonnee)

    def distance(self, autrepoint):
        """calculer la distance entre les 2 points"""
        dx = self.abscisse - autrepoint.abscisse
        dy = self.ordonnee - autrepoint.ordonnee
        distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) )
        print("distance : {0:.2f}".format(distance))

    def __copy__(self):
        return Point(self.abscisse, self.ordonnee)

if __name__ == "__main__":
    POINT1 = Point(1, 1)
    print(POINT1.__str__())
    print(POINT1)
    print( "POINT1: " + str(POINT1)) # concatenation
    print("POINT1:", POINT1)
    print("deplacer le point diffx=3, diffy=8")
    POINT1.deplacer(3, 8)
    print(POINT1)
    POINT2 = Point(3, 2)
    print(POINT1)
    POINT1.distance(POINT2)
