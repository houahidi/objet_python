import unittest

from objets import piles


class PileTestCase(unittest.TestCase):
    """test de la classe pile"""

    def setUp(self):
        print("initialiser la pile")
        self.__pile = piles.Pile(1)
        self.__nombre = 0
        self.__elem = "elem1"

    def tearDown(self):
        print("apres chaque test")

    # @classmethod
    # def setUpClass(cls):
    #     print("avant tous les test")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("apres tous les test")

    def testEmpiler(self):
        print("testEmpiler")
        try:
            self.__pile.empiler( self.__elem)
            resultatAttendu = self.__nombre + 1
            resultatCalcule = len(self.__pile)
            self.assertEqual(resultatAttendu, resultatCalcule)
        except Exception as e:
            self.fail(e)

    def testDepiler(self):
        print("testDepiler")
        try:
            self.__pile.empiler(self.__elem)
            elem = self.__pile.depiler()
            self.assertIsNotNone(elem)
            self.assertEqual(elem, self.__elem)
        except Exception as e:
            self.fail(e)

    def testPilePleine(self):
        print("testPilePleine")
        try:
            self.__pile.empiler(self.__elem)
            self.assertRaises(piles.PileException,
                              self.__pile.empiler,
                              self.__elem)

        except Exception as e:
            self.fail(e)


if __name__ == "__main__":
    unittest.main()