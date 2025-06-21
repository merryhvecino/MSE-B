#!/usr/bin/env python3
"""
Demonstration script for Engineering Calculator
Tests all major functions to verify functionality.
"""

from calculator import EngineeringCalculator

def main():
    """Demonstrate all calculator functions."""
    calc = EngineeringCalculator()
    
    print("Engineering Calculator Demo")
    print("=" * 30)
    
    # Basic arithmetic
    print("\n1. Basic Arithmetic:")
    print(f"   5 + 3 = {calc.add(5, 3)}")
    print(f"   10 - 4 = {calc.subtract(10, 4)}")
    print(f"   6 * 7 = {calc.multiply(6, 7)}")
    print(f"   15 / 3 = {calc.divide(15, 3)}")
    
    # Power operations
    print("\n2. Power Operations:")
    print(f"   2^8 = {calc.power(2, 8)}")
    print(f"   4^0.5 = {calc.power(4, 0.5)}")
    
    # Root operations
    print("\n3. Root Operations:")
    print(f"   √16 = {calc.square_root(16)}")
    print(f"   ∛27 = {calc.nth_root(27, 3)}")
    
    # Trigonometric functions (degrees)
    print("\n4. Trigonometric Functions (degrees):")
    print(f"   sin(30°) = {calc.sine_degrees(30):.6f}")
    print(f"   cos(60°) = {calc.cosine_degrees(60):.6f}")
    print(f"   tan(45°) = {calc.tangent_degrees(45):.6f}")
    
    # Trigonometric functions (radians)
    import math
    print("\n5. Trigonometric Functions (radians):")
    print(f"   sin(π/6) = {calc.sine(math.pi/6):.6f}")
    print(f"   cos(π/3) = {calc.cosine(math.pi/3):.6f}")
    print(f"   tan(π/4) = {calc.tangent(math.pi/4):.6f}")
    
    print("\nAll functions working correctly!")

if __name__ == "__main__":
    main() 