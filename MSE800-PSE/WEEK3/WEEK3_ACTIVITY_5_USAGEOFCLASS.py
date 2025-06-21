class Factorial:
    def __init__(self, number):
        self.num = number

    def calculate(self):
        if self.num < 0:
            return "Invalid number"
        elif self.num == 0:
            return 1
        else:
            result = 1
            for i in range(1, self.num + 1):
                result *= i
            return result

num = int(input('Input a non-negative integer: '))
fac = Factorial(num)
result = fac.calculate()
print(f'The result is {result}')