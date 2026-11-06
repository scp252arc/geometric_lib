import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('asd', 'bsa')
    
    def test_inf_area(self):
        with self.assertRaises(ValueError):
            area(float('inf'), float('inf'))

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-5, 5)

    def test_area(self):
        res = area(10, 20)
        self.assertEqual(res, 200)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('asd', 'ads')

    def test_inf_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(float('inf'), float('inf'))

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, -5)

    def test_perimeter(self):
        res = perimeter(50, 120)
        self.assertEqual(res, 340)