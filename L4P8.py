import unittest

def square(x):
    '''
    x: int or float.
    '''
    return x * x

def fourthPower(x):
    return square(square(x))

class TestFourthPower(unittest.TestCase):

    def test_with_three(self):
        self.assertEqual(fourthPower(3), 81)

    def test_with_seven(self):
        self.assertEqual(fourthPower(7), 2401)

    def test_with_float(self):
        self.assertEqual(round(fourthPower(1.1),4), 1.4641)


if __name__ == '__main__':
    unittest.main()
