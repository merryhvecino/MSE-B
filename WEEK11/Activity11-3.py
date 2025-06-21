import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        # MODIFIED: Changed expected value from 'FOO' to 'foo' 
        # to demonstrate test failure
        # This will fail because 'foo'.upper() returns 'FOO', not 'foo'
        self.assertEqual('foo'.upper(), 'foo')

    def test_isupper(self):
        # Test the isupper() method which checks if all letters are uppercase
        # Test 1: 'FOO' should return True (all letters are uppercase)
        self.assertTrue('FOO'.isupper())
        
        # Test 2: 'Foo' should return False (mixed case - 'o' is lowercase)
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # Test the split() method which splits strings into lists
        s = 'hello world'
        
        # Test 1: split() with no arguments splits on whitespace
        self.assertEqual(s.split(), ['hello', 'world'])
        
        # Test 2: Check that s.split() raises TypeError when separator 
        # is not a string (testing error handling)
        with self.assertRaises(TypeError):
            s.split(2)  # This should raise TypeError because 2 is not a string

    def test_isdigit(self):
        # NEW TEST CASE ADDED: Testing the isdigit() string method
        # Test 1: '123' should return True (all characters are digits)
        self.assertTrue('123'.isdigit())
        
        # Test 2: '12a' should return False (contains non-digit character 'a')
        self.assertFalse('12a'.isdigit())
        
        # Test 3: Empty string should return False (no digits present)
        self.assertFalse(''.isdigit())


if __name__ == '__main__':
    unittest.main()
