import unittest
from homework import *


class TestRectangle(unittest.TestCase):
    def test_rectangle_perimeter_int(self):
        test_obj = Rectangle(4, 6)
        expected_result = 20
        self.assertEqual(test_obj.get_rectangle_perimeter(), expected_result)


    def test_rectangle_perimeter_float(self):
        test_obj = Rectangle(4.3, 6.2)
        expected_result = 21
        self.assertEqual(test_obj.get_rectangle_perimeter(), expected_result)


    def test_rectangle_perimeter_with_incorrect_data(self):
        test_obj = Rectangle(5, 0)
        with self.assertRaises(ValueError):
            test_obj.get_rectangle_perimeter()


    def test_rectangle_square_int(self):
        test_obj = Rectangle(2, 7)
        expected_result = 14
        self.assertEqual(test_obj.get_rectangle_square(), expected_result)


    def test_rectangle_square_not_str(self):
        test_obj = Rectangle(2, 7)
        self.assertNotIsInstance(test_obj.get_rectangle_square(), str)

    def test_rectangle_square_with_incorrect_data(self):
        test_obj = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            test_obj.get_rectangle_square()


    def test_sum_of_corners(self):
        test_obj = Rectangle(2, 16)
        self.assertEqual(test_obj.get_sum_of_corners(4), 360)

    def test_sum_of_corners_exeption(self):
        test_obj = Rectangle(2, 16)
        with self.assertRaises(ValueError):
            test_obj.get_sum_of_corners(5)


    def test_rectangle_diagonal(self):
        test_obj = Rectangle(3, 7)
        self.assertAlmostEqual(test_obj.get_rectangle_diagonal(), 7.62, 2)


    def test_rectangle_diagonal_incorrect_data(self):
        test_obj = Rectangle(3, "7")
        with self.assertRaises(TypeError):
            test_obj.get_rectangle_diagonal()


    def test_radius_of_circumscribed_circle(self):
        test_obj = Rectangle(3, 7)
        self.assertAlmostEqual(test_obj.get_radius_of_circumscribed_circle(), 3.81, 2)

    def test_radius_of_circumscribed_circle_incorrect_data(self):
        test_obj = Rectangle([3, ], 7)
        with self.assertRaises(TypeError):
            test_obj.get_radius_of_circumscribed_circle()

    def test_radius_of_inscribed_circle_incorrect_data(self):
        test_obj = Rectangle(2, 3)
        with self.assertRaises(ValueError):
            test_obj.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
