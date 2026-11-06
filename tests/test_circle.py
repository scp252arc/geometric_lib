import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('asd')

    def test_inf_area(self):
        with self.assertRaises(ValueError):
            area(float('inf'))

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.15926535897932384626433832795)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('asd')

    def test_inf_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(float('inf'))

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_perimeter(self):
        res = perimeter(50)
        self.assertAlmostEqual(res, 314.15926535897932384626433832795)