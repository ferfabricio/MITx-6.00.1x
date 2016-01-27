import unittest

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = a
    if a > b:
        gcd = b
    while gcd > 1:
        if a % gcd == 0 and b % gcd == 0 :
            break
        else:
            gcd -= 1
    return gcd

class TestGdc(unittest.TestCase):

    def test_with_two_and_twelve(self):
        self.assertEqual(gcdIter(2,12), 2)

    def test_with_six_and_twelve(self):
        self.assertEqual(gcdIter(6,12), 6)

if __name__ == '__main__':
    unittest.main()
