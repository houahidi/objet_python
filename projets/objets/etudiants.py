"""
gestion des etudiants
"""
from numpy import random


class Etudiant(object):
    """etudiant"""
    def __init__(self, nom, prenom, note):
        self.nom = nom
        self.prenom = prenom
        self.note = note
    def __str__(self):
        return "Etudiant: nom:{}, prenom:{}, note:{}".format(self.nom,
                                                             self.prenom,
                                                             self.note)

    def __gt__(self, autreetudiant):
        return self.note > autreetudiant.note

    def __radd__(self, somme):
        return somme + self.note


if __name__ == "__main__":
    liste = [3, 8, 0]
    print("max : ", max(liste))
    print("min : ", min(liste))

    E1 = Etudiant("nom1", "prenom1", 12)
    print(E1)
    E2 = Etudiant("nom2", "prenom2", 10)
    print(E2)
    E3 = Etudiant("nom3", "prenom3", 11)
    print(E3)
    LiSTE = [E1, E2, E3]
    print("meilleur etudiant :", max(LiSTE))
    print("mauvais etudiant :",  min(LiSTE))
    print("somme des notes : ", sum(LiSTE))
    print("moyenne des notes : ", sum(LiSTE)/len(LiSTE))
