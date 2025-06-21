import math
from typing import Union

class EngineeringCalculator:
    """
    A comprehensive engineering calculator that supports basic arithmetic,
    power operations, roots, and trigonometric functions.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        pass
    
    # Basic Arithmetic Operations
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    # Power Operations
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> float:
        """Calculate base raised to the power of exponent."""
        try:
            return pow(base, exponent)
        except OverflowError:
            raise ValueError("Result too large to compute")
        except ValueError as e:
            raise ValueError(f"Invalid power operation: {e}")
    
    # Root Operations
    def square_root(self, number: Union[int, float]) -> float:
        """Calculate square root of a number."""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(number)
    
    def nth_root(self, number: Union[int, float], n: Union[int, float]) -> float:
        """Calculate nth root of a number."""
        if n == 0:
            raise ValueError("Root degree cannot be zero")
        if number < 0 and n % 2 == 0:
            raise ValueError("Cannot calculate even root of negative number")
        
        if number < 0:
            return -pow(abs(number), 1/n)
        return pow(number, 1/n)
    
    # Trigonometric Functions (input in radians)
    def sine(self, angle: Union[int, float]) -> float:
        """Calculate sine of angle (in radians)."""
        return math.sin(angle)
    
    def cosine(self, angle: Union[int, float]) -> float:
        """Calculate cosine of angle (in radians)."""
        return math.cos(angle)
    
    def tangent(self, angle: Union[int, float]) -> float:
        """Calculate tangent of angle (in radians)."""
        return math.tan(angle)
    
    # Utility functions for degree/radian conversion
    def degrees_to_radians(self, degrees: Union[int, float]) -> float:
        """Convert degrees to radians."""
        return math.radians(degrees)
    
    def radians_to_degrees(self, radians: Union[int, float]) -> float:
        """Convert radians to degrees."""
        return math.degrees(radians)
    
    # Trigonometric functions with degree input
    def sine_degrees(self, degrees: Union[int, float]) -> float:
        """Calculate sine of angle (in degrees)."""
        return self.sine(self.degrees_to_radians(degrees))
    
    def cosine_degrees(self, degrees: Union[int, float]) -> float:
        """Calculate cosine of angle (in degrees)."""
        return self.cosine(self.degrees_to_radians(degrees))
    
    def tangent_degrees(self, degrees: Union[int, float]) -> float:
        """Calculate tangent of angle (in degrees)."""
        return self.tangent(self.degrees_to_radians(degrees)) 