import unittest

from Calculator.Calculator import Calculator
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_results_property_calculator(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean_method_statistics(self):
        self.assertEqual(self.statistics.mean([1, 2, 3]), 2)
        self.assertEqual(self.statistics.result, 2)

    def test_median_method_statistics(self):
        # array odd length
        self.assertEqual(self.statistics.median([1, 3, 2]), 2)
        self.assertEqual(self.statistics.result, 2)

        # array with even length
        self.assertEqual(self.statistics.median([3, 4, 1, 2]), 2.5)
        self.assertEqual(self.statistics.result, 2.5)

    def test_mod_method_statistics(self):
        self.assertEqual(self.statistics.mode([1, 2, 2, 3, 3, 2]), 2)
        self.assertEqual(self.statistics.result, 2)

    def test_variance_method_statistics(self):
        self.assertEqual(self.statistics.variance([6, 3, 8, 5, 3]), 3.6)
        self.assertEqual(self.statistics.result, 3.6)

    def test_std_deviation_method_statistics(self):
        self.assertEqual(self.statistics.std_deviation([6, 3, 8, 5, 3]), 1.8973666)
        self.assertEqual(self.statistics.result, 1.8973666)
