import unittest

import App.operators as Operator


class UnitTest(unittest.TestCase):

    def test_negyzetgyok(self):
        # Tesztesetek:
        self.assertAlmostEqual(Operator.negyzetgyok(16), 4.0)  # 16 négyzetgyöke 4
        self.assertAlmostEqual(Operator.negyzetgyok(25), 5.0)  # 25 négyzetgyöke 5
        self.assertAlmostEqual(Operator.negyzetgyok(9), 3.0)   # 9 négyzetgyöke 3
        self.assertAlmostEqual(Operator.negyzetgyok(-12), 0)  # -12 négyzetgyöke 0
        self.assertAlmostEqual(Operator.negyzetgyok(14), 3.7416573867739413)  # nem egészre visszatérő érték ellenörzése
        self.assertAlmostEqual(Operator.negyzetgyok(4.5), 2.1213203435596424)  # nem egészre visszatérő érték ellenörzése

    def test_osszeadas(self):
        self.assertAlmostEqual(Operator.Addition(1,1),2)
        self.assertAlmostEqual(Operator.Addition(13,45),58)
        self.assertAlmostEqual(Operator.Addition(100,6543),6643)
        self.assertAlmostEqual(Operator.Addition(19765,20),19785)