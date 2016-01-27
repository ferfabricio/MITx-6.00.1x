import unittest

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(x, lo) == x and lo or (max(x, hi) == x and hi or x)


class TestClip(unittest.TestCase):

    def test_with_first_negative(self):
        self.assertEqual(clip(-4.01, 2.25, 9.29), 2.25)

    def test_with_small_values(self):
        self.assertEqual(clip(-0.29, 0.84, 0.18), 0.18)

    def test_with_five(self):
        self.assertEqual(clip(-5.62, 5.14, 5.23), 5.14)


if __name__ == '__main__':
    unittest.main()
