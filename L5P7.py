import unittest

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return lenRecur(aStr[:-1]) + 1

class TestLenRecur(unittest.TestCase):

    def test_with_len_one(self):
        self.assertEqual(lenRecur('a'), 1)

    def test_with_len_two(self):
        self.assertEqual(lenRecur('aa'), 2)

    def test_with_len_ten(self):
        self.assertEqual(lenRecur('aaaaaaaaaa'), 10)

if __name__ == '__main__':
    unittest.main()
