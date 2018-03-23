"""test case pour pile"""

import unittest
from objets.pile import Pile, PileException
import logging.config


class PileTestCase(unittest.TestCase):
    """unit test"""

    @classmethod
    def setUpClass(cls):
        logging.config.fileConfig("../fonctionnel/logging.conf")
        cls.logger = logging.getLogger("logger1")
        cls.logger.info("init unit test class once")

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("cleanup unit test class once")

    def setUp(self):
        """executed before each individual test"""
        self.logger.info("initialiser la pile")
        self.__pile = Pile(1)
        self.__nombre = 0
        self.__elem = "elem1"

    def tearDown(self):
        """executed after each individual test"""
        self.logger.info("cleanup unit test")

    def testEmpiler(self):
        self.logger.info("testEmpiler")
        try:
            self.__pile.empiler(self.__elem)
            resultatAttendu = self.__nombre + 1
            resultatCalcule = len(self.__pile)
            self.assertEqual(resultatAttendu, resultatCalcule)
        except Exception as e:
            self.fail(e)

    def testDepiler(self):
        self.logger.info("testDepiler")
        try:
            self.__pile.empiler(self.__elem)
            elem = self.__pile.depiler()
            self.assertIsNotNone(elem)
            self.assertEqual(elem, self.__elem)
        except Exception as e:
            self.fail(e)

    def testPilePleine(self):
        self.logger.info("testPilePleine")
        try:
            self.__pile.empiler(self.__elem)
            self.assertRaises(PileException,
                              self.__pile.empiler,
                              self.__elem)
        except Exception as e:
            self.logger.error("testPilePleine failed")
            self.fail(e)

    def testPileVide(self):
        self.logger.info("testPileVide")
        try:
            #self.__pile.empiler(self.__elem)
            self.assertRaises(PileException,
                              self.__pile.depiler)
        except Exception as e:
            self.logger.error("testPileVide failed")
            self.fail(e)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'PileTestCase.Empiler']

    unittest.main()