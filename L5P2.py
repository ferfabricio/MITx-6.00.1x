import unittest

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.00
    else:
        return base * recurPower(base, exp - 1)

class TestRecurPower(unittest.TestCase):

    def test_three_power_zero(self):
        self.assertEqual(round(recurPower(3, 0), 4), 1.0000)

    def test_three_power_three(self):
        self.assertEqual(round(recurPower(3, 3), 4), 27.0000)

    def test_five_power_two(self):
        self.assertEqual(round(recurPower(5, 2),4), 25.0000)

    def test_eleven_power_two(self):
        self.assertEqual(round(recurPower(11, 2),4), 121.0000)

    def test_negative_power_zero(self):
        self.assertEqual(round(recurPower(-7.62, 0),4), 1.0000)


if __name__ == '__main__':
    unittest.main()
