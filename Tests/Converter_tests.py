import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import unittest
from App.Converter import Converter as C

class Converter_test(unittest.TestCase):
    Dist_units: list = ["mm", "cm", "dm", "m", "km", "miles"]
    Vol_units: list = ["ml","cl","dl","l","hl","m^3"]
    Weight_units: list = ["g", "dkg", "kg"]
    def test_Convert_unit_mm(self):
        results: list = [10, 1, 0.1, 0.01, 0.00001, 0.00000625]
        for i in range(len(self.Dist_units)):
            self.assertEqual(C(10,"mm",self.Dist_units[i],"Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response mm to {self.Dist_units[i]}")

    def test_Convert_unit_cm(self):
        results: list = [100, 10, 1, 0.1, 0.0001, 0.0000625]
        for i in range(len(self.Dist_units)):
            self.assertEqual(C(10, "cm", self.Dist_units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response cm to {self.Dist_units[i]}")

    def test_Converter_unit_dm(self):
        results: list = [1000, 100, 10, 1, 0.001, 0.000625]
        for i in range(len(self.Dist_units)):
            self.assertEqual(C(10, "dm", self.Dist_units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response dm to {self.Dist_units[i]}")
    def test_Converter_unit_m(self):
        results: list = [10000, 1000, 100, 10, 0.01, 0.00625]
        for i in range(len(self.Dist_units)):
            self.assertEqual(C(10, "m", self.Dist_units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response m to {self.Dist_units[i]}")

    def test_Converter_unit_miles(self):
        results: list = [1600000, 160000, 16000, 1600, 1.6, 1]
        for i in range(len(self.Dist_units)):
            self.assertEqual(C(1, "miles", self.Dist_units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response m to {self.Dist_units[i]}")

    def test_Converter_unit_ml(self):
        results: list = [10, 1, 0.1, 0.001, 0.00001, 0.000001]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(10,"ml",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_cl(self):
        results: list = [100, 10, 1, 0.1, 0.001, 0.0001]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(10,"cl",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_dl(self):
        results: list = [1000, 100, 10, 1, 0.01, 0.001]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(10,"dl",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_l(self):
        results: list = [10000, 1000, 100, 10, 0.1, 0.01]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(10,"l",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_hl(self):
        results: list = [1000000, 100000, 10000, 1000, 10, 1]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(10,"hl",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_m3(self):
        results: list = [1000000, 100000, 10000, 1000, 10, 1]
        for i in range(len(self.Vol_units)):
            self.assertEqual(C(1,"m^3",self.Vol_units[i],"Térfogat").Convert_unit(), results[i],
                             f"Test failed not correct response ml to {self.Dist_units[i]}")
    def test_Converter_unit_g(self):
        results: list = [10, 1, 0.01]
        for i in range(len(self.Weight_units)):
            self.assertEqual(C(10,"g",self.Weight_units[i],"Tömeg").Convert_unit(), results[i],
                             f"Test failed not correct response g to {self.Weight_units[i]}")
    def test_Converter_unit_dkg(self):
        results: list = [100, 10, 0.1]
        for i in range(len(self.Weight_units)):
            self.assertEqual(C(10,"dkg",self.Weight_units[i],"Tömeg").Convert_unit(), results[i],
                             f"Test failed not correct response g to {self.Weight_units[i]}")
    def test_Converter_unit_kg(self):
        results: list = [10000, 1000, 10]
        for i in range(len(self.Weight_units)):
            self.assertEqual(C(10,"kg",self.Weight_units[i],"Tömeg").Convert_unit(), results[i],
                             f"Test failed not correct response g to {self.Weight_units[i]}")