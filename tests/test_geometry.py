import unittest

from area_calculator.geometry import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.14159, places=5)

    def test_area_large(self):
        circle = Circle(10)
        self.assertAlmostEqual(circle.area(), 314.159, places=3)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_not_right_angle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angle())


if __name__ == '__main__':
    unittest.main()
