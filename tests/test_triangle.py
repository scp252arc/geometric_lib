import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
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
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('asd', 'ads', 'asd')

    def test_inf_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(float('inf'), float('inf'), float('inf'))

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-5, -5,- 5)
    
    def test_impossible_perimeter(self):
        res = perimeter(50, 500, 1000)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)