"""
fonctions a nombre variable de parametres
"""

def moyenne(*args):
    print("params : ", args)
    moyenne = sum(args)/len(args)
    return moyenne



def moyenneBis(moyennes, *args):
    print("params : ", args)
    moyenne = sum(args)/len(args)
    moyennes.append(moyenne)




def demarrer(**kwargs):
    print("kwargs:", kwargs)
    if "ip" in kwargs:
        print("demarrer avec ip :", kwargs["ip"])
    elif "host" in kwargs:
        print("demarrer avec host :", kwargs["host"])
    elif "dns" in kwargs:
        print("demarrer avec dns :", kwargs["dns"])
    else:
        print("ip, host ou dns manquant")


if __name__ != "__main__":
    resultat1 = moyenne(2)
    print("resultat1: ", resultat1)
    resultat2 = moyenne(1, 2, 5)
    print("resultat2 :", resultat2)
    resultat3 = moyenne(1, 4, 7, 8, 0, 6)
    print("resultat3: ", resultat3)




    moyennes = []
    print("moyennes :", moyennes)
    moyenneBis(moyennes, 2, 5, 7)
    print("moyennes", moyennes)
    moyenneBis(moyennes, 2, 5)
    print("moyennes", moyennes)



    demarrer(ip="192.168.1.1")
    demarrer(host="mw1321", dns="mw112@orsys.fr")
    dico = {"ip":"192.99.0.1"}

    demarrer(**dico)
