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
