# import unittest to test my code
import unittest


# simple function that adds two numbers
def add(x, y):
    return x + y


# test class for my function
class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        # test if add function works
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


# run tests
if __name__ == '__main__':
    unittest.main()
