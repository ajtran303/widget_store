import unittest

from widget import calculate_price

class TestCalculatePrice(unittest.TestCase):
    def test_1(self):
        """It multiplies by 10 for quantity less than 10"""
        quantity = 5
        actual = calculate_price(quantity)
        self.assertEqual(actual, 50)
    
    def test_2(self):
        """It multiplies by 10 for quantity equal to 10"""
        quantity = 10
        actual = calculate_price(quantity)
        self.assertEqual(actual, 100)

    def test_3(self):
        """It multiplies by 9 for quantity greater than 10"""
        quantity = 11
        actual = calculate_price(quantity)
        self.assertEqual(actual, 99)

    def test_4(self):
        """It multiplies by 8 for quantity equal to 20"""
        quantity = 20
        actual = calculate_price(quantity)
        self.assertEqual(actual, 160)
    
    def test_5(self):
        """It multiplies by 8 for quantity greater than 20"""
        quantity = 40
        actual = calculate_price(quantity)
        self.assertEqual(actual, 320)

    def test_6(self):
        """It returns a message for quantity 0"""
        quantity = 0
        actual = calculate_price(quantity)
        self.assertEqual(actual, "Invalid quantity")

    def test_7(self):
        """It returns a message for negative quantity"""
        quantity = -1
        actual = calculate_price(quantity)
        self.assertEqual(actual, "Invalid quantity")
    
    def test_8(self):
        """It returns a message for a float quantity"""
        quantity = 1.5
        actual = calculate_price(quantity)
        self.assertEqual(actual, "Invalid quantity")

    def test_9(self):
        """It returns a message for a string quantity"""
        quantity = "One"
        actual = calculate_price(quantity)
        self.assertEqual(actual, "Invalid quantity")




if __name__ == '__main__':
    unittest.main()