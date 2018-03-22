

class MaClasse:

    def __init__(self, param):
        self.__attribut = param

    def methode(self):
        print("__attribut", self.__get__attribut())

    def __get__attribut(self):
        return self.__attribut

    def __set__attribut(self, value):
        self.__attribut = value + " set__"

    attribut = property(__get__attribut, # methode de consultation
                        __set__attribut, #methode de modification
                        None, #methode de suppression
                        "attribut public", #commentaire associe a la propriete
                        )


if __name__ == "__main__":
    INST1 = MaClasse("val1")
    help(MaClasse)
    print("attribut : ", INST1.attribut)
    INST1.attribut = "new Value"
    print("attribut : ", INST1.attribut)
    #del(INST1.attribut)
    print("attribut : ", INST1.attribut)

