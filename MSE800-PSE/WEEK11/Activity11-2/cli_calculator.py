#!/usr/bin/env python3
"""
Command-line Engineering Calculator
A comprehensive calculator for basic arithmetic, power, root, and trigonometric operations.
"""

import sys
import argparse
from calculator import EngineeringCalculator


def main():
    """Main function to handle command-line interface."""
    parser = argparse.ArgumentParser(
        description="Engineering Calculator - Command Line Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli_calculator.py add 5 3
  python cli_calculator.py multiply 4 2.5
  python cli_calculator.py power 2 8
  python cli_calculator.py sqrt 16
  python cli_calculator.py sin 1.57
  python cli_calculator.py sin_deg 90
        """
    )
    
    parser.add_argument('operation', 
                       choices=['add', 'subtract', 'multiply', 'divide', 
                               'power', 'sqrt', 'root', 
                               'sin', 'cos', 'tan',
                               'sin_deg', 'cos_deg', 'tan_deg'],
                       help='Mathematical operation to perform')
    
    parser.add_argument('operands', nargs='+', type=float,
                       help='Numbers to operate on')
    
    args = parser.parse_args()
    
    calc = EngineeringCalculator()
    
    try:
        result = perform_operation(calc, args.operation, args.operands)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def perform_operation(calc, operation, operands):
    """Perform the specified operation with given operands."""
    
    # Validate operand count
    if operation in ['add', 'subtract', 'multiply', 'divide', 'power']:
        if len(operands) != 2:
            raise ValueError(f"{operation} requires exactly 2 operands")
    elif operation in ['sqrt', 'sin', 'cos', 'tan', 'sin_deg', 'cos_deg', 'tan_deg']:
        if len(operands) != 1:
            raise ValueError(f"{operation} requires exactly 1 operand")
    elif operation == 'root':
        if len(operands) != 2:
            raise ValueError("root requires exactly 2 operands (number, root_degree)")
    
    # Perform operations
    if operation == 'add':
        return calc.add(operands[0], operands[1])
    elif operation == 'subtract':
        return calc.subtract(operands[0], operands[1])
    elif operation == 'multiply':
        return calc.multiply(operands[0], operands[1])
    elif operation == 'divide':
        return calc.divide(operands[0], operands[1])
    elif operation == 'power':
        return calc.power(operands[0], operands[1])
    elif operation == 'sqrt':
        return calc.square_root(operands[0])
    elif operation == 'root':
        return calc.nth_root(operands[0], operands[1])
    elif operation == 'sin':
        return calc.sine(operands[0])
    elif operation == 'cos':
        return calc.cosine(operands[0])
    elif operation == 'tan':
        return calc.tangent(operands[0])
    elif operation == 'sin_deg':
        return calc.sine_degrees(operands[0])
    elif operation == 'cos_deg':
        return calc.cosine_degrees(operands[0])
    elif operation == 'tan_deg':
        return calc.tangent_degrees(operands[0])
    else:
        raise ValueError(f"Unknown operation: {operation}")


if __name__ == "__main__":
    main() 