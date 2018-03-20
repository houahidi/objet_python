"""

ensemble de cle valeur avec unite de la cle
"""

personne1 = {"nom": "OUAHIDI", "ville":  "Nice"}
print("personne1 : ", personne1, "type :", type(personne1))
personne1["nom"] = "ouahidi"
print("personne1 : ", personne1)
personne1["prenom"] = "Hafid"
print("personne1 : ", personne1)
print("taille : ", len(personne1))
print(personne1.values())
print("ouahidi" in personne1)


print("__name__:", __name__)
print("__file__:", __file__)
print("__doc__", __doc__)

