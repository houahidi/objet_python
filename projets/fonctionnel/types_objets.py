
# les listes : ensemble d'objets modifiable avec doublon
tableau = [1]
#tableau = list()
print("tableau :", tableau, "type : ", type(tableau))
tableau.append("elem")
tableau.append(10)
tableau.append(True)
print("tableau :", tableau)
tableau[0]=10
print("tableau :", tableau)
print("dernier : ", tableau[-1])
print("dernier : ", tableau[ len(tableau) - 1])
print("dernier : ", tableau[ tableau.__len__() - 1])
print("tableau :", tableau)
print("premier ajoute : ", tableau.pop(0))
print("tableau :", tableau)
tableau.extend("elem")
print("tableau :", tableau)
# affectation par reference
liste = tableau
print("liste:", liste)
print("tableau:", tableau)
liste.append("new elem")
print("liste:", liste)
print("tableau:", tableau)

