"""
Gestion des piles de type FILO
"""

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
            print("La pile est pleine : taille {} est depassee".format(self.taille))

    def depiler(self):
        """retoune le dernier element empile"""
        return self.elements.pop(-1)

        if self.elements:
            return self.elements.pop(-1)
        else:
            print("La pile est vide")

    def __str__(self):
        """str(p) ==> p.__str__()"""
        return "Pile(taille:{}, nombre:{})".format(self.taille, len(self))

    def __len__(self):
        """calcule le nombre d'elements empiles"""
        return len(self.elements)


if __name__ == "__main__":
    PILE1 = Pile(2)
    print(PILE1)
    PILE1.empiler("elem1")
    PILE1.empiler("elem2")
    PILE1.empiler("elem3")
    print("taille de la pile :", len(PILE1))
    print("elem depile :", PILE1.depiler())
    print("elem depile :", PILE1.depiler())
    print("elem depile :", PILE1.depiler())
    print("taille de la pile :", len(PILE1))

