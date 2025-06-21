"""
Activity Week11-3: Understanding Unit Testing

TASK OBJECTIVES:
1. Describe what each test method is checking
2. Run the code and interpret the results  
3. Add new test case that checks if '123'.isdigit() returns True
4. See what happens when assertions fail by changing expected values

This code demonstrates unittest framework with string method testing.
"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # MODIFIED: This test will FAIL - expecting 'foo' but gets 'FOO'
        self.assertEqual('foo'.upper(), 'foo')

    def test_isupper(self):
        # Tests if string is all uppercase
        self.assertTrue('FOO'.isupper())    # 'FOO' is all uppercase = True
        self.assertFalse('Foo'.isupper())  # 'Foo' has lowercase = False

    def test_split(self):
        # Tests splitting strings into lists
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])  # Split by space
        
        # Tests that split() raises error with wrong input type
        with self.assertRaises(TypeError):
            s.split(2)  # Can't split with number 2

    def test_isdigit(self):
        # NEW TEST: Tests if string contains only digits
        self.assertTrue('123'.isdigit())     # '123' has only digits = True
        # '12a' is NOT all digits (has letter 'a'), so isdigit() returns False
        self.assertFalse('12a'.isdigit())    # Test expects False = passes ✅
        self.assertFalse(''.isdigit())       # Empty string = False


if __name__ == '__main__':
    unittest.main()
