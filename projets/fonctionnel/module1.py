import sys

print("====debut programme principal", __name__)

print("path python : ", sys.path)
print("argument du programme :", sys.argv)


from fonctionnel.fonctions import *

moyenne(1, 4, 6)
moyennes = []
print("====", moyennes)
moyenneBis(moyennes, 1, 4, 6)
print("====", moyennes)
print("====fin programme principal", __name__)

