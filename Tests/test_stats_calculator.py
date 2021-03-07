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
