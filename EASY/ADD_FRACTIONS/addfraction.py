from math import gcd

class Answer:
    def __init__(self, num1, den1, num2, den2):
        if den1 == 0 or den2 == 0:
            raise ValueError("Denominator cannot be zero.")

        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2
    
    def add_fractions(self):
        denominator = gcd(self.den1, self.den2) # Find the greatest common divisor of the denominators
        lcm = (self.den1 * self.den2) // denominator # Calculate the least common multiple of the denominators
        numerator = (self.num1 * (lcm // self.den1)) + (self.num2 * (lcm // self.den2)) # Calculate the numerator of the sum of the fractions
        common_divisor = gcd(numerator, lcm) # Find the greatest common divisor of the numerator and the least common multiple to simplify the fraction
        return (numerator // common_divisor, lcm // common_divisor)
    

num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))

a = Answer(num1, den1, num2, den2)
result = a.add_fractions()
print(f"The sum of the fractions is: {result[0]}/{result[1]})")