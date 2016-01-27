import unittest

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


class TestGdcRecur(unittest.TestCase):

    def test_with_two_and_twoelve(self):
        self.assertEqual(gcdRecur(2,12), 2)

    def test_with_six_and_twoelve(self):
        self.assertEqual(gcdRecur(6,12), 6)

if __name__ == '__main__':
    unittest.main()
