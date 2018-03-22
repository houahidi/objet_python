from functools import reduce

from objets.etudiants import Etudiant

def filtrerEtudiants(e):
    return e.note >= 11

E1 = Etudiant("nom1", "prenom1", 12)
print(E1)
E2 = Etudiant("nom2", "prenom2", 10)
print(E2)
E3 = Etudiant("nom3", "prenom3", 11)
print(E3)
LiSTE = [E1, E2, E3]

print("taille LiSTE ", len(LiSTE))
etudiants = list(filter(lambda e: e.note >= 11, LiSTE))
print("etudiants filtres ", etudiants)


etudiants = filter(filtrerEtudiants, LiSTE)
print("taille etudiants ", len(list(etudiants)))
notes = map(lambda e: e.note, LiSTE)
print("type : ", type(notes))
print(help(notes))
print("les notes  ", list(notes))
print("taille   ",len(list(notes)))

