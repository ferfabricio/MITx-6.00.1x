import unittest

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1.0
    elif exp > 0 and exp % 2 == 1:
        return base * recurPowerNew(base, exp - 1)
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)

class TestRecurPowerNew(unittest.TestCase):

    def test_three_power_zero(self):
        self.assertEqual(round(recurPowerNew(3, 0), 4), 1.0000)

    def test_three_power_three(self):
        self.assertEqual(round(recurPowerNew(3, 3), 4), 27.0000)

    def test_five_power_two(self):
        self.assertEqual(round(recurPowerNew(5, 2),4), 25.0000)

    def test_eleven_power_two(self):
        self.assertEqual(round(recurPowerNew(11, 2),4), 121.0000)

    def test_negative_power_zero(self):
        self.assertEqual(round(recurPowerNew(-7.62, 0),4), 1.0000)


if __name__ == '__main__':
    unittest.main()
