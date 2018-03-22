"""
stockage d'objets avec pickle
"""

from objets.etudiants import Etudiant
import pickle

print("Stockage d'objet")

E1 = Etudiant("etudiant 1", "prenom 1", 10)
E2 = Etudiant("etudiant 2","prenom 1", 10)
E3 = Etudiant("etudiant 3","prenom 1", 10)

with open("etudiants.txt", "wb") as file:
    print("stocker E1, E2, E3")
    pickle.dump(E1, file)
    pickle.dump(E2, file)
    pickle.dump(E3, file)

with open("etudiants.txt", "rb") as file:
    print("lire les objets stockes")
    E1 = pickle.load(file)
    print(E1)
    E2 = pickle.load(file)
    print(E2)
    E3 = pickle.load(file)
    print(E3)


