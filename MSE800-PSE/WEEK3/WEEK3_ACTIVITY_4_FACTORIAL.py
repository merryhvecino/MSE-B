def factorial(n):
    if n < 0:
        return "Undefined"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

for num in range(5):
    print(f"{num}! = {factorial(num)}")