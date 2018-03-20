# *-* coding:utf8 *-*
"""
 gestion des points 2D
"""
import math


def init(abscisse=None, ordonnee=None):
    """initialiser les coordonnees d'un point"""
    if abscisse is None:
        abscisse = input("Saisir x:")
    if ordonnee is None:
        ordonnee = input("Saisir y:")

    return {"x": int(abscisse), "y": int(ordonnee)}


def deplacer(point, diffx, diffy):
    """ changer les coordonnees du point"""

    point["x"] += diffx  # equivalent point["x"] = point['x'] + diffx
    point["y"] += diffy

def afficher(point):
    """afficher les coordonnees du point"""
    #print("Point(x:", point["x"], ",y:", point["y"], ")", sep="")
    strpoint = "Point(x:{0},y:{1})".format(point["x"], point["y"])
    print(strpoint)


def distance(point1, point2):
    """calculer la distance entre les 2 points"""
    dx = point1["x"] - point2["x"]
    dy = point1["y"] - point2["y"]
    distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2) )
    print("distance : {}".format(distance))
    print("distance : {0:.2f}".format(distance))
    print("distance : %.2f" % (distance))


if __name__ == "__main__":
    POINT1 = init(1, 1)
    afficher(POINT1)
    print("deplacer le point diffx=3, diffy=8")
    deplacer(POINT1, 3, 8)
    afficher(POINT1)
    POINT2 = init(3, 2)
    afficher(POINT2)
    distance(POINT1, POINT2)
