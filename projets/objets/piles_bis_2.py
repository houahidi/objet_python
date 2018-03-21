"""
Gestion des piles de type FILO
"""
import copy


class PileException(Exception):
    """Erreur de manipulation de la pile"""

    def __init__(self, message="erreur de pile"):
        Exception.__init__(self, message)

    def __str__(self):
        return "PileException: erreur = {}".format(self.args[0])



class Pile(object):
    """
    Pile FILO
    """
    def __init__(self, taille):
        """initialiser la pile avec une taille"""
        self.taille = taille
        self.elements = []

    def empiler(self, element):
        """ajouter un element """
        if len(self) < self.taille:# if len(self.elements) < self.taille
            self.elements.append(element)
        else:
            raise PileException("La pile est pleine : taille {} est depassee".format(self.taille))

    def depiler(self):
        """retoune le dernier element empile"""
        if self.elements:
            return self.elements.pop(-1)
        else:
            raise PileException("La pile est vide")

    def __str__(self):
        """str(p) ==> p.__str__()"""
        return "Pile(taille:{}, nombre:{})".format(self.taille, len(self))

    def __len__(self):
        """calcule le nombre d'elements empiles"""
        return len(self.elements)

    def __copy__(self):
        clone = Pile(self.taille)
        clone.elements = copy.deepcopy(self.elements)
        return clone

    def __iter__(self):
        print("__iter__")
        return iter(self.elements[:])


if __name__ == "__main__":
    PILE1 = Pile(2)
    print(PILE1)
    try:
        PILE1.empiler("elem1")
        PILE1.empiler("elem2")
        PILE1.empiler("elem3")
    except PileException as e:
        print(e)
    print("==taille de la pile :", len(PILE1))
    indice = 1
    for elem in PILE1:
        print("iteration ", indice, "=", elem)
        indice += 1
    print("===")
    try:
        print("elem depile :", PILE1.depiler())
        print("elem depile :", PILE1.depiler())
        print("elem depile :", PILE1.depiler())
    except PileException as e:
        print(e)
    print("taille de la pile :", len(PILE1))

