class Factorial:
    def __init__(self, number):
        self.num = num

    def doRun(self, num):
        if (num < 0):
            print("it is an invalid number")
        else:
            if (num == 0):
                return 1
            else:
                return num * self.doRun(num - 1)
            
    def run(self):
        return self.doRun(self.num)   

num = int(float(input('input a number ')))
fac = Factorial(num)
result = fac.run()
print(f'the result is {result}')