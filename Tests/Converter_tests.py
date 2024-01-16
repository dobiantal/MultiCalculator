import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
import unittest
from App.Converter import Converter as C

class Converter_test(unittest.TestCase):
    units: list = ["mm", "cm", "dm", "m", "km", "miles"]
    def test_Convert_unit_mm(self):
        results: list = [10, 1, 0.1, 0.01, 0.00001, 0.00000625]
        for i in range(len(self.units)):
            self.assertEqual(C(10,"mm",self.units[i],"Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response mm to {self.units[i]}")

    def test_Convert_unit_cm(self):
        results: list = [100, 10, 1, 0.1, 0.0001, 0.0000625]
        for i in range(len(self.units)):
            self.assertEqual(C(10, "cm", self.units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response cm to {self.units[i]}")

    def test_Converter_unit_dm(self):
        results: list = [1000, 100, 10, 1, 0.001, 0.000625]
        for i in range(len(self.units)):
            self.assertEqual(C(10, "dm", self.units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response dm to {self.units[i]}")
    def test_Converter_unit_m(self):
        results: list = [10000, 1000, 100, 10, 0.01, 0.00625]
        for i in range(len(self.units)):
            self.assertEqual(C(10, "m", self.units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response m to {self.units[i]}")

    def test_Converter_unit_miles(self):
        results: list = [1600000, 160000, 16000, 1600, 1.6, 1]
        for i in range(len(self.units)):
            self.assertEqual(C(1, "miles", self.units[i], "Távolság").Convert_unit(), results[i],
                             f"Test failed not correct response m to {self.units[i]}")

