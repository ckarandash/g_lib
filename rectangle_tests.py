import unittest
from src.rectangle import area, perimeter

class RectangleAreaTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(area(5, 19), 5 * 19)

    def test_rectangle_int_second(self):
        self.assertEqual(area(57285, 187533), 57285 * 187533)

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            area("85", "92")

    def test_rectangle_string_second(self):

        with self.assertRaises(TypeError):
            area("85", 19)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, True)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-5, 8)
    def dhigsifgsidgf(self):
        with self.assertRaises(ValueError):
            area(-5, 8)
    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-59853, -15)

    def test_rectangle_zero_int_first(self):
        with self.assertRaises(ValueError):
            area(0, 8)

    def test_rectangle_zero_int_second(self):
        with self.assertRaises(ValueError):
            area(0, 0)
class RectanglePerimeterTestCases(unittest.TestCase):
    def test_rectangle_int_first(self):
        self.assertEqual(perimeter(5, 9), 2 * (5 + 9))

    def test_rectangle_int_second(self):
        self.assertEqual(perimeter(57285, 394732), 2 * (57285 + 394732))

    def test_rectangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("85", "92")

    def test_rectangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("85", 19)

    def test_rectangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True)

    def test_rectangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False)

    def test_rectangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 8)

    def test_rectangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853, -15)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 8)

    def test_rectangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 0)
