


class CalculatorAssing:

    def divisionNumbers(self, a, b):
        if b == 0:
            raise ZeroDivisionError("The divisor must not be zero")
        if type(b) == str:
            raise TypeError("The value must be a integer!")
        return a / b

    def addNumbers(self, a, b):
        return a + b

    def substractionNumebers(self, a, b):
        return a - b

    def multiplicationNumbers(self, a, b):
        return a * b


cal = CalculatorAssing()
# print(cal.divisionNumbers(10, "a"))
# print(cal.divisionNumbers(10,0))
print(cal.addNumbers(10,8))
print(cal.substractionNumebers(10,8))
print(cal.multiplicationNumbers(10,8))
