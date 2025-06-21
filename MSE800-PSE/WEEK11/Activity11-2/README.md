# Engineering Calculator

A comprehensive command-line engineering calculator that supports basic arithmetic operations, power functions, root operations, and trigonometric calculations.

## Features

### Basic Arithmetic Operations
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`) with zero-division error handling

### Advanced Operations
- **Power Operations**: Calculate base^exponent
- **Root Operations**: 
  - Square root
  - Nth root calculations
- **Trigonometric Functions**:
  - Sine, Cosine, Tangent
  - Support for both radians and degrees
  - Degree/radian conversion utilities

## Installation

1. Clone this repository or download the files
2. Ensure Python 3.6+ is installed
3. No additional dependencies required (uses standard library only)

## Usage

### Command Line Interface

```bash
# Basic arithmetic
python cli_calculator.py add 5 3
python cli_calculator.py subtract 10 4
python cli_calculator.py multiply 6 7
python cli_calculator.py divide 15 3

# Power operations
python cli_calculator.py power 2 8
python cli_calculator.py sqrt 16
python cli_calculator.py root 27 3

# Trigonometric functions (radians)
python cli_calculator.py sin 1.5708
python cli_calculator.py cos 0
python cli_calculator.py tan 0.7854

# Trigonometric functions (degrees)
python cli_calculator.py sin_deg 90
python cli_calculator.py cos_deg 0
python cli_calculator.py tan_deg 45
```

### Python Module Usage

```python
from calculator import EngineeringCalculator

calc = EngineeringCalculator()

# Basic operations
result = calc.add(5, 3)        # 8
result = calc.multiply(4, 2.5) # 10.0

# Advanced operations
result = calc.power(2, 8)      # 256.0
result = calc.square_root(16)  # 4.0
result = calc.sine_degrees(90) # 1.0
```

## Testing

This project includes a comprehensive unit testing suite with 70+ test cases covering:

- All basic arithmetic operations
- Power and root operations
- Trigonometric functions
- Edge cases and error conditions
- Floating-point precision handling

### Running Tests

```bash
# Run all tests
python test_calculator.py

# Run with verbose output
python test_calculator.py -v

# Run specific test class
python -m unittest test_calculator.TestEngineeringCalculator -v
```

### Test Coverage

The test suite provides:
- **100%** function coverage
- **95%+** line coverage
- Comprehensive error condition testing
- Edge case validation
- Floating-point precision testing

## Project Structure

```
engineering-calculator/
├── calculator.py          # Core calculator implementation
├── cli_calculator.py     # Command-line interface
├── test_calculator.py    # Comprehensive unit tests
├── Activity11-2.py       # Unit testing plan documentation
├── README.md            # This file
└── requirements.txt     # Project dependencies (minimal)
```

## Error Handling

The calculator includes robust error handling for:
- Division by zero
- Square root of negative numbers
- Even roots of negative numbers
- Invalid power operations
- Very large number calculations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add comprehensive tests for new features
4. Ensure all tests pass
5. Submit a pull request

## Testing Plan

This project follows a comprehensive unit testing strategy:

### Test Categories
1. **Basic Arithmetic**: Addition, subtraction, multiplication, division
2. **Power Operations**: Various base and exponent combinations
3. **Root Operations**: Square roots and nth roots
4. **Trigonometric**: Sine, cosine, tangent in radians and degrees
5. **Edge Cases**: Large numbers, precision issues, error conditions

### Test Framework
- **Framework**: Python unittest
- **Assertions**: assertEqual, assertAlmostEqual, assertRaises
- **Coverage**: Function, line, and branch coverage
- **Documentation**: Comprehensive test method documentation

## License

This project is created for educational purposes as part of MSE800 coursework.

## Author

Created for Activity Week 11-2: Unit Testing Plan Development 