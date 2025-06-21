class Prime:

    def __init__(self, num):
        self.num = num

    def factorial(self):
        f = 1
        for i in range(1, self.num + 1):
            f *= i
        return f

    def factors(self):
        return [i for i in range(1, self.num + 1) if self.num % i == 0]

    def is_prime(self):
        return self.factors() == [1, self.num]

num = int(input("Give number: "))
op = Prime(num)

print(f"Factorial: {op.factorial()}")
print(f"Factors: {op.factors()}")
print("Prime" if op.is_prime() else "Not prime")