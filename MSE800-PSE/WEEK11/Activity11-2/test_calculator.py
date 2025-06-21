#!/usr/bin/env python3
"""
Unit Tests for Engineering Calculator
Comprehensive test suite covering all calculator functions and edge cases.
"""

import unittest
import math
from calculator import EngineeringCalculator


class TestEngineeringCalculator(unittest.TestCase):
    """Test class for EngineeringCalculator."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = EngineeringCalculator()
    
    # Test Basic Arithmetic Operations
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10.5, 2.3), 12.8)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(5, -3), 2)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.3), 3.2, places=7)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(0, -100), 0)
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333333, places=5)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        with self.assertRaises(ValueError):
            self.calc.divide(-10, 0)
    
    # Test Power Operations
    def test_power_positive_base(self):
        """Test power with positive base."""
        self.assertEqual(self.calc.power(2, 3), 8.0)
        self.assertEqual(self.calc.power(5, 2), 25.0)
        self.assertEqual(self.calc.power(10, 0), 1.0)
        self.assertEqual(self.calc.power(2, -2), 0.25)
    
    def test_power_negative_base(self):
        """Test power with negative base."""
        self.assertEqual(self.calc.power(-2, 3), -8.0)
        self.assertEqual(self.calc.power(-2, 2), 4.0)
        self.assertEqual(self.calc.power(-5, 0), 1.0)
    
    def test_power_fractional_exponent(self):
        """Test power with fractional exponents."""
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2.0, places=7)
        self.assertAlmostEqual(self.calc.power(8, 1/3), 2.0, places=7)
        self.assertAlmostEqual(self.calc.power(27, 1/3), 3.0, places=7)
    
    def test_power_zero_base(self):
        """Test power with zero base."""
        self.assertEqual(self.calc.power(0, 5), 0.0)
        self.assertEqual(self.calc.power(0, 0), 1.0)
    
    # Test Root Operations
    def test_square_root_positive(self):
        """Test square root of positive numbers."""
        self.assertEqual(self.calc.square_root(4), 2.0)
        self.assertEqual(self.calc.square_root(9), 3.0)
        self.assertEqual(self.calc.square_root(0), 0.0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.414213, places=5)
    
    def test_square_root_negative(self):
        """Test square root of negative numbers raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_nth_root_positive(self):
        """Test nth root of positive numbers."""
        self.assertAlmostEqual(self.calc.nth_root(8, 3), 2.0, places=7)
        self.assertAlmostEqual(self.calc.nth_root(16, 4), 2.0, places=7)
        self.assertAlmostEqual(self.calc.nth_root(32, 5), 2.0, places=7)
        self.assertEqual(self.calc.nth_root(0, 3), 0.0)
    
    def test_nth_root_negative_odd(self):
        """Test nth root of negative numbers with odd roots."""
        self.assertAlmostEqual(self.calc.nth_root(-8, 3), -2.0, places=7)
        self.assertAlmostEqual(self.calc.nth_root(-32, 5), -2.0, places=7)
    
    def test_nth_root_negative_even(self):
        """Test nth root of negative numbers with even roots raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.nth_root(-4, 2)
        with self.assertRaises(ValueError):
            self.calc.nth_root(-16, 4)
    
    def test_nth_root_zero_degree(self):
        """Test nth root with zero degree raises ValueError."""
        with self.assertRaises(ValueError):
            self.calc.nth_root(8, 0)
    
    # Test Trigonometric Functions (Radians)
    def test_sine_radians(self):
        """Test sine function with radian input."""
        self.assertAlmostEqual(self.calc.sine(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.sine(math.pi/2), 1.0, places=7)
        self.assertAlmostEqual(self.calc.sine(math.pi), 0.0, places=7)
        self.assertAlmostEqual(self.calc.sine(3*math.pi/2), -1.0, places=7)
    
    def test_cosine_radians(self):
        """Test cosine function with radian input."""
        self.assertAlmostEqual(self.calc.cosine(0), 1.0, places=7)
        self.assertAlmostEqual(self.calc.cosine(math.pi/2), 0.0, places=7)
        self.assertAlmostEqual(self.calc.cosine(math.pi), -1.0, places=7)
        self.assertAlmostEqual(self.calc.cosine(3*math.pi/2), 0.0, places=7)
    
    def test_tangent_radians(self):
        """Test tangent function with radian input."""
        self.assertAlmostEqual(self.calc.tangent(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.tangent(math.pi/4), 1.0, places=7)
        self.assertAlmostEqual(self.calc.tangent(math.pi), 0.0, places=7)
    
    # Test Trigonometric Functions (Degrees)
    def test_sine_degrees(self):
        """Test sine function with degree input."""
        self.assertAlmostEqual(self.calc.sine_degrees(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.sine_degrees(30), 0.5, places=7)
        self.assertAlmostEqual(self.calc.sine_degrees(90), 1.0, places=7)
        self.assertAlmostEqual(self.calc.sine_degrees(180), 0.0, places=7)
    
    def test_cosine_degrees(self):
        """Test cosine function with degree input."""
        self.assertAlmostEqual(self.calc.cosine_degrees(0), 1.0, places=7)
        self.assertAlmostEqual(self.calc.cosine_degrees(60), 0.5, places=7)
        self.assertAlmostEqual(self.calc.cosine_degrees(90), 0.0, places=7)
        self.assertAlmostEqual(self.calc.cosine_degrees(180), -1.0, places=7)
    
    def test_tangent_degrees(self):
        """Test tangent function with degree input."""
        self.assertAlmostEqual(self.calc.tangent_degrees(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.tangent_degrees(45), 1.0, places=7)
        self.assertAlmostEqual(self.calc.tangent_degrees(180), 0.0, places=7)
    
    # Test Conversion Functions
    def test_degrees_to_radians(self):
        """Test degree to radian conversion."""
        self.assertAlmostEqual(self.calc.degrees_to_radians(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.degrees_to_radians(90), math.pi/2, places=7)
        self.assertAlmostEqual(self.calc.degrees_to_radians(180), math.pi, places=7)
        self.assertAlmostEqual(self.calc.degrees_to_radians(360), 2*math.pi, places=7)
    
    def test_radians_to_degrees(self):
        """Test radian to degree conversion."""
        self.assertAlmostEqual(self.calc.radians_to_degrees(0), 0.0, places=7)
        self.assertAlmostEqual(self.calc.radians_to_degrees(math.pi/2), 90.0, places=7)
        self.assertAlmostEqual(self.calc.radians_to_degrees(math.pi), 180.0, places=7)
        self.assertAlmostEqual(self.calc.radians_to_degrees(2*math.pi), 360.0, places=7)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Additional tests for edge cases and error conditions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = EngineeringCalculator()
    
    def test_very_large_numbers(self):
        """Test calculator with very large numbers."""
        large_num = 1e10
        self.assertEqual(self.calc.add(large_num, large_num), 2e10)
        self.assertEqual(self.calc.multiply(large_num, 2), 2e10)
    
    def test_very_small_numbers(self):
        """Test calculator with very small numbers."""
        small_num = 1e-10
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2e-10, places=15)
        self.assertAlmostEqual(self.calc.multiply(small_num, 2), 2e-10, places=15)
    
    def test_precision_floating_point(self):
        """Test floating point precision issues."""
        # Known floating point precision issue
        result = self.calc.add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3, places=7)


if __name__ == '__main__':
    # Run all tests
    unittest.main(verbosity=2) 