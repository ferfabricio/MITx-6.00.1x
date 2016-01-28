import unittest

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    i = 0
    for a in aStr:
        i+= 1
    return i

class TestLenIter(unittest.TestCase):

    def test_with_len_one(self):
        self.assertEqual(lenIter('a'), 1)

    def test_with_len_two(self):
        self.assertEqual(lenIter('aa'), 2)

if __name__ == '__main__':
    unittest.main()
